from inspect import cleandoc
import torch

from .helper_functions import comonLazy, eval_tensor_expr, generate_dim_variables, make_zero_like, as_tensor

from comfy_api.latest import io


from .MathNodeBase import MathNodeBase


class ConditioningMathNode(MathNodeBase):
    """
    Enables math operations on conditionings.

    Inputs:
        a, b, c, d: Conditioning inputs (b, c, d default to zero if not provided)
        w, x, y, z: Float variables for expressions
        Tensor: Expression for the tensor part (describes image composition)
        pooled_output: Expression for the pooled output (condensed representation)

    Outputs:
        CONDITIONING: Result of applying expressions to input conditionings
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ConditioningMathNode",
            display_name="Conditioning math",
            category="More math",
            inputs=[
                io.Conditioning.Input(id="a"),
                io.Conditioning.Input(id="b", optional=True, lazy=True),
                io.Conditioning.Input(id="c", optional=True, lazy=True),
                io.Conditioning.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Tensor", default="a*(1-w)+b*w", tooltip="Expression for tensor part (image composition)"),
                io.String.Input(
                    id="pooled_output", default="a*(1-w)+b*w", tooltip="Expression for pooled output (condensed representation)"
                ),
            ],
            outputs=[
                io.Conditioning.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Tensor, pooled_output, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0):
        tensor_needs = set(comonLazy(Tensor, a, b, c, d))
        pooled_needs = set(comonLazy(pooled_output, a, b, c, d))
        return list(tensor_needs.union(pooled_needs))

    @classmethod
    def execute(cls, Tensor, pooled_output, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        # Default missing conditionings to zero
        a, b, c, d = cls.prepare_inputs(a, b, c, d)

        # Extract tensors
        ta, tb, tc, td = a[0][0], b[0][0], c[0][0], d[0][0]

        # Evaluate tensor expression
        variables = {"a": ta, "b": tb, "c": tc, "d": td, "w": w, "x": x, "y": y, "z": z} | generate_dim_variables(ta)
        result_tensor = as_tensor(eval_tensor_expr(Tensor, variables, ta.shape), ta.shape)

        # Evaluate pooled_output expression if available
        pa = a[0][1].get("pooled_output")
        if pa is not None:
            pb = b[0][1].get("pooled_output")
            pc = c[0][1].get("pooled_output")
            pd = d[0][1].get("pooled_output")
            variables = {"a": pa, "b": pb, "c": pc, "d": pd, "w": w, "x": x, "y": y, "z": z} | generate_dim_variables(pa)
            result_pooled = as_tensor(eval_tensor_expr(pooled_output, variables, pa.shape), pa.shape)
        else:
            result_pooled = None

        return ([[result_tensor, {"pooled_output": result_pooled}]],)
