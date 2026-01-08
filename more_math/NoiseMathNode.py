from inspect import cleandoc

import torch

from .helper_functions import (
    generate_dim_variables,
    getIndexTensorAlongDim,
    comonLazy,
    parse_expr,
    eval_tensor_expr_with_tree,
    make_zero_like,
    as_tensor,
)

from comfy_api.latest import io

import comfy.nested_tensor as _nested_tensor_module


class NoiseMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Latents.
    inputs:
        a, b, c, d:
            Noise generators, bound to variables with the same name. Defaults to zero latent if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Latent expression:
            String, describing expression to mix noise.

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
            node_id="mrmth_NoiseMathNode",
            category="More math",
            display_name="Noise math",
            inputs=[
                io.Noise.Input(id="a"),
                io.Noise.Input(id="b", optional=True, lazy=True),
                io.Noise.Input(id="c", optional=True, lazy=True),
                io.Noise.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Noise", default="a*(1-w)+b*w", tooltip="Expression to apply on input noise generators"),
            ],
            outputs=[
                io.Noise.Output(),
            ],
        )

    # RETURN_NAMES = ("image_output_name",)
    tooltip = cleandoc(__doc__)
    # OUTPUT_NODE = False
    # OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    CATEGORY = "More math"

    @classmethod
    def check_lazy_status(cls, Noise, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0):
        return comonLazy(Noise, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, Noise, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        return (NoiseExecutor(a, b, c, d, w, x, y, z, Noise),)

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


class NoiseExecutor:
    def __init__(self, a, b, c, d, w, x, y, z, Noise):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.expr = Noise
        self.tree = parse_expr(Noise)

    seed = -1

    def generate_noise(self, input_latent: torch.Tensor) -> torch.Tensor:
        samples = input_latent["samples"]

        a_val = self.a.generate_noise(input_latent) if self.a is not None else make_zero_like(samples)
        b_val = self.b.generate_noise(input_latent) if self.b is not None else make_zero_like(samples)
        c_val = self.c.generate_noise(input_latent) if self.c is not None else make_zero_like(samples)
        d_val = self.d.generate_noise(input_latent) if self.d is not None else make_zero_like(samples)

        # helper to convert a returned value into a list matching ref_list
        def to_list(val, ref_list):
            if val is None:
                return [make_zero_like(r) for r in ref_list]
            # If val is a NestedTensor-like, return underlying list
            if hasattr(val, "is_nested") and getattr(val, "is_nested"):
                return val.unbind()
            if isinstance(val, list) or isinstance(val, tuple):
                return list(val)
            # If val is a single tensor that encodes multiple subtensors along batch dim,
            # try to split it into pieces that match ref_list batch sizes.
            if torch.is_tensor(val):
                try:
                    sizes = [r.shape[0] for r in ref_list]
                    if val.shape[0] == sum(sizes):
                        return list(val.split(sizes, dim=0))
                except Exception:
                    pass
            # single tensor broadcast
            return [val for _ in ref_list]

        # nested case: merge subtensors, evaluate once, split back
        if hasattr(samples, "is_nested") and getattr(samples, "is_nested"):
            sample_list = samples.unbind()
            sizes = [t.shape[0] for t in sample_list]
            merged_samples = torch.cat(sample_list, dim=0)

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
                    if val.shape[0] == sum(sizes):
                        return val
                    # if val has per-subtensor batches, try to split and cat
                    try:
                        if val.shape[0] == len(sample_list):
                            return torch.cat(
                                [val[i].unsqueeze(0).expand(sample_list[i].shape[0], *val.shape[1:]) for i in range(len(sample_list))],
                                dim=0,
                            )
                    except Exception:
                        pass
                return make_zero_like(ref)

            merged_a = merge_to_tensor(a_val, merged_samples)
            merged_b = merge_to_tensor(b_val, merged_samples)
            merged_c = merge_to_tensor(c_val, merged_samples)
            merged_d = merge_to_tensor(d_val, merged_samples)

        else:
            merged_samples = samples
            merged_a = a_val
            merged_b = b_val
            merged_c = c_val
            merged_d = d_val

        # evaluate once
        ndim = merged_samples.ndim
        batch_dim = 0
        channel_dim = -3
        height_dim = -2
        width_dim = -1
        time_dim = None
        if ndim >= 5:
            time_dim = -4

        frame_count = merged_samples.shape[time_dim] if time_dim is not None else merged_samples.shape[batch_dim]

        B = getIndexTensorAlongDim(merged_samples, batch_dim)
        W = getIndexTensorAlongDim(merged_samples, width_dim)
        H = getIndexTensorAlongDim(merged_samples, height_dim)
        C = getIndexTensorAlongDim(merged_samples, channel_dim)
        variables = {
            "a": merged_a,
            "b": merged_b,
            "c": merged_c,
            "d": merged_d,
            "w": self.w,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "B": B,
            "X": W,
            "Y": H,
            "C": C,
            "W": merged_samples.shape[width_dim],
            "H": merged_samples.shape[height_dim],
            "I": merged_samples,
            "T": frame_count,
            "N": merged_samples.shape[channel_dim],
            "batch": B,
            "width": merged_samples.shape[width_dim],
            "height": merged_samples.shape[height_dim],
            "channel": C,
            "batch_count": merged_samples.shape[0],
            "channel_count": merged_samples.shape[1],
            "input_latent": merged_samples,
        } | generate_dim_variables(merged_samples)
        if time_dim is not None:
            F = getIndexTensorAlongDim(merged_samples, time_dim)
            variables.update({"frame": F, "frame_count": frame_count})

        merged_result = as_tensor(eval_tensor_expr_with_tree(self.tree, variables, variables["a"].shape), variables["a"].shape)

        if hasattr(samples, "is_nested") and getattr(samples, "is_nested"):
            split_results = list(merged_result.split(sizes, dim=0))
            return _nested_tensor_module.NestedTensor(split_results)

        return merged_result
