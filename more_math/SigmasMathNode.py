from .helper_functions import generate_dim_variables, parse_expr, getIndexTensorAlongDim, as_tensor, prepare_inputs, make_zero_like, normalize_to_common_shape
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
import re

class SigmasMathNode(io.ComfyNode):
    """
    Enables math expressions on Images with autogrow support.

    Inputs:
        I: Autogrow image inputs (I0, I1, ...)
        F: Autogrow float inputs (F0, F1, ...)
        Image: Expression
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_SigmasMathNode",
            category="More math",
            display_name="Sigmas math",
            inputs=[
                io.Autogrow.Input(id="I",template=io.Autogrow.TemplatePrefix(io.Sigmas.Input("input"), prefix="I", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Image", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on input images"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="tile",
                    tooltip="How to handle mismatched image batch sizes. broadcast: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                )
            ],
            outputs=[
                io.Sigmas.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Image, I, F, length_mismatch="tile"):

        input_stream = InputStream(Image)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()

        # Support aliases
        aliases_img = {"a": "I0", "b": "I1", "c": "I2", "d": "I3"}
        aliases_flt = {"w": "F0", "x": "F1", "y": "F2", "z": "F3"}

        needed = []
        needed1 = []
        for token in filter(lambda t: t.type == MathExprParser.VARIABLE, stream.tokens):
            var_name = token.text

            if re.match(r"[IF][0-9]+", var_name):
                needed.append(var_name)
            elif var_name in aliases_img:
                needed.append(aliases_img[var_name])
            elif var_name in aliases_flt:
                needed.append(aliases_flt[var_name])
        for v in needed:
            if v.begins_with("I") and not I[v]:
                needed1.append[v]
            elif not F[v]:
                needed1.append[v]
        return needed1

    @classmethod
    def execute(cls, I, F, Image, length_mismatch="tile"):
        # I and F are Autogrow.Type which is dict[str, Any]

        # Determine reference image for zero-initialization (fallback for a,b,c,d)
        ref_image = None
        for img in I.values():
            if img is not None:
                ref_image = img
                break

        if ref_image is None:
             raise ValueError("At least one image input is required.")

        # Extract base images for a,b,c,d
        a = I.get("I0")
        b = I.get("I1")
        c = I.get("I2")
        d = I.get("I3")

        if a is None:
            a = make_zero_like(ref_image)

        ae, be, ce, de = prepare_inputs(a, b, c, d)

        ae, be, ce, de = normalize_to_common_shape(ae, be, ce, de, mode=length_mismatch)

        if(length_mismatch == "error"):
            max_length = ae.shape[0]
            for name, tensor in I.items():
                if tensor is not None and tensor.shape[0] != max_length:
                    raise ValueError(f"Input '{name}' has shape {tensor.shape[0]}, expected {max_length} to match largest input.")

        variables = {
            "a": ae, "b": be, "c": ce, "d": de,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "X": getIndexTensorAlongDim(ae, 3),
            "W": ae.shape[2],
            "width": ae.shape[2],
        } | generate_dim_variables(ae)

        # Add all dynamic inputs
        for k, v in I.items():
            if v is not None:
                # Normalize all images in I to match ae.shape
                norm_v = normalize_to_common_shape(ae, v, mode=length_mismatch)[1]
                variables[k] = norm_v

        for k, v in F.items():
            variables[k] = v if v is not None else 0.0

        tree = parse_expr(Image);
        visitor = UnifiedMathVisitor(variables, ae.shape)
        result = visitor.visit(tree)
        result = as_tensor(result, ae.shape)
        return (result,)
