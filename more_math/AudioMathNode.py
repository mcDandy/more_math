from .helper_functions import (
    generate_dim_variables,
    parse_expr,
    getIndexTensorAlongDim,
    as_tensor,
    normalize_to_common_shape,
    make_zero_like,
    get_v_variable,
    get_f_variable
)
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
import re
import torch
from .Stack import MrmthStack
import copy

class AudioMathNode(io.ComfyNode):
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
            node_id="mrmth_ag_AudioMathNode",
            category="More math",
            display_name="Audio math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Audio.Input("values", optional=True), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Expression", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on input audio"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["do nothing","error","tile", "pad"],
                    display_name="on size mismatch",
                    default="error",
                    tooltip="How to handle mismatched image batch sizes. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                ),
                io.Int.Input(id="batching", default=0),
                MrmthStack.Input(id="stack", tooltip="Access stack between nodes",optional=True)
            ],
            outputs=[
                io.Audio.Output(is_output_list=True),
                MrmthStack.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Expression, V, F, length_mismatch="tile",batching=0,stack={}):

        input_stream = InputStream(Expression)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)

        try:
            tree = parser.start()
        except:
            # Fallback to simple token scanning if parse fails
            return cls._fallback_lazy_check(Expression, V, F)

        # Support aliases
        aliases = {"a": "V0", "b": "V1", "c": "V2", "d": "V3",
                   "w": "F0", "x": "F1", "y": "F2", "z": "F3"}

        assigned_vars = set()
        needed_vars = set()

        # Process all top-level statements
        for child in tree.children:
            if not hasattr(child, 'getRuleIndex'):
                continue

            rule_name = parser.ruleNames[child.getRuleIndex()] if child.getRuleIndex() < len(parser.ruleNames) else None

            # Process function definitions: scan for reads but ignore writes
            if rule_name == 'funcDef':
                func_params = set()
                if child.paramList():
                    for param in child.paramList().VARIABLE():
                        func_params.add(param.getText())

                cls._collect_reads_only(child, needed_vars, assigned_vars, func_params)

            # Top-level assignments
            elif rule_name == 'varDef':
                var_name = child.VARIABLE().getText()
                cls._collect_vars_from_node(child, needed_vars, assigned_vars, set())
                assigned_vars.add(var_name)

            # Track other top-level statements
            else:
                cls._collect_vars_from_node(child, needed_vars, assigned_vars, set())

        # Normalize variable names through aliases
        needed = set()
        for var in needed_vars:
            norm = aliases.get(var, var)
            if var == "V":
                needed.add(V.Keys())
            if var == "F":
                needed.add(F.Keys())
            if re.match(r"[VF][0-9]+", norm):
                needed.add(norm)

        return needed

    @classmethod
    def _collect_reads_only(cls, node, needed_vars, assigned_vars, shadowed_vars):
        if node is None:
            return

        node_type = type(node).__name__

        if node_type == 'VariableExpContext':
            var_name = node.VARIABLE().getText()
            if var_name in shadowed_vars:
                return
            if var_name not in assigned_vars:
                needed_vars.add(var_name)
            return

        if node_type == 'FunctionDefContext':
            return

        if node_type == 'VarDefContext':
            for expr in node.expr():
                cls._collect_reads_only(expr, needed_vars, assigned_vars, shadowed_vars)
            return

        for i in range(node.getChildCount()):
            cls._collect_reads_only(node.getChild(i), needed_vars, assigned_vars, shadowed_vars)

    @classmethod
    def _collect_vars_from_node(cls, node, needed_vars, assigned_vars, shadowed_vars):
        """Recursively collect variable reads from an AST node"""
        if node is None:
            return

        node_type = type(node).__name__

        # Found a variable read
        if node_type == 'VariableExpContext':
            var_name = node.VARIABLE().getText()
            # Skip if shadowed
            if var_name in shadowed_vars:
                return
            if var_name not in assigned_vars:
                needed_vars.add(var_name)
            return

        # Skip
        if node_type == 'FunctionDefContext':
            return

        # Recursively visit children
        for i in range(node.getChildCount()):
            cls._collect_vars_from_node(node.getChild(i), needed_vars, assigned_vars, shadowed_vars)

    @classmethod
    def execute(cls, V, F, Expression, length_mismatch="tile",batching=0,stack={}):
        # Identify all present audio inputs and their keys
        tensor_keys = [k for k, v in V.items() if v is not None and isinstance(v, dict) and "waveform" in v]
        if not tensor_keys:
             raise ValueError("At least one audio input is required.")
        stack = copy.deepcopy(stack) if stack is not None else {}
        waveforms = {k: V[k]["waveform"] for k in tensor_keys}
        sample_rates = {k + "sr": V[k].get("sample_rate", 44100) for k in tensor_keys}

        # Normalize all waveforms together
        normalized_waveforms = normalize_to_common_shape(*waveforms.values(), mode=length_mismatch)
        V_norm_waveforms = dict(zip(tensor_keys, normalized_waveforms))

        ref_waveform = normalized_waveforms[0]
        common_shape = ref_waveform.shape
        sample_rate = V[tensor_keys[0]].get("sample_rate", 44100)

        if(length_mismatch == "error"):
            for name in tensor_keys:
                if waveforms[name].shape != common_shape:
                     raise ValueError(f"Input '{name}' has shape ({waveforms[name].shape[0]}, {waveforms[name].shape[2]}), expected ({common_shape[0]}, {common_shape[2]}) to match input.")

        # Setup legacy variables a, b, c, d
        a_w = V_norm_waveforms.get("V0", make_zero_like(ref_waveform))
        b_w = V_norm_waveforms.get("V1", make_zero_like(a_w))
        c_w = V_norm_waveforms.get("V2", make_zero_like(a_w))
        d_w = V_norm_waveforms.get("V3", make_zero_like(a_w))

        # Ensure legacy are normalized
        a_w, b_w, c_w, d_w = normalize_to_common_shape(a_w, b_w, c_w, d_w, mode=length_mismatch)

        variables = {
            "a": a_w, "b": b_w, "c": c_w, "d": d_w,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "B": getIndexTensorAlongDim(a_w, 0),
            "C": getIndexTensorAlongDim(a_w, 1),
            "channel": getIndexTensorAlongDim(a_w, 1),
            "S": getIndexTensorAlongDim(a_w, 2),
            "sample": getIndexTensorAlongDim(a_w, 2),
            "R": sample_rate,
            "sample_rate": sample_rate,
            "batch": getIndexTensorAlongDim(a_w, 0),
            "T": a_w.shape[0],
            "batch_count": a_w.shape[0],
        } | generate_dim_variables(a_w) | V_norm_waveforms | sample_rates

        v_stacked, v_cnt = get_v_variable(V_norm_waveforms, length_mismatch=length_mismatch)
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
        visitor = UnifiedMathVisitor(variables, a_w.shape,a_w.device,state_storage=stack)
        result = visitor.visit(tree)
        result = as_tensor(result, a_w.shape)

        if batching and batching > 0:
            res = torch.split(result, batching, dim=0)
            res_list = []
            for result_chunk in res:
                res_list.append({"waveform": result_chunk, "sample_rate": sample_rate})
            return (res_list, stack)
        else:
            return ([{"waveform": result, "sample_rate": sample_rate}], stack)
