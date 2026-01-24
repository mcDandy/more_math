import torch
from .helper_functions import generate_dim_variables, parse_expr, getIndexTensorAlongDim, as_tensor, prepare_inputs, normalize_to_common_shape
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
                    options=["error", "error", "pad"],
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
        # Extract tensors and pooled outputs
        tensor = {}
        pooled_output = {}

        # Get shape reference from V0 (assumed to exist and be valid conditioning)
        ref_cond = V.get("V0")
        ref_tensor_shape = ref_cond[0][0].shape if ref_cond else None
        ref_pooled_shape = ref_cond[0][1].get("pooled_output").shape if ref_cond and "pooled_output" in ref_cond[0][1] else None

        for key, conditioning in V.items():
            # Standard Conditioning is list of [tensor, dict]
            if isinstance(conditioning, list) and len(conditioning) > 0 and isinstance(conditioning[0], (list, tuple)):
                tensor[key] = conditioning[0][0]
                pooled_output[key] = conditioning[0][1].get("pooled_output", torch.zeros(ref_pooled_shape) if ref_pooled_shape is not None else None)
            else:
                # Fallback to zeros if structure is unknown or empty
                tensor[key] = torch.zeros(ref_tensor_shape) if ref_tensor_shape is not None else None
                pooled_output[key] = torch.zeros(ref_pooled_shape) if ref_pooled_shape is not None else None

        # Normalize shapes
        new_values = normalize_to_common_shape(*tensor.values(), mode=length_mismatch)
        tensor.update(zip(tensor.keys(), new_values))

        if any(p is not None for p in pooled_output.values()):
             # Filter out Nones for normalization if any
             valid_pooled = {k:v for k,v in pooled_output.items() if v is not None}
             if valid_pooled:
                 new_p_values = normalize_to_common_shape(*valid_pooled.values(), mode=length_mismatch)
                 pooled_output.update(zip(valid_pooled.keys(), new_p_values))

        ac,bc,cc,dc = prepare_inputs(V.get("V0"),V.get("V1"),V.get("V2"),V.get("V3"))

        a = ac[0][0]
        b = bc[0][0]
        c = cc[0][0]
        d = dc[0][0]

        # variables for Main Tensor (Expression)
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

        # Execute Expression (Main Tensor)
        tree = parse_expr(Expression)
        visitor = UnifiedMathVisitor(variables, a.shape)
        rtensor = visitor.visit(tree)
        rtensor = as_tensor(rtensor, a.shape)


        # variables for Pooled Output (Expression_pi)
        a_p = ac[0][1].get("pooled_output", torch.zeros(ref_pooled_shape) if ref_pooled_shape is not None else torch.tensor([]))
        b_p = bc[0][1].get("pooled_output", torch.zeros_like(a_p))
        c_p = cc[0][1].get("pooled_output", torch.zeros_like(a_p))
        d_p = dc[0][1].get("pooled_output", torch.zeros_like(a_p))

        variables = {
            "a": a_p, "b": b_p, "c": c_p, "d": d_p,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "B": getIndexTensorAlongDim(a_p, 0),
            "batch": getIndexTensorAlongDim(a_p, 0),
            "T": a_p.shape[0],
            "batch_count": a_p.shape[0],
        } | generate_dim_variables(a_p) | pooled_output

        # Execute Expression_pi (Pooled Output)
        tree = parse_expr(Expression_pi)
        visitor = UnifiedMathVisitor(variables, a_p.shape)
        rpooled = visitor.visit(tree)
        rpooled = as_tensor(rpooled, a_p.shape)

        # Clone result structure
        import copy
        vl = copy.deepcopy(V["V0"])
        vl[0][0] = rtensor
        vl[0][1]["pooled_output"] = rpooled
        return (vl,)
