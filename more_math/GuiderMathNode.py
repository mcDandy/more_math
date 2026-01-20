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


class GuiderMathNode(io.ComfyNode):
    """
    Enables math expressions on Guiders (sampler inputs) with autogrow support.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_GuiderMathNode",
            category="More math",
            display_name="Guider math",
            inputs=[
                io.Autogrow.Input(id="G", template=io.Autogrow.TemplatePrefix(io.Guider.Input("guider"), prefix="G", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Guider", default="G0*(1-F0)+G1*F0", tooltip="Expression to apply on input guiders. Aliases: a=G0, b=G1, c=G2, d=G3, w=F0, x=F1, y=F2, z=F3"),
            ],
            outputs=[
                io.Guider.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Guider, G, F):
        input_stream = InputStream(Guider)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()

        # Support aliases
        aliases_smp = {"a": "G0", "b": "G1", "c": "G2", "d": "G3"}
        aliases_flt = {"w": "F0", "x": "F1", "y": "F2", "z": "F3"}

        needed = []
        needed1 = []
        for token in filter(lambda t: t.type == MathExprParser.VARIABLE, stream.tokens):
            var_name = token.text
            if re.match(r"[GF][0-9]+", var_name):
                needed.append(var_name)
            elif var_name in aliases_smp:
                needed.append(aliases_smp[var_name])
            elif var_name in aliases_flt:
                needed.append(aliases_flt[var_name])

        for v in needed:
            if v.startswith("G"):
                if v not in G or G[v] is None:
                    needed1.append(v)
            elif v.startswith("F"):
                if v not in F or F[v] is None:
                    needed1.append(v)
        return needed1

    @classmethod
    def execute(cls, G, F, Guider):
        return (MathGuider(G, F, Guider),)


class MathGuider:
    def __init__(self, G, F, expression):
        self.G = G
        self.F = F
        self.expression = expression
        self.tree = parse_expr(expression)
        self.inner_model = None  # Will be set during sample
    
    @property
    def model_patcher(self):
        # Return the model patcher of the first valid guider
        # This is needed because some nodes (like SamplerCustomAdvanced) inspect the model via the guider
        for g in self.G.values():
            if g is not None and hasattr(g, "model_patcher"):
                return g.model_patcher
        # If no guider has it (e.g. all None or bare wrappers), try to return shared inner model's patcher if available?
        # But usually we need it before inner_model is set. 
        # So we just return None which might fail later if caller doesn't check.
        return None

    def __call__(self, x, sigma, model_options={}, seed=None):
        print("__call__")
        # Collect predictions from all guiders
        g_results = {}
        for k, guider in self.G.items():
            if guider is not None:
                g_results[k] = guider(x, sigma, model_options=model_options, seed=seed)
            else:
                g_results[k] = torch.zeros_like(x)

        # Handle NestedTensor logic similar to SamplerMathNode but for noise predictions
        # Usually noise predictions match x shape directly

        # Context variables
        eval_samples = x
        ndim = eval_samples.ndim

        # Depending on if it's batched or not, dimensions might vary
        # Expected shape [B, C, H, W]
        # x comes from KSamplerX0Inpaint call which passes x (latent)

        batch_dim = 0
        channel_dim = 1
        height_dim = 2
        width_dim = 3
        time_dim = None # standard 4D latent

        # Heuristic for dimensions based on SamplerMathNode
        if ndim == 3: # Flattened? or 1D?
            pass
        if ndim == 4:
            pass
        if ndim >= 5:
            time_dim = 2 # [B, C, T, H, W]? or [B, F, C, H, W]
            channel_dim = 1
            height_dim = 3
            width_dim = 4

        # SamplerMathNode used negative indices. Let's stick to safe assumptions or reuse helper
        # generate_dim_variables uses shape

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
            "sigma": sigma, # sigma is scalar or tensor? usually tensor broadcastable
            "test_sigma": sigma,
            "seed": seed if seed is not None else 0,
        }

        # Add dynamic inputs and aliases
        variables.update(g_results)
        variables.update({
            "a": g_results.get("G0", make_zero_like(eval_samples)),
            "b": g_results.get("G1", make_zero_like(eval_samples)),
            "c": g_results.get("G2", make_zero_like(eval_samples)),
            "d": g_results.get("G3", make_zero_like(eval_samples)),
        })

        # Add F inputs
        for k, v in self.F.items():
            variables[k] = v if v is not None else 0.0

        variables.update(generate_dim_variables(eval_samples))

        visitor = UnifiedMathVisitor(variables, eval_samples.shape)
        result_tensor = visitor.visit(self.tree)
        # Result should be noise prediction, matching x shape
        return as_tensor(result_tensor, eval_samples.shape)

    def sample(self, noise, latent_image, sampler, sigmas, denoise_mask=None, callback=None, disable_pbar=False, seed=None):
        print("sample")
        if sigmas.shape[-1] == 0:
            return latent_image

        # 1. Setup all guiders
        # We need to replicate what CFGGuider.sample does for each sub-guider to prepare them
        # (conds processing, model patching)

        # Group guiders by model_patcher to avoid double patching if possible,
        # but prepare_sampling creates a NEW inner_model wrapper, so safe to call multiple times?
        # CFGGuider.sample sets self.inner_model.

        # We will iterate and setup each.
        active_guiders = [g for g in self.G.values() if g is not None]
        if not active_guiders:
            return latent_image # Or zero noise? But without model we can't do anything really.

        # Assume G0 is the primary one for model properties (like noise scaling)
        primary_guider = active_guiders[0]

        # We hold a list of cleanup functions or objects
        cleanup_items = []

        try:
            # Setup phase
            for guider in active_guiders:
                # Assuming guider is CFGGuider-like
                if hasattr(guider, "original_conds"):
                    guider.conds = {}
                    for k in guider.original_conds:
                        guider.conds[k] = list(map(lambda a: a.copy(), guider.original_conds[k]))

                # Run standard hooks/preprocessing if available
                if hasattr(comfy.samplers, "preprocess_conds_hooks") and hasattr(guider, "conds"):
                     comfy.samplers.preprocess_conds_hooks(guider.conds)

                # Prepare model patcher
                if hasattr(guider, "model_patcher"):
                    # Backup options
                    guider._orig_model_options = guider.model_options
                    guider.model_options = comfy.model_patcher.create_model_options_clone(guider.model_options)

                    # Hint: Hook mode handling?
                    # For now simplified:
                    comfy.sampler_helpers.prepare_model_patcher(guider.model_patcher, guider.conds, guider.model_options)

                    if hasattr(comfy.samplers, "filter_registered_hooks_on_conds"):
                        comfy.samplers.filter_registered_hooks_on_conds(guider.conds, guider.model_options)

                    # Prepare sampling (loads model)
                    guider.inner_model, guider.conds, guider.loaded_models = comfy.sampler_helpers.prepare_sampling(
                        guider.model_patcher, noise.shape, guider.conds, guider.model_options
                    )

                    cleanup_items.append(guider)

            # Load devices and cast options
            # Again, assuming primary guider dictates the device
            device = primary_guider.model_patcher.load_device
            noise = noise.to(device)
            latent_image = latent_image.to(device)
            sigmas = sigmas.to(device)

            # Cast load options for all
            for guider in active_guiders:
                if hasattr(guider, "model_options"):
                     comfy.samplers.cast_to_load_options(guider.model_options, device=device, dtype=guider.model_patcher.model_dtype())

            # Pre-run models
            # Just run pre_run on all patchers. Unique them?
            # If they share the patcher, pre_run might be idempotent or ref-counted?
            # ModelPatcher.pre_run is NOT ref counted usually.
            # But usually we shouldn't mix different models.
            # If they are same patcher, we should only call once.

            patchers = set(g.model_patcher for g in active_guiders if hasattr(g, "model_patcher"))
            for p in patchers:
                p.pre_run()

            try:
                # Helper to process latent in/out
                # Using primary guider logic
                if latent_image is not None and torch.count_nonzero(latent_image) > 0:
                    latent_image = primary_guider.inner_model.process_latent_in(latent_image)

                # Process conds for all guiders (area masks etc)
                for guider in active_guiders:
                     if hasattr(guider, "inner_model") and hasattr(guider, "conds"):
                         guider.conds = comfy.samplers.process_conds(
                             guider.inner_model, noise, guider.conds, device, latent_image, denoise_mask, seed
                         )

                # Set inner_model of self to primary's inner_model so KSampler can access it
                self.inner_model = primary_guider.inner_model

                # Execute Sampler
                # We need a wrapper executor like CFGGuider does?
                # "executor.execute(self, sigmas, ...)"
                # But here 'self' is the 'model' passed to sampler.

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
            # Cleanup guiders
            for guider in cleanup_items:
                if hasattr(guider, "model_patcher") and hasattr(guider, "loaded_models"):
                     comfy.sampler_helpers.cleanup_models(guider.conds, guider.loaded_models)
                     if hasattr(guider, "_orig_model_options"):
                         # restore options? CFGGuider does logic with load_options casting back to offload
                         comfy.samplers.cast_to_load_options(guider.model_options, device=guider.model_patcher.offload_device)
                         guider.model_options = guider._orig_model_options
                         # restore hook patches
                         guider.model_patcher.restore_hook_patches()

                     del guider.inner_model
                     del guider.loaded_models
                     del guider.conds
                     if hasattr(guider, "_orig_model_options"): del guider._orig_model_options

            self.inner_model = None
