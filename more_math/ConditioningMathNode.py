import torch
from .helper_functions import generate_dim_variables, parse_expr, getIndexTensorAlongDim, as_tensor, prepare_inputs, make_zero_like, normalize_to_common_shape
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
import re

class ConditioningMathNode(io.ComfyNode):
    """
    Enables math expressions on Audio.

    Inputs:
        I: Autogrow image inputs (I0, I1, ...)
        F: Autogrow float inputs (F0, F1, ...)
        Image: Expression
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_ConditioningMathNode",
            category="More math",
            display_name="Conditioning math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Conditioning.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Expression", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on tensor part of conditioning"),
                io.String.Input(id="Expression_pi", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on pooled_input part of conditioning"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="error",
                    tooltip="How to handle mismatched image batch sizes. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                )
            ],
            outputs=[
                io.Conditioning.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Expression,Expression_pi, V, F, length_mismatch="tile"):

        input_stream = InputStream(Expression)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()

        input_stream = InputStream(Expression)
        lexer = MathExprLexer(input_stream)
        stream1 = CommonTokenStream(lexer)
        stream1.fill()

        # Support aliases
        aliases_img = {"a": "V0", "b": "V1", "c": "V2", "d": "V3"}
        aliases_flt = {"w": "F0", "x": "F1", "y": "F2", "z": "F3"}

        needed = set()
        needed1 = set()
        for token in filter(lambda t: t.type == MathExprParser.VARIABLE, stream.tokens + stream1.tokens):
            var_name = token.text

            if re.match(r"[VF][0-9]+", var_name):
                needed.add(var_name)
            elif var_name in aliases_img:
                needed.add(aliases_img[var_name])
            elif var_name in aliases_flt:
                needed.add(aliases_flt[var_name])
        for v in needed:
            if v.startswith("V"):
                if v not in V or V[v] is None:
                    needed1.add(v)
            elif v.startswith("F"):
                if v not in F or F[v] is None:
                    needed1.add(v)
        return needed1

    @classmethod
    def execute(cls, V, F, Expression, Expression_pi, length_mismatch="tile"):
        dir(V["V0"])
        print(V["V0"])
        if(length_mismatch == "error"):
            max_lengths = V.get("V0")[0][0].shape
            for name, tensor in V.items():
                if tensor[0][0] is not None and max_lengths!=tensor[0][0].shape:
                    raise ValueError(f"Input '{name}' has shape {tensor[0][0].shape}, expected {max_lengths} to match input.")
            max_lengths = V.get("V0")[0][1]["pooled_output"].shape
            for name, tensor in V.items():
                if tensor[0][1]["pooled_output"] is not None and max_lengths!=tensor[0][1]["pooled_output"].shape:
                    raise ValueError(f"Input '{name}' has shape {tensor[0][1]["pooled_output"].shape}, expected {max_lengths} to match input.")

        tensor={}
        pooled_output={}
        for key, conditioning in V.items():
            if conditioning is not None and isinstance(conditioning, dict) and "waveform" in conditioning:
                tensor[key] = conditioning[0][0]
                pooled_output[key] = conditioning[0][1]["pooled_output"]
            else:
                tensor[key] = torch.zeros_like(V.get("V0")[0][0])
                pooled_output[key] = torch.zeros_like(V.get("V0")[0][1]["pooled_output"])
        new_values = normalize_to_common_shape(*tensor.values(), mode=length_mismatch)
        tensor.update(zip(tensor.keys(), new_values))
        new_values = normalize_to_common_shape(*pooled_output.values(), mode=length_mismatch)
        tensor.update(zip(pooled_output.keys(), new_values))
        ac,bc,cc,dc = prepare_inputs(V.get("V0"),V.get("V1"),V.get("V2"),V.get("V3"))

        a = ac[0][0]
        b = bc[0][0]
        c = cc[0][0]
        d = dc[0][0]
        variables = {
            "a": a, "b": b, "c": c, "d": d,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "B": getIndexTensorAlongDim(a, 0),
            "batch": getIndexTensorAlongDim(a, 0),
            "T": a.shape[0],
            "batch_count": a.shape[0],
        } | generate_dim_variables(a) | tensor

        tree = parse_expr(Expression);
        visitor = UnifiedMathVisitor(variables, a.shape)
        rtensor = visitor.visit(tree)
        rtensor = as_tensor(rtensor, a.shape)


        a = ac[0][1]["pooled_output"]
        b = bc[0][1]["pooled_output"]
        c = cc[0][1]["pooled_output"]
        d = dc[0][1]["pooled_output"]
        variables = {
            "a": a, "b": b, "c": c, "d": d,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "B": getIndexTensorAlongDim(a, 0),
            "batch": getIndexTensorAlongDim(a, 0),
            "T": a.shape[0],
            "batch_count": a.shape[0],
        } | generate_dim_variables(a) | pooled_output

        tree = parse_expr(Expression);
        visitor = UnifiedMathVisitor(variables, a.shape)
        rpooled = visitor.visit(tree)
        rpooled = as_tensor(rpooled, a.shape)
        vl = V["V0"]
        vl[0][0] = rtensor
        vl[0][1]["pooled_output"] = rpooled
        return (vl,)
