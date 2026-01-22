import torch
from .helper_functions import generate_dim_variables, parse_expr, getIndexTensorAlongDim, as_tensor, prepare_inputs, normalize_to_common_shape
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

        if(length_mismatch == "error"):
            max_lengths = V.get("V0")["waveform"].shape
            for name, tensor in V.items():
                if tensor["waveform"] is not None and max_lengths!=tensor["waveform"].shape:
                    raise ValueError(f"Input '{name}' has shape {tensor['waveform'].shape}, expected {max_lengths} to match input.")

        waveforms={}
        sample_rates={}
        for key, audio in V.items():
            if audio is not None and isinstance(audio, dict) and "waveform" in audio:
                waveforms[key] = audio["waveform"]
                sample_rates[key+"sr"] = audio.get("sample_rate", 44100)
            else:
                waveforms[key] = torch.zeros(V["V0"]["waveform"].shape)
                sample_rates[key] = 44100
        sample_rate = sample_rates["V0sr"] if len(sample_rates) > 0 else 44100
        new_values = normalize_to_common_shape(*waveforms.values(), mode=length_mismatch)
        waveforms.update(zip(waveforms.keys(), new_values))
        a,b,c,d = prepare_inputs(V.get("V0"),V.get("V1"),V.get("V2"),V.get("V3"))
        a = a["waveform"]
        b = b["waveform"]
        c = c["waveform"]
        d = d["waveform"]
        variables = {
            "a": a, "b": b, "c": c, "d": d,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "B": getIndexTensorAlongDim(a, 0),
            "C": getIndexTensorAlongDim(a, 1),
            "channel": getIndexTensorAlongDim(a, 1),
            "S": getIndexTensorAlongDim(a, 2),
            "sample": getIndexTensorAlongDim(a, 2),
            "R": sample_rate,
            "sample_rate": sample_rate,
            "batch": getIndexTensorAlongDim(a, 0),
            "T": a.shape[0],
            "batch_count": a.shape[0],
        } | generate_dim_variables(a) | waveforms | sample_rates

        tree = parse_expr(Expression);
        visitor = UnifiedMathVisitor(variables, a.shape)
        result = visitor.visit(tree)
        result = as_tensor(result, a.shape)
        return ({"waveform":result,"sample_rate":sample_rate},)
