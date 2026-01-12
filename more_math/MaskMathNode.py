from .helper_functions import generate_dim_variables, getIndexTensorAlongDim, eval_tensor_expr, as_tensor,commonLazy

from comfy_api.latest import io


class MaskMathNode(io.ComfyNode):
    """
    Enables math expressions on Images.

    Inputs:
        a, b, c, d: Mask inputs (b, c, d default to zero if not provided)
        w, x, y, z: Float variables for expressions
        mask: Expression to apply on input mask

    Outputs:
        MASK: Result of applying expression to input masks
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_MaskMathNode",
            category="More math",
            display_name="Mask math",
            inputs=[
                io.Mask.Input(id="a"),
                io.Mask.Input(id="b", optional=True, lazy=True),
                io.Mask.Input(id="c", optional=True, lazy=True),
                io.Mask.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Mask", default="a*(1-w)+b*w", tooltip="Expression to apply on input images"),
            ],
            outputs=[
                io.Mask.Output(),
            ],
        )
    @classmethod
    def check_lazy_status(cls, Mask, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0):
        return commonLazy(Mask, a, b, c, d, w, x, y, z)
    @classmethod
    def execute(cls, Mask, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        a, b, c, d = cls.prepare_inputs(a, b, c, d)

        variables = {
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            "w": w,
            "x": x,
            "y": y,
            "z": z,
            "X": getIndexTensorAlongDim(a, 2),
            "Y": getIndexTensorAlongDim(a, 1),
            "B": getIndexTensorAlongDim(a, 0),
            "batch": getIndexTensorAlongDim(a, 0),
            "W": a.shape[2],
            "width": a.shape[2],
            "H": a.shape[1],
            "height": a.shape[1],
            "T": a.shape[0],
            "batch_count": a.shape[0],
        } | generate_dim_variables(a)

        result = eval_tensor_expr(Mask, variables, a.shape)

        return (as_tensor(result, a.shape),)
