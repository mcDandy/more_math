from .helper_functions import generate_dim_variables, parse_expr, getIndexTensorAlongDim, as_tensor, normalize_to_common_shape, make_zero_like, get_v_variable, get_f_variable
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
import re
from .Stack import MrmthStack

class ImageMathNode(io.ComfyNode):
    """
    Enables math expressions on Images using Autogrow inputs.

    Inputs:
        V: Autogrow image inputs (V0, V1, ...)
        F: Autogrow float inputs (F0, F1, ...)
        Image: Expression to apply on input images
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_ImageMathNode",
            category="More math",
            display_name="Image math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Image.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Expression", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on input images"), # Changed ID to Expression to match AudioMathNode pattern, or keep Image? AudioMathNode used "Expression".
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="error",
                    tooltip="How to handle mismatched image batch sizes. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                ),
                MrmthStack.Input(id="stack", tooltip="Access stack between nodes",optional=True)
            ],
            outputs=[
                io.Image.Output(),
                MrmthStack.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Expression, V, F, length_mismatch="tile",stack=dict()):

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
    def execute(cls, V, F, Expression, length_mismatch="error",stack=dict()):
        # I and F are Autogrow.Type which is dict[str, Any]

        # Identify all present tensors and their keys
        tensor_keys = [k for k, v in V.items() if v is not None]
        if not tensor_keys:
             raise ValueError("At least one input is required.")

        tensors = [V[k] for k in tensor_keys]

        # Normalize all tensors together to find the common target shape
        normalized_tensors = normalize_to_common_shape(*tensors, mode=length_mismatch)
        V_norm = dict(zip(tensor_keys, normalized_tensors))

        # Use first normalized tensor to establish the reference shape
        ref_tensor = normalized_tensors[0]
        common_shape = ref_tensor.shape

        # Setup legacy variables a, b, c, d
        ae = V_norm.get("V0", make_zero_like(ref_tensor))
        be = V_norm.get("V1", make_zero_like(ae))
        ce = V_norm.get("V2", make_zero_like(ae))
        de = V_norm.get("V3", make_zero_like(ae))

        # Ensure legacy variables are normalized in case they were zero-initialized
        ae, be, ce, de = normalize_to_common_shape(ae, be, ce, de, mode=length_mismatch)

        if(length_mismatch == "error"):
            for name, tensor in V.items():
                if tensor is not None and tensor.shape[0] != common_shape[0]:
                    raise ValueError(f"Input '{name}' has shape {tensor.shape[0]}, expected {common_shape[0]} to match input.")

        variables = {
            "a": ae, "b": be, "c": ce, "d": de,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
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

        # Add all dynamic inputs
        variables.update(V_norm)

        v_stacked, v_cnt = get_v_variable(V_norm, length_mismatch=length_mismatch)
        if v_stacked is not None:
             variables["V"] = v_stacked
             variables["Vcnt"] = float(v_cnt)
             variables["V_count"] = float(v_cnt)

        f_stacked, f_cnt = get_f_variable(F)
        if f_stacked is not None:
             variables["F"] = f_stacked
             variables["Fcnt"] = float(f_cnt)
             variables["F_count"] = float(f_cnt)

        for k, val in F.items():
            variables[k] = val if val is not None else 0.0

        tree = parse_expr(Expression);
        visitor = UnifiedMathVisitor(variables, ae.shape,ae.device,state_storage=stack)
        result = visitor.visit(tree)
        result = as_tensor(result, ae.shape)
        return (result,stack)
