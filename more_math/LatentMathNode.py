from inspect import cleandoc
from comfy_api.latest import io
from .helper_functions import (
    generate_dim_variables,
    getIndexTensorAlongDim,
    parse_expr,
    as_tensor,
    normalize_to_common_shape,
    prepare_inputs,
    make_zero_like
)
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
import torch
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
import re


class LatentMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Latents using Autogrow inputs.
    """

    def __init__(self):
        pass

    @classmethod
    def define_schema(cls) -> io.Schema:
        """ """
        return io.Schema(
            node_id="mrmth_ag_LatentMathNode",
            display_name="Latent math",
            category="More math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Latent.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Expression", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on input latents"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["error", "error", "pad"],
                    default="error",
                    tooltip="How to handle mismatched latent batch sizes. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                )
            ],
            outputs=[
                io.Latent.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Expression, V, F, length_mismatch="tile"):

        input_stream = InputStream(Expression)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()

        # Support aliases
        aliases_img = {"a": "V0", "b": "V1", "c": "V2", "d": "V3"}
        aliases_flt = {"w": "F0", "x": "F1", "y": "F2", "z": "F3"}

        needed = []
        needed1 = []
        for token in filter(lambda t: t.type == MathExprParser.VARIABLE, stream.tokens):
            var_name = token.text

            if re.match(r"[VF][0-9]+", var_name):
                needed.append(var_name)
            elif var_name in aliases_img:
                needed.append(aliases_img[var_name])
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
    def execute(cls, V, F, Expression, length_mismatch="tile") -> io.NodeOutput:
        # Determine reference latent
        ref_latent = None
        for lat in V.values():
            if lat is not None:
                ref_latent = lat
                break

        if ref_latent is None:
             raise ValueError("At least one input is required.")

        # Identify if any input is a NestedTensor and track original sizes for restoration
        stacked = False
        orig_split_sizes = None

        # Check all present inputs for nested tensors
        for item in V.values():
            if item is not None:
                samples = item.get("samples")
                if getattr(samples, "is_nested", False):
                    stacked = True
                    # Store original split sizes (batch dimension) - assume all nested inputs share structure if mixed?
                    # Or just take from the first one found.
                    orig_split_sizes = [t.shape[0] for t in samples.tensors]
                    break

        # Flatten nested tensors in V
        if stacked:
            for k, val in V.items():
                if val is not None and getattr(val.get("samples"), "is_nested", False):
                    new_val = val.copy()
                    new_val["samples"] = torch.cat(new_val["samples"].tensors, dim=0)
                    V[k] = new_val

        a = V.get("V0")
        b = V.get("V1")
        c = V.get("V2")
        d = V.get("V3")

        if a is None:
            a = make_zero_like(ref_latent)

        a_c, b_c, c_c, d_c = prepare_inputs(a, b, c, d)
        at,bt,ct,dt = a_c["samples"],b_c["samples"],c_c["samples"],d_c["samples"]

        if(length_mismatch == "error"):
            max_length = at.shape[0]
            for name, val in V.items():
                if val is not None:
                    tensor = val["samples"]
                    if tensor.shape[0] != max_length:
                         raise ValueError(f"Input '{name}' has shape {tensor.shape[0]}, expected {max_length} to match largest input.")

        ae, be, ce, de = normalize_to_common_shape(at, bt, ct, dt, mode=length_mismatch)

        # parse expression once
        tree = parse_expr(Expression)

        ndim = ae.ndim
        batch_dim = 0
        channel_dim = -3
        height_dim = -2
        width_dim = -1
        time_dim = None
        if ndim >= 5:
            time_dim = -4

        frame_count = ae.shape[time_dim] if time_dim is not None else ae.shape[batch_dim]

        variables = {
            "a": ae, "b": be, "c": ce, "d": de,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "X": getIndexTensorAlongDim(ae, width_dim),
            "Y": getIndexTensorAlongDim(ae, height_dim),
            "B": getIndexTensorAlongDim(ae, batch_dim),
            "batch": getIndexTensorAlongDim(ae, batch_dim),
            "C": getIndexTensorAlongDim(ae, channel_dim),
            "channel": getIndexTensorAlongDim(ae, channel_dim),
            "W": ae.shape[width_dim],
            "width": ae.shape[width_dim],
            "H": ae.shape[height_dim],
            "height": ae.shape[height_dim],
            "T": frame_count,
            "batch_count": ae.shape[batch_dim],
            "N": ae.shape[channel_dim],
            "channel_count": ae.shape[channel_dim],
        } | generate_dim_variables(ae)

        if time_dim is not None:
            F_idx = getIndexTensorAlongDim(ae, time_dim)
            variables.update({"frame_idx": F_idx, "frame": F_idx, "frame_count": frame_count})

        # Add all dynamic inputs
        for k, v in V.items():
            if v is not None:
                v_tensor = v["samples"]
                norm_v = normalize_to_common_shape(ae, v_tensor, mode=length_mismatch)[1]
                variables[k] = norm_v

        for k, v in F.items():
            variables[k] = v if v is not None else 0.0

        visitor = UnifiedMathVisitor(variables, ae.shape)
        result_t = as_tensor(visitor.visit(tree), ae.shape)

        result_latent = a_c.copy()
        if stacked and orig_split_sizes is not None:
            from comfy.nested_tensor import NestedTensor
            # Restore original split sizes
            try:
                result_latent["samples"] = NestedTensor(torch.split(result_t, orig_split_sizes, dim=0))
            except Exception:
                # Fallback if split fails (e.g. result shape changed)
                result_latent["samples"] = result_t
        else:
            result_latent["samples"] = result_t

        return (result_latent,)
