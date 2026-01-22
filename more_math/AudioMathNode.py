import torch
from .helper_functions import generate_dim_variables, parse_expr, getIndexTensorAlongDim, as_tensor, prepare_inputs, make_zero_like, normalize_to_common_shape
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
    def check_lazy_status(cls, Image, V, F, length_mismatch="tile"):

        input_stream = InputStream(Image)
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
        # I and F are Autogrow.Type which is dict[str, Any]

        # Determine reference image for zero-initialization (fallback for a,b,c,d)
        ref_image = None
        for img in V.values():
            if img is not None:
                ref_image = img
                break

        if ref_image is None:
             raise ValueError("At least one input is required.")

        aa = V.get("V0")
        ba = V.get("V1")
        ca = V.get("V2")
        da = V.get("V3")

        if aa is None:
            aa = make_zero_like(ref_image)

        ae, be, ce, de = prepare_inputs(aa, ba, ca, da)

        if(length_mismatch == "error"):
            max_lengths = a.shape
            for name, tensor in V.items():
                if tensor is not None and max_lengths==tensor.shape:
                    raise ValueError(f"Input '{name}' has shape {tensor.shape}, expected {max_lengths} to match input.")

        a, b, c, d = normalize_to_common_shape(ae["waweform"], be["waweform"], ce["waweform"], de, mode=length_mismatch)
        waweforms={}
        sample_rates={}
        for key, audio in V.items():
            if audio is not None and isinstance(audio, dict) and "waveform" in audio:
                waweforms[key] = audio["waveform"]
                sample_rates[key] = audio.get("sample_rate", 44100)
            else:
                waweforms[key] = torch.zeros(V["V0"]["waveform"].shape)
                sample_rates[key] = 44100
        sample_rate = sample_rates["V0"] if len(sample_rates) > 0 else 44100


        variables = {
            "a": a, "b": b, "c": c, "d": d,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "B": getIndexTensorAlongDim(ae, 0),
            "C": getIndexTensorAlongDim(ae, 1),
            "channel": getIndexTensorAlongDim(ae, 1),
            "S": getIndexTensorAlongDim(ae, 2),
            "sample": getIndexTensorAlongDim(ae, 2),
            "R": sample_rate,
            "sample_rate": sample_rate,
            "batch": getIndexTensorAlongDim(ae, 0),
            "T": ae.shape[0],
            "batch_count": ae.shape[0],
        } | generate_dim_variables(ae) | waweforms | sample_rates

        # Add all dynamic inputs
        for k, v in V.items():
            if v is not None:
                # Normalize all images in I to match ae.shape
                norm_v = normalize_to_common_shape(ae, v, mode=length_mismatch)[1]
                variables[k] = norm_v

        for k, v in F.items():
            variables[k] = v if v is not None else 0.0

        tree = parse_expr(Expression);
        visitor = UnifiedMathVisitor(variables, ae.shape)
        result = visitor.visit(tree)
        result = as_tensor(result, ae.shape)
        return (result,)
