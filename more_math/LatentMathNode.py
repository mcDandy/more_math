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
    def check_lazy_status(cls, Latent, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0, length_mismatch="tile"):
        return commonLazy(Latent, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, Latent, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0, length_mismatch="tile") -> io.NodeOutput:
        # Identify if any input is a NestedTensor and track original sizes for restoration
        stacked = False
        orig_split_sizes = None

        for item in [a, b, c, d]:
            if item is not None:
                samples = item.get("samples")
                if getattr(samples, "is_nested", False):
                    stacked = True
                    # Store original split sizes (batch dimension)
                    orig_split_sizes = [t.shape[0] for t in samples.tensors]
                    break

        if stacked:
            if a is not None and getattr(a.get("samples"), "is_nested", False):
                a = a.copy()
                a["samples"] = torch.cat(a["samples"].tensors, dim=0)
            if b is not None and getattr(b.get("samples"), "is_nested", False):
                b = b.copy()
                b["samples"] = torch.cat(b["samples"].tensors, dim=0)
            if c is not None and getattr(c.get("samples"), "is_nested", False):
                c = c.copy()
                c["samples"] = torch.cat(c["samples"].tensors, dim=0)
            if d is not None and getattr(d.get("samples"), "is_nested", False):
                d = d.copy()
                d["samples"] = torch.cat(d["samples"].tensors, dim=0)

        a_c, b_c, c_c, d_c = prepare_inputs(a, b, c, d)
        at,bt,ct,dt = a_c["samples"],b_c["samples"],c_c["samples"],d_c["samples"]
        if(length_mismatch == "error"):
            # Check only available tensors
            tensors_to_check = [t for t in [at, bt, ct, dt] if t is not None]
            max_length = max(t.shape[0] for t in tensors_to_check)
            for tensor, name in zip([at, bt, ct, dt], ["a", "b", "c", "d"]):
                if tensor is not None:
                    if tensor.shape[0] != max_length:
                        raise ValueError(f"Input '{name}' has shape {tensor.shape[0]}, expected {max_length} to match largest input.")
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
        result_t = as_tensor(visitor.visit(tree), ae.shape)

        result_latent = a_c.copy()
        if stacked and orig_split_sizes is not None:
            from comfy.nested_tensor import NestedTensor
            # Restore original split sizes
            result_latent["samples"] = NestedTensor(torch.split(result_t, orig_split_sizes, dim=0))
        else:
            result_latent["samples"] = result_t

        return (result_latent,)
