from .helper_functions import generate_dim_variables, parse_expr, getIndexTensorAlongDim, as_tensor, prepare_inputs, commonLazy, normalize_to_common_shape
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io


class ImageMathNode(io.ComfyNode):
    """
    Enables math expressions on Images.

    Inputs:
        a, b, c, d: Image inputs (b, c, d default to zero if not provided)
        w, x, y, z: Float variables for expressions
        Image: Expression to apply on input images

    Outputs:
        IMAGE: Result of applying expression to input images
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ImageMathNode",
            category="More math",
            display_name="Image math",
            inputs=[
                io.Image.Input(id="a"),
                io.Image.Input(id="b", optional=True, lazy=True),
                io.Image.Input(id="c", optional=True, lazy=True),
                io.Image.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Image", default="a*(1-w)+b*w", tooltip="Expression to apply on input images"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="tile",
                    tooltip="How to handle mismatched image batch sizes. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                )
            ],
            outputs=[
                io.Image.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Image, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0, length_mismatch="tile"):
        return commonLazy(Image, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, Image, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0, length_mismatch="tile"):
        ae, be, ce, de = prepare_inputs(a, b, c, d)
        print(f"DEBUG: shapes {ae.shape[0]}, {be.shape[0]}, {ce.shape[0]}, {de.shape[0]}")

        if(length_mismatch == "error"):
            max_length = max(ae.shape[0], be.shape[0], ce.shape[0], de.shape[0])
            for tensor, name in zip([ae, be, ce, de], ["a", "b", "c", "d"]):
                if tensor.shape[0] != max_length:
                    raise ValueError(f"Input '{name}' has shape {tensor.shape[0]}, expected {max_length} to match largest input.")
        ae, be, ce, de = normalize_to_common_shape(ae, be, ce, de, mode=length_mismatch)

        variables = {
            "a": ae, "b": be, "c": ce, "d": de,
            "w": w, "x": x, "y": y, "z": z,
            "X": getIndexTensorAlongDim(ae, 3),
            "Y": getIndexTensorAlongDim(ae, 2),
            "B": getIndexTensorAlongDim(ae, 0),
            "batch": getIndexTensorAlongDim(ae, 0),
            "C": getIndexTensorAlongDim(ae, 1),
            "channel": getIndexTensorAlongDim(ae, 1),
            "W": ae.shape[2],
            "width": ae.shape[2],
            "H": ae.shape[1],
            "height": ae.shape[1],
            "T": ae.shape[0],
            "batch_count": ae.shape[0],
            "N": ae.shape[3],
            "channel_count": ae.shape[3],
        } | generate_dim_variables(ae)
        tree = parse_expr(Image);
        visitor = UnifiedMathVisitor(variables, ae.shape)
        result = visitor.visit(tree)
        result = as_tensor(result, ae.shape)
        return (result,)
