from inspect import cleandoc
import torch
from antlr4 import CommonTokenStream, InputStream
from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor
from .helper_functions import getIndexTensorAlongDim

class AudioMathNode:
    """
    This node enables the use of math expressions on AUDIO tensors.
    INPUTS:
        a, b, c, d:
            AUDIO, bound to variables with the same name. Defaults to zero AUDIO if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Audio expression:
            String, describing expression to apply to audio tensors.

    OUTPUTS:
        AUDIO:
            Returns an AUDIO object that contains the result of the math expression applied to the input audio tensors.
    """
    def __init__(self):
        pass

    @classmethod   
    def INPUT_TYPES(s):
        """
        """
        return {
            "required": {
                "a": ("AUDIO", {
                    "description": "Input audio tensor"
                }),
                "AudioExpr": ("STRING", {
                    "multiline": False,
                    "default": "a*(1-w)+b*w",
                    "description": "Expression to apply on input audio tensors"
                }),
            },
            "optional": {
                "b": ("AUDIO", {
                    "default": 0,
                    "description": "Second input audio tensor"
                }),
                "c": ("AUDIO", {
                    "default": 0,
                    "description": "Third input audio tensor"
                }),
                "d": ("AUDIO", {
                    "default": 0,
                    "description": "Fourth input audio tensor"
                }),
                "w": ("FLOAT", {
                    "default": 0,
                    "forceInput": True
                }),
                "x": ("FLOAT", {
                    "default": 0,
                    "forceInput": True
                }),
                "y": ("FLOAT", {
                    "default": 0,
                    "forceInput": True
                }),
                "z": ("FLOAT", {
                    "default": 0,
                    "forceInput": True
                }),
            }
        }

    RETURN_TYPES = ("AUDIO",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "audioMathNode"
    CATEGORY = "More math"

    def audioMathNode(self, a, AudioExpr, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
   

        bv = b if b else {'waveform':torch.zeros_like(a['waveform']),'sample_rate':a['sample_rate']}
        cv = c if c else {'waveform':torch.zeros_like(a['waveform']),'sample_rate':a['sample_rate']}
        dv = d if d else {'waveform':torch.zeros_like(a['waveform']),'sample_rate':a['sample_rate']}
        print("AudioMathNode: a shape:", a['waveform'].shape)


        B = getIndexTensorAlongDim(a['waveform'], 0)
        C = getIndexTensorAlongDim(a['waveform'], 1)
        T = getIndexTensorAlongDim(a['waveform'], 2)
       

        variables = {
            'a': a['waveform'], 'b': bv['waveform'], 'c': cv['waveform'], 'd': dv['waveform'],
            'w': w, 'x': x, 'y': y, 'z': z,
            'B': B, 'C': C, 'T': T
        }

        input_stream = InputStream(AudioExpr)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        tree = parser.expr()

        visitor = TensorEvalVisitor(variables, a['waveform'].shape)
        result_tensor = visitor.visit(tree)

        # Create output dictionary with the same sample rate
        output = {
            'waveform': result_tensor,
            'sample_rate': a['sample_rate']
        }

        return (output,)
