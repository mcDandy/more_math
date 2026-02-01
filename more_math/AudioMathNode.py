from .helper_functions import (
    generate_dim_variables,
    parse_expr,
    getIndexTensorAlongDim,
    as_tensor,
    normalize_to_common_shape,
    make_zero_like,
    get_v_variable
)
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
import re

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
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Audio.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Expression", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on input audio"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="error",
                    tooltip="How to handle mismatched image batch sizes. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                )
            ],
            outputs=[
                io.Audio.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Expression, V, F, length_mismatch="tile"):

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
    def execute(cls, V, F, Expression, length_mismatch="tile"):
        # Identify all present audio inputs and their keys
        tensor_keys = [k for k, v in V.items() if v is not None and isinstance(v, dict) and "waveform" in v]
        if not tensor_keys:
             raise ValueError("At least one audio input is required.")

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

        for k, val in F.items():
            variables[k] = val if val is not None else 0.0

        tree = parse_expr(Expression);
        visitor = UnifiedMathVisitor(variables, a_w.shape,a_w.device)
        result = visitor.visit(tree)
        result = as_tensor(result, a_w.shape)
        return ({"waveform":result,"sample_rate":sample_rate},)
