import torch
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from .helper_functions import (
    checkLazyNew,
    generate_dim_variables,
    getIndexTensorAlongDim,
    parse_expr,
    make_zero_like,
    as_tensor,
    get_v_variable,
    get_f_variable
)
from comfy_api.latest import io
import comfy.sampler_helpers
import comfy.model_patcher
import comfy.utils
import comfy.hooks
import comfy.samplers
from .Stack import MrmthStack
from .ParseTree import MrmthParseTree
import copy


class LazyVariableDict(dict):
    def __getitem__(self, key):
        val = super().__getitem__(key)
        if callable(val) and getattr(val, "is_lazy_var", False):
            val = val()
            self[key] = val
        return val

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def copy(self):
        return LazyVariableDict(self)

    def __or__(self, other):
        res = self.copy()
        res.update(other)
        return res

    def __ror__(self, other):
        res = LazyVariableDict(other)
        res.update(self)
        return res

    def __ior__(self, other):
        self.update(other)
        return self


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
                io.MultiType.Input(
                    io.String.Input("Expression", default="V0", multiline=False),
                    types=[io.String,MrmthParseTree],
                    tooltip="Expression to apply on input guiders. Aliases: a=G0, b=G1, c=G2, d=G3, w=F0, x=F1, y=F2, z=F3. Context: steps, current_step",
                ),
                io.MultiType.Input(
                    io.String.Input("Expression1", default="sample", multiline=False),
                    types=[io.String,MrmthParseTree],
                    tooltip="Expression to apply after generation finishes.",
                ),
                io.Boolean.Input(
                    id="remember_stack",
                    default=False,
                    display_name="Remember stack across batch",
                    tooltip=(
                        "If enabled, stack is copied at output leading to changes being remembered during batch operations (node runs multiple times in sucession). If disabled each batch gets it's own copy of the stack."
                    ),
                ),
                MrmthStack.Input(id="stack", tooltip="Access stack between nodes",optional=True)
            ],
            outputs=[
                io.Guider.Output(),
                MrmthStack.Output()
            ],
        )

    @classmethod
    def check_lazy_status(cls, Expression,Expression1, V, F,remember_stack=True,stack={}):
        d = checkLazyNew(Expression,V,F)
        b = checkLazyNew(Expression1,V,F)
        return d|b


    @classmethod
    def execute(cls, V, F, Expression, Expression1,remember_stack = True, stack=None):
        stack = stack if remember_stack else (copy.deepcopy(stack) if stack is not None else {})
        guider = MathGuider(V, F, Expression, Expression1, stack);
        stack = stack if remember_stack else copy.deepcopy(stack)
        return (guider, stack)


