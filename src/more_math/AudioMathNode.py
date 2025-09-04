from inspect import cleandoc
import torch
from antlr4 import CommonTokenStream, InputStream
from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor
from .helper_functions import getIndexTensorAlongDim

from comfy_api.latest import ComfyExtension, io

class AudioMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on AUDIO tensors.
    inputs:
        a, b, c, d:
            AUDIO, bound to variables with the same name. Defaults to zero AUDIO if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Audio expression:
            String, describing expression to apply to audio tensors.

    outputs:
        AUDIO:
            Returns an AUDIO object that contains the result of the math expression applied to the input audio tensors.
    """
    def __init__(self):
        pass

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_AudioMathNode",
            category="More math",
            inputs=[
                io.Audio.Input(id="a", tooltip="Input audio tensor"),
                io.Audio.Input(id="b", optional=True, tooltip="Second input audio tensor"),
                io.Audio.Input(id="c", optional=True, tooltip="Third input audio tensor"),
                io.Audio.Input(id="d", optional=True, tooltip="Fourth input audio tensor"),
                io.Float.Input(id="w", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, force_input=True),
                io.String.Input(id="AudioExpr", default="a*(1-w)+b*w", tooltip="Expression to apply on input audio tensors"),
            ],
            outputs=[
                io.Audio.Output(),
            ],
        )

    @classmethod
    def execute(self,cls, a, AudioExpr, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
   

        bv = b if b else {'waveform':torch.zeros_like(a['waveform']),'sample_rate':a['sample_rate']}
        cv = c if c else {'waveform':torch.zeros_like(a['waveform']),'sample_rate':a['sample_rate']}
        dv = d if d else {'waveform':torch.zeros_like(a['waveform']),'sample_rate':a['sample_rate']}

        B = getIndexTensorAlongDim(a['waveform'], 0)
        C = getIndexTensorAlongDim(a['waveform'], 1)
        S = getIndexTensorAlongDim(a['waveform'], 2)
        R = torch.full_like(S, a['sample_rate'], dtype=torch.float32)
        T = torch.full_like(S, a['waveform'].shape[2], dtype=torch.float32)

        variables = {
            'a': a['waveform'], 'b': bv['waveform'], 'c': cv['waveform'], 'd': dv['waveform'],
            'w': w, 'x': x, 'y': y, 'z': z,
            'B': B, 'C': C, 'S': S,'R': R, 'T' : T
        }

        input_stream = InputStream(AudioExpr)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        tree = parser.expr()

        visitor = TensorEvalVisitor(variables, a['waveform'].shape)
        result_tensor = visitor.visit(tree)

        print("Audio Tree\n" + tree.toStringTree(recog=parser))
        print("Result Tensor: ", result_tensor)
        print("Result Tensor Shape: ", result_tensor.shape)

        # Create output dictionary with the same sample rate
        output = {
            'waveform': result_tensor,
            'sample_rate': a['sample_rate']
        }

        return (output,)
