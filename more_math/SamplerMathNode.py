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
from comfy.nested_tensor import NestedTensor


class SamplerMathNode(io.ComfyNode):
    """
    Enables math expressions on Samplers with autogrow support.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_SamplerMathNode",
            category="More math",
            display_name="Sampler math",
            inputs=[
                io.Autogrow.Input(id="V", template=io.Autogrow.TemplatePrefix(io.Sampler.Input("sampler"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Sampler", default="V0*(1-F0)+V1*F0", tooltip="Expression to apply on input samplers"),
            ],
            outputs=[
                io.Sampler.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Sampler, V, F):
        input_stream = InputStream(Sampler)
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
    def execute(cls, V, F, Sampler):
        return (SamplerExecutor(V, F, Sampler),)

class SamplerExecutor:
    def __init__(self, V, F, expression):
        self.V = V
        self.F = F
        self.expression = expression
        self.tree = parse_expr(expression)

    def sample(self, model_wrap, sigmas, extra_args, callback, noise, latent_image=None, denoise_mask=None, disable_pbar=False):
        ref_latent = latent_image if latent_image is not None else noise

        # Invoke all input samplers
        v_results = {}
        for k, sampler in self.V.items():
            if sampler is not None:
                v_results[k] = sampler.sample(model_wrap, sigmas, extra_args, callback, noise, latent_image, denoise_mask, disable_pbar)
            else:
                v_results[k] = make_zero_like(ref_latent)

        # Handle NestedTensor common in NoiseMathNode
        # Template follows closely to LatentMathNode.py
        is_nested = getattr(ref_latent, "is_nested", False)
        orig_split_sizes = None
        eval_samples = ref_latent

        if is_nested:
            orig_split_sizes = [t.shape[0] for t in ref_latent.unbind()]
            eval_samples = torch.cat(ref_latent.unbind(), dim=0)

            # Flatten all sampler results to match the merged reference latent
            for k, val in v_results.items():
                if getattr(val, "is_nested", False):
                    v_results[k] = torch.cat(val.unbind(), dim=0)
                elif torch.is_tensor(val):
                    if val.shape[0] == len(orig_split_sizes) and val.shape[0] != eval_samples.shape[0]:
                        # Handle "per-subtensor" results by expanding them to match sub-batch sizes
                        v_results[k] = torch.cat(
                            [val[i].unsqueeze(0).expand(orig_split_sizes[i], *val.shape[1:]) for i in range(len(orig_split_sizes))],
                            dim=0,
                        )
                    # If it's already a regular tensor, we assume it's either broadcastable or already matches
                elif val is None:
                    v_results[k] = make_zero_like(eval_samples)

        # Context variables
        ndim = eval_samples.ndim
        batch_dim = 0
        channel_dim = -3
        height_dim = -2
        width_dim = -1
        time_dim = -4 if ndim >= 5 else None

        frame_count = eval_samples.shape[time_dim] if time_dim is not None else eval_samples.shape[batch_dim]

        variables = {
            "w": self.F.get("F0", 0.0),
            "x": self.F.get("F1", 0.0),
            "y": self.F.get("F2", 0.0),
            "z": self.F.get("F3", 0.0),
            "B": getIndexTensorAlongDim(eval_samples, batch_dim),
            "batch": getIndexTensorAlongDim(eval_samples, batch_dim),
            "W": eval_samples.shape[width_dim],
            "width": eval_samples.shape[width_dim],
            "H": eval_samples.shape[height_dim],
            "height": eval_samples.shape[height_dim],
            "T": frame_count,
            "batch_count": eval_samples.shape[0],
            "N": eval_samples.shape[channel_dim],
            "channel_count": eval_samples.shape[1],
            "sigmas": sigmas,
            "seed": extra_args.get("seed", 0),
            "noise": noise,
            "latent": latent_image,
            "mask": denoise_mask,
        }

        # Add dynamic inputs and aliases
        variables.update(v_results)
        variables.update({
            "a": v_results.get("V0", make_zero_like(eval_samples)),
            "b": v_results.get("V1", make_zero_like(eval_samples)),
            "c": v_results.get("V2", make_zero_like(eval_samples)),
            "d": v_results.get("V3", make_zero_like(eval_samples)),
        })

        # Add F inputs
        for k, v in self.F.items():
            variables[k] = v if v is not None else 0.0

        if width_dim is not None: variables["X"] = getIndexTensorAlongDim(eval_samples, width_dim)
        if height_dim is not None: variables["Y"] = getIndexTensorAlongDim(eval_samples, height_dim)
        if channel_dim is not None: variables["C"] = getIndexTensorAlongDim(eval_samples, channel_dim)
        if time_dim is not None:
            F_idx = getIndexTensorAlongDim(eval_samples, time_dim)
            variables.update({"frame": F_idx, "frame_count": frame_count})

        variables.update(generate_dim_variables(eval_samples))

        visitor = UnifiedMathVisitor(variables, eval_samples.shape)
        result_tensor = visitor.visit(self.tree)
        merged_result = as_tensor(result_tensor, eval_samples.shape)

        if is_nested and orig_split_sizes is not None:
            return NestedTensor(torch.split(merged_result, orig_split_sizes, dim=0))

        return merged_result
