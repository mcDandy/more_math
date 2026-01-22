import torch
import re
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from .helper_functions import (
    generate_dim_variables,
    getIndexTensorAlongDim,
    parse_expr,
    make_zero_like,
    as_tensor,
)
from comfy_api.latest import io
import comfy.sampler_helpers
import comfy.model_patcher
import comfy.utils
import comfy.hooks
import comfy.samplers


class GuiderMathNode(io.ComfyNode):
    """
    Enables math expressions on Guiders (sampler inputs) with autogrow support.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_GuiderMathNode",
            category="More math",
            display_name="Guider math",
            inputs=[
                io.Autogrow.Input(id="V", template=io.Autogrow.TemplatePrefix(io.Guider.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Guider", default="G0*(1-F0)+G1*F0", tooltip="Expression to apply on input guiders. Aliases: a=G0, b=G1, c=G2, d=G3, w=F0, x=F1, y=F2, z=F3. Context: steps, current_step"),
            ],
            outputs=[
                io.Guider.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Guider, V, F):
        input_stream = InputStream(Guider)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()

        # Support aliases
        aliases_smp = {"a": "V0", "b": "V1", "c": "V2", "d": "V3"}
        aliases_flt = {"w": "F0", "x": "F1", "y": "F2", "z": "F3"}

        needed = []
        needed1 = []
        for token in filter(lambda t: t.type == MathExprParser.VARIABLE, stream.tokens):
            var_name = token.text
            if re.match(r"[VF][0-9]+", var_name):
                needed.append(var_name)
            elif var_name in aliases_smp:
                needed.append(aliases_smp[var_name])
            elif var_name in aliases_flt:
                needed.append(aliases_flt[var_name])

        for v in needed:
            if v.startswith("V"):
                if v not in V or V[v] is None:
                    needed1.append(v)
            elif v.startswith("F"):
                if v not in F or F[v] is None:
                    needed1.append(v)
        return needed1

    @classmethod
    def execute(cls, V, F, Guider):
        return (MathGuider(V, F, Guider),)


class MathGuider:
    def __init__(self, V, F, expression):
        self.V = V
        self.F = F
        self.expression = expression
        self.tree = parse_expr(expression)
        self.inner_model = None  # Will be set during sample
        self.sigmas = None
        self.current_step = 0
        self.steps = 0

    @property
    def model_patcher(self):
        # Return the model patcher of the first valid guider
        # This is needed because some nodes (like SamplerCustomAdvanced) inspect the model via the guider
        for v in self.V.values():
            if v is not None and hasattr(v, "model_patcher"):
                return v.model_patcher
        # If no guider has it (e.g. all None or bare wrappers), try to return shared inner model's patcher if available?
        # But usually we need it before inner_model is set.
        # So we just return None which might fail later if caller doesn't check.
        return None

    def __call__(self, x, sigma, model_options={}, seed=None):
        g_results = {}
        for k, guider in self.V.items():
            if guider is not None:
                g_results[k] = guider(x, sigma, model_options=model_options, seed=seed)
            else:
                g_results[k] = torch.zeros_like(x)

        eval_samples = x
        ndim = eval_samples.ndim

        batch_dim = 0
        channel_dim = 1
        height_dim = 2
        width_dim = 3
        time_dim = None

        if ndim >= 5:
            time_dim = 2
            channel_dim = 1
            height_dim = 3
            width_dim = 4

        frame_count = eval_samples.shape[time_dim] if time_dim is not None else 1

        variables = {
            "w": self.F.get("F0", 0.0),
            "x": self.F.get("F1", 0.0),
            "y": self.F.get("F2", 0.0),
            "z": self.F.get("F3", 0.0),
            "B": getIndexTensorAlongDim(eval_samples, batch_dim),
            "batch": getIndexTensorAlongDim(eval_samples, batch_dim),
            "W": eval_samples.shape[width_dim] if width_dim < ndim else 0,
            "width": eval_samples.shape[width_dim] if width_dim < ndim else 0,
            "H": eval_samples.shape[height_dim] if height_dim < ndim else 0,
            "height": eval_samples.shape[height_dim] if height_dim < ndim else 0,
            "T": frame_count,
            "batch_count": eval_samples.shape[0],
            "N": eval_samples.shape[channel_dim] if channel_dim < ndim else 0,
            "channel_count": eval_samples.shape[channel_dim] if channel_dim < ndim else 0,
            "sigma": sigma.item(),
            "seed": seed if seed is not None else 0,
            "steps": self.steps,
            "current_step": self.current_step,
        }

        variables.update(g_results)
        variables.update({
            "a": g_results.get("V0", make_zero_like(eval_samples)),
            "b": g_results.get("V1", make_zero_like(eval_samples)),
            "c": g_results.get("V2", make_zero_like(eval_samples)),
            "d": g_results.get("V3", make_zero_like(eval_samples)),
        })

        for k, v in self.F.items():
            variables[k] = v if v is not None else 0.0

        variables.update(generate_dim_variables(eval_samples))

        visitor = UnifiedMathVisitor(variables, eval_samples.shape)
        result_tensor = visitor.visit(self.tree)
        self.current_step = self.current_step + 1;
        return as_tensor(result_tensor, eval_samples.shape).to(x.device)

    def sample(self, noise, latent_image, sampler, sigmas, denoise_mask=None, callback=None, disable_pbar=False, seed=None):
        self.sigmas = sigmas
        self.steps = len(sigmas)
        if sigmas.shape[-1] == 0:
            return latent_image

        active_guiders = [g for g in self.V.values() if g is not None]
        if not active_guiders:
            return latent_image

        primary_guider = active_guiders[0]
        cleanup_items = []

        try:
            for guider in active_guiders:
                if hasattr(guider, "original_conds"):
                    guider.conds = {}
                    for k in guider.original_conds:
                        guider.conds[k] = list(map(lambda a: a.copy(), guider.original_conds[k]))

                if hasattr(comfy.samplers, "preprocess_conds_hooks") and hasattr(guider, "conds"):
                     comfy.samplers.preprocess_conds_hooks(guider.conds)

                if hasattr(guider, "model_patcher"):
                    guider._orig_model_options = guider.model_options
                    guider.model_options = comfy.model_patcher.create_model_options_clone(guider.model_options)
                    comfy.sampler_helpers.prepare_model_patcher(guider.model_patcher, guider.conds, guider.model_options)
                    if hasattr(comfy.samplers, "filter_registered_hooks_on_conds"):
                        comfy.samplers.filter_registered_hooks_on_conds(guider.conds, guider.model_options)

                    guider.inner_model, guider.conds, guider.loaded_models = comfy.sampler_helpers.prepare_sampling(
                        guider.model_patcher, noise.shape, guider.conds, guider.model_options
                    )

                    cleanup_items.append(guider)

            device = primary_guider.model_patcher.load_device
            noise = noise.to(device)
            latent_image = latent_image.to(device)
            sigmas = sigmas.to(device)

            for guider in active_guiders:
                if hasattr(guider, "model_options"):
                     comfy.samplers.cast_to_load_options(guider.model_options, device=device, dtype=guider.model_patcher.model_dtype())

            patchers = set(g.model_patcher for g in active_guiders if hasattr(g, "model_patcher"))
            for p in patchers:
                p.pre_run()

            try:
                if latent_image is not None and torch.count_nonzero(latent_image) > 0:
                    latent_image = primary_guider.inner_model.process_latent_in(latent_image)

                for guider in active_guiders:
                     if hasattr(guider, "inner_model") and hasattr(guider, "conds"):
                         guider.conds = comfy.samplers.process_conds(
                             guider.inner_model, noise, guider.conds, device, latent_image, denoise_mask, seed
                         )

                self.inner_model = primary_guider.inner_model

                extra_model_options = comfy.model_patcher.create_model_options_clone(primary_guider.model_options)
                extra_model_options.setdefault("transformer_options", {})["sample_sigmas"] = sigmas
                extra_args = {"model_options": extra_model_options, "seed": seed}

                output = sampler.sample(self, sigmas, extra_args, callback, noise, latent_image, denoise_mask, disable_pbar)

                if hasattr(primary_guider.inner_model, "process_latent_out"):
                     output = primary_guider.inner_model.process_latent_out(output.to(torch.float32))

                return output

            finally:
                for p in patchers:
                    p.cleanup()

        finally:
            for guider in cleanup_items:
                if hasattr(guider, "model_patcher") and hasattr(guider, "loaded_models"):
                     comfy.sampler_helpers.cleanup_models(guider.conds, guider.loaded_models)
                     if hasattr(guider, "_orig_model_options"):
                         comfy.samplers.cast_to_load_options(guider.model_options, device=guider.model_patcher.offload_device)
                         guider.model_options = guider._orig_model_options
                         guider.model_patcher.restore_hook_patches()

                     del guider.inner_model
                     del guider.loaded_models
                     del guider.conds
                     if hasattr(guider, "_orig_model_options"): del guider._orig_model_options

            self.inner_model = None