class MathGuider:
    def __init__(self, V, F, expression,expression1,stack):
        self.V = V
        self.F = F
        self.expression = expression
        if isinstance(expression,str):
            self.tree = parse_expr(expression)
        else:
            self.tree = expression
        if isinstance(expression1,str):
            self.tree1 = parse_expr(expression1)
        else:
            self.tree1 = expression1
        self.inner_model = None  # Will be set during sample
        self.sigmas = None
        self.current_step = 0
        self.steps = 0
        self.stck = stack

    @property
    def model_patcher(self):
        for v in self.V.values():
            if v is not None and hasattr(v, "model_patcher"):
                return v.model_patcher

        return None

    def __call__(self, x, sigma, model_options={}, seed=None):
        lazy_g_results = {}

        zero_cache = [None]
        def get_zero_cache():
            if zero_cache[0] is None:
                zero_cache[0] = torch.zeros_like(x)
            return zero_cache[0]

        def make_lazy(guider_obj):
            def lazy_eval():
                if guider_obj is not None:
                    return guider_obj(x, sigma, model_options=model_options, seed=seed)
                return get_zero_cache()
            lazy_eval.is_lazy_var = True
            return lazy_eval

        for k, guider in self.V.items():
            lazy_g_results[k] = make_lazy(guider)

        eval_samples, variables = self.setVars(x, sigma, seed, lazy_g_results)
        visitor = UnifiedMathVisitor(variables, eval_samples.shape,eval_samples.device,state_storage=self.stck)
        result_tensor = visitor.visit(self.tree)
        self.current_step = self.current_step + 1;
        return as_tensor(result_tensor, eval_samples.shape).to(x.device)


    def setVars(self, x, sigma, seed, g_results):
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

        variables = LazyVariableDict()
        variables.update({
            "w": self.F.get("F0", 0.0),
            "x": self.F.get("F1", 0.0),
            "y": self.F.get("F2", 0.0),
            "z": self.F.get("F3", 0.0),
            "B": getIndexTensorAlongDim(eval_samples, batch_dim),
            "batch": getIndexTensorAlongDim(eval_samples, batch_dim),
            "W": float(eval_samples.shape[width_dim]) if width_dim < ndim else 0.0,
            "width": float(eval_samples.shape[width_dim]) if width_dim < ndim else 0.0,
            "H": float(eval_samples.shape[height_dim]) if height_dim < ndim else 0.0,
            "height": float(eval_samples.shape[height_dim]) if height_dim < ndim else 0.0,
            "T": float(frame_count),
            "batch_count": float(eval_samples.shape[0]),
            "N": float(eval_samples.shape[channel_dim]) if channel_dim < ndim else 0.0,
            "channel_count": float(eval_samples.shape[channel_dim]) if channel_dim < ndim else 0.0,
            "sigma": sigma.item() if isinstance(sigma,torch.Tensor) else sigma,
            "seed": seed if seed is not None else 0,
            "steps": self.steps,
            "current_step": self.current_step,
            "sample": x
        })
        if g_results is not None:
            for k, func in g_results.items():
                variables[k] = func

            def lazy_a(): return variables["V0"] if "V0" in g_results else make_zero_like(eval_samples)
            lazy_a.is_lazy_var = True
            variables["a"] = lazy_a

            def lazy_b(): return variables["V1"] if "V1" in g_results else make_zero_like(eval_samples)
            lazy_b.is_lazy_var = True
            variables["b"] = lazy_b

            def lazy_c(): return variables["V2"] if "V2" in g_results else make_zero_like(eval_samples)
            lazy_c.is_lazy_var = True
            variables["c"] = lazy_c

            def lazy_d(): return variables["V3"] if "V3" in g_results else make_zero_like(eval_samples)
            lazy_d.is_lazy_var = True
            variables["d"] = lazy_d

            def lazy_stacked_v():
                evaluated_g_results = {k: variables[k] for k in g_results.keys()}
                v_stacked, v_cnt = get_v_variable(evaluated_g_results)
                return v_stacked
            lazy_stacked_v.is_lazy_var = True

            def lazy_v_cnt():
                evaluated_g_results = {k: variables[k] for k in g_results.keys()}
                v_stacked, v_cnt = get_v_variable(evaluated_g_results)
                return float(v_cnt)
            lazy_v_cnt.is_lazy_var = True

            variables["V"] = lazy_stacked_v
            variables["Vcnt"] = lazy_v_cnt
            variables["V_count"] = lazy_v_cnt

        for k, v in self.F.items():
            variables[k] = v if v is not None else 0.0

        f_stacked, f_cnt = get_f_variable(self.F)
        if f_stacked is not None:
             variables["F"] = f_stacked
             variables["Fcnt"] = float(f_cnt)
             variables["F_count"] = float(f_cnt)

        variables.update(generate_dim_variables(eval_samples))
        return eval_samples,variables

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

                eval_samples, variables = self.setVars(output, 0.0, seed, None)
                variables["noise"] = noise
                variables["previous_sample"] = latent_image
                visitor = UnifiedMathVisitor(variables, eval_samples.shape,state_storage=self.stck)
                output = visitor.visit(self.tree1)

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
