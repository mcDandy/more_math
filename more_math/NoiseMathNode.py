from .helper_functions import generate_dim_variables, as_tensor, parse_expr, getIndexTensorAlongDim, make_zero_like, get_v_variable, get_f_variable
from comfy_api.latest import io
import torch
from .Parser.MathExprParser import MathExprParser,InputStream,CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
import re
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from .Stack import MrmthStack

class NoiseMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on noise generators.
    inputs:
        a, b, c, d:
            Noise generators.
        w, x, y, z:
            Floats.
        Noise expression:
            The expression to apply on those noise generators.
            Note that variables X, Y, W, H, C, batch, batch_count, input_latent refer to input_latent.
    outputs:
        NOISE:
            The resulting noise generator.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_NoiseMathNode",
            display_name="Noise math",
            category="More math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Noise.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Noise", default="a*(1-w)+b*w"),
                MrmthStack.Input(id="stack", tooltip="Access stack between nodes",optional=True)
            ],
            outputs=[
                io.Noise.Output(),
                MrmthStack.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Noise, V, F,stack={}):
        input_stream = InputStream(Noise)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()

        # Support aliases
        aliases_smp = {"a": "V0", "b": "V1", "c": "V2", "d": "V3"}
        aliases_flt = {"w": "F0", "x": "F1", "y": "F2", "z": "F3"}

        needed = []
        needed1 = []
        for token in filter(lambda t: t.type == MathExprParser.VARIABLE, stream.tokens):
            var_name = token.text
            if re.match(r"[VF][0-9]+", var_name):
                needed.append(var_name)
            elif var_name in aliases_smp:
                needed.append(aliases_smp[var_name])
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
    def execute(cls, Noise, V,F,stack={}):
        stack = stack.deepcopy() if stack is not None else {}
        return (NoiseExecutor(V,F, Noise,stack),)


class NoiseExecutor:
    def __init__(self, V,F, expr,stack):
        self.V = V
        self.F = F
        self.tree = parse_expr(expr)
        self.stack = stack

    seed = -1

    def generate_noise(self, input_latent: torch.Tensor) -> torch.Tensor:
        samples = input_latent["samples"]

        vals = {v: (self.V[v].generate_noise(input_latent) if self.V[v] is not None else make_zero_like(samples)) for v in self.V}

        ndim = samples.ndim
        batch_dim = 0
        channel_dim = -3
        height_dim = -2
        width_dim = -1
        time_dim = None
        if ndim >= 5:
            time_dim = -4

        frame_count = samples.shape[time_dim] if time_dim is not None else samples.shape[batch_dim]

        B = getIndexTensorAlongDim(samples, batch_dim)
        W = getIndexTensorAlongDim(samples, width_dim)
        H = getIndexTensorAlongDim(samples, height_dim)
        C = getIndexTensorAlongDim(samples, channel_dim)

        variables = {
            "a": vals.get("V0") if "V0" in vals else make_zero_like(samples),
            "b": vals.get("V1") if "V1" in vals else make_zero_like(samples),
            "c": vals.get("V2") if "V2" in vals else make_zero_like(samples),
            "d": vals.get("V3") if "V3" in vals else make_zero_like(samples),
            "w": self.F.get("F0", 0.0),
            "x": self.F.get("F1", 0.0),
            "y": self.F.get("F2", 0.0),
            "z": self.F.get("F3", 0.0),
            "B": B, "batch": B,
            "X": W, "width": samples.shape[width_dim],
            "Y": H, "height": samples.shape[height_dim],
            "C": C, "channel": C,
            "W": samples.shape[width_dim], "H": samples.shape[height_dim], "I": samples,
            "T": frame_count, "N": samples.shape[channel_dim],
            "batch_count": samples.shape[batch_dim], "channel_count": samples.shape[channel_dim],
            "input_latent": samples,
        } | generate_dim_variables(samples) | vals | self.F

        v_stacked, v_cnt = get_v_variable(vals)
        if v_stacked is not None:
             variables["V"] = v_stacked
             variables["Vcnt"] = float(v_cnt)
             variables["V_count"] = float(v_cnt)

        f_stacked, f_cnt = get_f_variable(self.F)
        if f_stacked is not None:
             variables["F"] = f_stacked
             variables["Fcnt"] = float(f_cnt)
             variables["F_count"] = float(f_cnt)

        if time_dim is not None:
            F = getIndexTensorAlongDim(samples, time_dim)
            variables.update({"frame": F, "frame_count": frame_count})

        visitor = UnifiedMathVisitor(variables, samples.shape,samples.device,state_storage=self.stack)
        result = visitor.visit(self.tree)
        result = as_tensor(result, samples.shape)
        return result
