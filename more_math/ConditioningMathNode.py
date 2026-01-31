from unittest import result
import torch
from .helper_functions import generate_dim_variables, parse_expr, getIndexTensorAlongDim, as_tensor, normalize_to_common_shape, make_zero_like
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
import re
import copy

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
                io.String.Input(id="Expression",display_name="Tensor expr.", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on tensor part of conditioning"),
                io.String.Input(id="Expression_pi",display_name="pooled output expr.", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on pooled_input part of conditioning"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="error",
                    tooltip="How to handle mismatched image batch sizes. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                ),
                io.Int.Input(id="batching")
            ],
            outputs=[
                io.Conditioning.Output(is_output_list=True),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Expression,Expression_pi, V, F,batching, length_mismatch="tile"):

        input_stream = InputStream(Expression)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()

        input_stream = InputStream(Expression_pi)
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
    def execute(cls, V, F, Expression, Expression_pi,batching, length_mismatch="tile"):
        # Identify all present conditioning inputs
        tensor_keys = [k for k, v in V.items() if v is not None and isinstance(v, list) and len(v) > 0]
        if not tensor_keys:
             raise ValueError("At least one input is required.")

        # Extract tensors and pooled outputs
        tensors = {}
        pooled_outputs = {}
        ss = dict()
        for key in tensor_keys:
             conditioning = V[key]
             tensors[key] = conditioning[0][0]
             # pooled_output is optional in the dict

             pooled_outputs[key] = conditioning[0][1].get("pooled_output")

        # Normalize main tensors
        norm_tensors_batch = normalize_to_common_shape(*tensors.values(), mode=length_mismatch)
        V_norm_tensors = dict(zip(tensor_keys, norm_tensors_batch))

        ref_tensor = norm_tensors_batch[0]
        common_shape = ref_tensor.shape

        # Normalize pooled outputs (if they exist)
        valid_pooled_keys = [k for k, v in pooled_outputs.items() if v is not None]
        if valid_pooled_keys:
             norm_pooled_batch = normalize_to_common_shape(*[pooled_outputs[k] for k in valid_pooled_keys], mode=length_mismatch)
             V_norm_pooled = dict(zip(valid_pooled_keys, norm_pooled_batch))
             ref_pooled = norm_pooled_batch[0]
        else:
             V_norm_pooled = {}
             ref_pooled = torch.tensor([])

        # Setup legacy variables a, b, c, d (Main Tensor)
        a = V_norm_tensors.get("V0", make_zero_like(ref_tensor))
        b = V_norm_tensors.get("V1", make_zero_like(a))
        c = V_norm_tensors.get("V2", make_zero_like(a))
        d = V_norm_tensors.get("V3", make_zero_like(a))
        a, b, c, d = normalize_to_common_shape(a, b, c, d, mode=length_mismatch)

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
        } | generate_dim_variables(a) | V_norm_tensors

        for k, val in F.items():
            variables[k] = val if val is not None else 0.0

        # Execute Expression (Main Tensor)
        tree = parse_expr(Expression)
        visitor = UnifiedMathVisitor(variables, a.shape,a.device, state_storage=ss)
        rtensor = visitor.visit(tree)
        rtensor = as_tensor(rtensor, a.shape)


        # variables for Pooled Output (Expression_pi)
        a_p = V_norm_pooled.get("V0", make_zero_like(ref_pooled))
        b_p = V_norm_pooled.get("V1", make_zero_like(a_p))
        c_p = V_norm_pooled.get("V2", make_zero_like(a_p))
        d_p = V_norm_pooled.get("V3", make_zero_like(a_p))
        a_p, b_p, c_p, d_p = normalize_to_common_shape(a_p, b_p, c_p, d_p, mode=length_mismatch)

        variables_pi = {
            "a": a_p, "b": b_p, "c": c_p, "d": d_p,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "B": getIndexTensorAlongDim(a_p, 0) if a_p.numel() > 0 else torch.tensor([]),
            "batch": getIndexTensorAlongDim(a_p, 0) if a_p.numel() > 0 else torch.tensor([]),
            "T": a_p.shape[0] if a_p.numel() > 0 else 0,
            "batch_count": a_p.shape[0] if a_p.numel() > 0 else 0,
        } | generate_dim_variables(a_p) | V_norm_pooled

        for k, val in F.items():
            variables_pi[k] = val if val is not None else 0.0

        # Execute Expression_pi (Pooled Output)
        tree_pi = parse_expr(Expression_pi)
        visitor_pi = UnifiedMathVisitor(variables_pi, a_p.shape,a_p.device, state_storage=ss)
        rpooled_raw = visitor_pi.visit(tree_pi)
        rpooled = as_tensor(rpooled_raw, a_p.shape)


        if rtensor is None:
            rtensor = torch.zeros([1])
        if rpooled is None:
            rpooled = torch.zeros([1])

        # batching = size of each chunk -> use torch.split(tensor, batching, dim=0)
        if batching and batching > 0:
            rt_chunks = torch.split(rtensor, batching, dim=0)
            rp_chunks = torch.split(rpooled, batching, dim=0)
            res_list = []
            for i in range(max(len(rt_chunks), len(rp_chunks))):
                result_tensor = rt_chunks[i] if i < len(rt_chunks) else torch.zeros([1])
                result_pooled = rp_chunks[i] if i < len(rp_chunks) else torch.zeros([1])
                base = copy.deepcopy(V["V0"])
                base[0][0] = result_tensor
                if len(base[0]) == 1:
                    base[0].append({"pooled_output": result_pooled})
                else:
                    base[0][1]["pooled_output"] = result_pooled
                res_list.append(base)
        else:
            # Single output (no batching)
            base = copy.deepcopy(V["V0"])
            base[0][0] = rtensor
            if len(base[0]) == 1:
                base[0].append({"pooled_output": rpooled})
            else:
                base[0][1]["pooled_output"] = rpooled
            res_list = [base]

        return (res_list,)
