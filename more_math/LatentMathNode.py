from inspect import cleandoc
from comfy_api.latest import io
from .helper_functions import (
    generate_dim_variables,
    getIndexTensorAlongDim,
    parse_expr,
    as_tensor,
    normalize_to_common_shape,
    prepare_inputs
)
from .helper_functions import commonLazy
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
import torch


class LatentMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Latents.
    inputs:
        a, b, c, d:
            Latent, bound to variables with the same name. Defaults to zero latent if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Latent expression:
            String, describing expression to aply to latents.

    outputs:
        LATENT:
            Returns a LATENT object that contains the result of the math expression applied to the input conditionings.
    """

    def __init__(self):
        pass

    @classmethod
    def define_schema(cls) -> io.Schema:
        """ """
        return io.Schema(
            node_id="mrmth_LatentMathNode",
            display_name="Latent math",
            category="More math",
            inputs=[
                io.Latent.Input(id="a"),
                io.Latent.Input(id="b", optional=True, lazy=True),
                io.Latent.Input(id="c", optional=True, lazy=True),
                io.Latent.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Latent", default="a*(1-w)+b*w", tooltip="Expression to apply on input latents"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="tile",
                    tooltip="How to handle mismatched latent batch sizes. broadcast: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                )
            ],
            outputs=[
                io.Latent.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Latent, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0, length_mismatch="tile"):
        return commonLazy(Latent, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, Latent, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0, length_mismatch="tile") -> io.NodeOutput:
        # TODO: NestedTensor
        stacked = (
            (a or {}).get("is_nested") or
            (b or {}).get("is_nested") or
            (c or {}).get("is_nested") or
            (d or {}).get("is_nested")
        )
        if stacked:
            if a is not None and a["is_nested"]:
                a = [torch.stack(i) for i in a]
            if b is not None and b["is_nested"]:
                b = [torch.stack(i) for i in b]
            if c is not None and c["is_nested"]:
                c = [torch.stack(i) for i in c]
            if d is not None and d["is_nested"]:
                d = [torch.stack(i) for i in d]


        a, b, c, d = prepare_inputs(a, b, c, d)
        at,bt,ct,dt = a["samples"],b["samples"],c["samples"],d["samples"]
        if(length_mismatch == "error"):
            max_length = max(at.shape, bt.shape, ct.shape, dt.shape)
            for tensor, name in zip([at, bt, ct, dt], ["a", "b", "c", "d"]):
                print(tensor.shape)
                if tensor.shape not in (1, max_length):
                    raise ValueError(f"Input '{name}' has length {tensor.shape[0]}, expected {max_length} to match largest input.")
        ae, be, ce, de = normalize_to_common_shape(at, bt, ct, dt, mode=length_mismatch)

        # parse expression once
        tree = parse_expr(Latent)

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
            "w": w, "x": x, "y": y, "z": z,
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
            F = getIndexTensorAlongDim(ae, time_dim)
            variables.update({"frame_idx": F, "frame": F, "frame_count": frame_count})

        visitor = UnifiedMathVisitor(variables, ae.shape)
        result = visitor.visit(tree)
        result_t = as_tensor(result, ae.shape)
        result = a
        result["samples"]=result_t
        if stacked:
            v = torch.split(result,1)
            result["is_nested"]=True
            result["samples"]=v
        return (result,)
