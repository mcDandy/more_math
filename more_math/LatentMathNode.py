from inspect import cleandoc
import comfy.nested_tensor
from comfy_api.latest import io
import torch
from .helper_functions import (
    generate_dim_variables,
    getIndexTensorAlongDim,
    parse_expr,
    eval_tensor_expr_with_tree,
    make_zero_like,
    as_tensor,
)
from .MathNodeBase import MathNodeBase


class LatentMathNode(MathNodeBase):
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
            ],
            outputs=[
                io.Latent.Output(),
            ],
        )

    # RETURN_NAMES = ("image_output_name",)
    tooltip = cleandoc(__doc__)

    # OUTPUT_NODE = False
    # OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node
    @classmethod
    def execute(cls, Latent, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:
        # Extract raw sample tensors (may be Tensor or NestedTensor)
        a_in = a["samples"]
        b_in = None if b is None else b["samples"]
        c_in = None if c is None else c["samples"]
        d_in = None if d is None else d["samples"]

        # parse expression once
        tree = parse_expr(Latent)

        def eval_single_tensor(a_t, b_t, c_t, d_t):
            ndim = a_t.ndim
            batch_dim = 0
            channel_dim = -3
            height_dim = -2
            width_dim = -1
            time_dim = None
            if ndim >= 5:
                time_dim = -4

            B = getIndexTensorAlongDim(a_t, batch_dim)
            C = getIndexTensorAlongDim(a_t, channel_dim)
            H = getIndexTensorAlongDim(a_t, height_dim)
            W = getIndexTensorAlongDim(a_t, width_dim)

            width_val = a_t.shape[width_dim]
            height_val = a_t.shape[height_dim]
            channel_count = a_t.shape[channel_dim]
            batch_count = a_t.shape[batch_dim]
            frame_count = a_t.shape[time_dim] if time_dim is not None else a_t.shape[batch_dim]

            variables = {
                "a": a_t,
                "b": b_t,
                "c": c_t,
                "d": d_t,
                "w": w,
                "x": x,
                "y": y,
                "z": z,
                "X": W,
                "Y": H,
                "B": B,
                "batch": B,
                "C": C,
                "channel": C,
                "W": width_val,
                "width": width_val,
                "H": height_val,
                "height": height_val,
                "T": frame_count,
                "batch_count": batch_count,
                "N": channel_count,
                "channel_count": channel_count,
            } | generate_dim_variables(a_t)

            if time_dim is not None:
                F = getIndexTensorAlongDim(a_t, time_dim)
                variables.update({"frame_idx": F, "frame": F, "frame_count": frame_count})

            return as_tensor(eval_tensor_expr_with_tree(tree, variables, a_t.shape), a_t.shape)

        if hasattr(a_in, "is_nested") and getattr(a_in, "is_nested"):
            a_list = a_in.unbind()
            sizes = [t.shape[0] for t in a_list]
            merged_a = torch.cat(a_list, dim=0)

            def merge_to_tensor(val, ref):
                if val is None:
                    return make_zero_like(ref)
                if hasattr(val, "is_nested") and getattr(val, "is_nested"):
                    lst = val.unbind()
                    return torch.cat(lst, dim=0)
                if isinstance(val, (list, tuple)):
                    return torch.cat(list(val), dim=0)
                if torch.is_tensor(val):
                    if val.shape == ref.shape:
                        return val
                    try:
                        if val.shape[0] in sizes and val.shape[1:] == a_list[0].shape[1:]:
                            return torch.cat([val for _ in a_list], dim=0)
                    except Exception:
                        pass
                    if val.shape[0] == sum(sizes):
                        return val
                return make_zero_like(ref)

            merged_b = merge_to_tensor(b_in, merged_a)
            merged_c = merge_to_tensor(c_in, merged_a)
            merged_d = merge_to_tensor(d_in, merged_a)
            merged_result = eval_single_tensor(merged_a, merged_b, merged_c, merged_d)

            split_results = list(merged_result.split(sizes, dim=0))
            out_samples = comfy.nested_tensor.NestedTensor(split_results)

            return ({"samples": out_samples},)

        def to_tensor(val, ref):
            if val is None:
                return make_zero_like(ref)
            if hasattr(val, "is_nested") and getattr(val, "is_nested"):
                lst = val.unbind()
            elif isinstance(val, (list, tuple)):
                lst = list(val)
            else:
                return val

            if len(lst) == 0:
                return make_zero_like(ref)
            if len(lst) == 1:
                return lst[0]
            try:
                cat = torch.cat(lst, dim=0)
                if cat.shape == ref.shape or (cat.shape[0] == ref.shape[0] and cat.shape[1:] == ref.shape[1:]):
                    return cat
            except Exception:
                pass
            try:
                stk = torch.stack(lst, dim=0)
                if stk.shape == ref.shape or (stk.shape[0] == ref.shape[0] and stk.shape[1:] == ref.shape[1:]):
                    return stk
            except Exception:
                pass
            return lst[0]

        b_single = to_tensor(b_in, a_in)
        c_single = to_tensor(c_in, a_in)
        d_single = to_tensor(d_in, a_in)

        result1 = eval_single_tensor(a_in, b_single, c_single, d_single)
        result = {"samples": result1}
        return (result,)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    # @classmethod
    # def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""
