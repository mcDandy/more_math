from ..helper_functions import generate_dim_variables,parse_expr, getIndexTensorAlongDim, as_tensor, commonLazy, normalize_to_common_shape,prepare_inputs
from ..Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io




class MaskMathNodeOLD(io.ComfyNode):
    """
    Enables math expressions on Masks.

    Inputs:
        a, b, c, d: Mask inputs (b, c, d default to zero if not provided)
        w, x, y, z: Float variables for expressions
        Mask: Expression to apply on input masks

    Outputs:
        MASK: Result of applying expression to input masks
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_MaskMathNode",
            display_name="Mask math",
            is_deprecated=True,
            inputs=[
                io.Mask.Input(id="a"),
                io.Mask.Input(id="b", optional=True, lazy=True),
                io.Mask.Input(id="c", optional=True, lazy=True),
                io.Mask.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Mask", default="a*(1-w)+b*w", tooltip="Expression to apply on input masks"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["error", "error", "pad"],
                    default="error",
                    tooltip="How to handle mismatched mask batch sizes. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                )
            ],
            outputs=[
                io.Mask.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Mask, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0, length_mismatch="tile"):
        return commonLazy(Mask, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, Mask, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0, length_mismatch="tile"):
        a, b, c, d = prepare_inputs(a, b, c, d)

        if(length_mismatch == "error"):
            max_length = max(a.shape[0], b.shape[0], c.shape[0], d.shape[0])
            for tensor, name in zip([a, b, c, d], ["a", "b", "c", "d"]):
                if tensor.shape[0] != max_length:
                    raise ValueError(f"Input '{name}' has shape {tensor.shape[0]}, expected {max_length} to match largest input.")
        ae, be, ce, de = normalize_to_common_shape(a, b, c, d, mode=length_mismatch)

        variables = {
            "a": ae, "b": be, "c": ce, "d": de,
            "w": w, "x": x, "y": y, "z": z,
            "X": getIndexTensorAlongDim(ae, 2),
            "Y": getIndexTensorAlongDim(ae, 1),
            "B": getIndexTensorAlongDim(ae, 0),
            "batch": getIndexTensorAlongDim(ae, 0),
            "W": ae.shape[2],
            "width": ae.shape[2],
            "H": ae.shape[1],
            "height": ae.shape[1],
            "T": ae.shape[0],
            "batch_count": ae.shape[0],
        } | generate_dim_variables(ae)
        tree = parse_expr(Mask);
        visitor = UnifiedMathVisitor(variables, ae.shape)
        result = visitor.visit(tree)
        result = as_tensor(result, ae.shape)
        return (result,)
