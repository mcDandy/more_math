from inspect import cleandoc
from math import e

from antlr4 import CommonTokenStream, InputStream
import torch

from .helper_functions import getIndexTensorAlongDim

from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor

class NoiseMathNode:
    """
    This node enables the use of math expressions on Latents.
    INPUTS:
        a, b, c, d:
            Noise generators, bound to variables with the same name. Defaults to zero latent if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Latent expression:
            String, describing expression to mix latents. Valid functions are sin, cos, tan, abs, sqrt, min, max, norm. Valid operators are +, -, *, /, ^, %. Usable constants are e and pi.
        
    OUTPUTS:
        LATENT:
            Returns a LATENT object that contains the result of the math expression applied to the input conditionings.
    """
    def __init__(self):
        va= None
        vb= None
        vc= None
        vd= None
        vw= 0.0
        vx= 0.0
        vy= 0.0
        vz= 0.0
        expr="";
    @classmethod
    def INPUT_TYPES(s):
        """
        """
        return {
            "required": {
                "a": ("NOISE", {

                }),

                "Noise": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "a*(1-w)+b*w",
                    "description": "Describes inital noise. Valid functions are sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh, abs, sqrt, ln, log, exp, pow, min, max, norm, floor, ceil, round, gamma. Valid operators are +, -, *, /, %, ^,!˛&,|. Usable constants are e and pi."

                }),
            },
            "optional": {
                "b": ("NOISE", {
                    "default": 0,
                }),
                "c": ("NOISE", {
                    "default": 0,
                }),
                "d": ("NOISE", {
                    "default": 0,
                }),
                "w": ("FLOAT", {
                    "default": 0,
                    "forceInput":True
                }),
                "x": ("FLOAT", {
                    "default": 0,
                    "forceInput":True
                }),
                "y": ("FLOAT", {
                    "default": 0,
                    "forceInput":True
                }),
                "z": ("FLOAT", {
                    "default": 0,
                    "forceInput":True
                }),


                # "int_field": ("INT", {"default": 0, "min": 0, "max": 100, "step": 1}),
                # "float_field": ("FLOAT", {"default": 0.5, "min": -10.0, "max": 10.0, "step": 0.001}),
            }
        }

    RETURN_TYPES = ("NOISE",)
    #RETURN_NAMES = ("image_output_name",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "noiMathNode"
    seed = 0
    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    CATEGORY = "More math"

    def noiMathNode(self, Noise, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        self.va = a
        self.vb = b
        self.vc = c
        self.vd = d
        self.vw = w
        self.vx = x
        self.vy = y
        self.vz = z

        self.expr = Noise
        return (self,)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

    
    def generate_noise(self, input_latent:torch.Tensor) -> torch.Tensor:
        print(input_latent)
        if self.vb is None:
            self.vb = torch.zeros_like(input_latent["samples"])
        else:
            self.vb = self.vb.generate_noise(input_latent)
        if self.vc is None:
            self.vc = torch.zeros_like(input_latent["samples"])
        else:
            self.vc = self.vc.generate_noise(input_latent)
        if self.vd is None:
            self.vd = torch.zeros_like(input_latent["samples"])
        else:
            self.vd = self.vd.generate_noise(input_latent)

        B = getIndexTensorAlongDim(input_latent["samples"], 0)
        W = getIndexTensorAlongDim(input_latent["samples"], 2)
        H = getIndexTensorAlongDim(input_latent["samples"], 3)
        C = getIndexTensorAlongDim(input_latent["samples"], 1)

        variables = {'a': self.va.generate_noise(input_latent), 'b': self.vb, 'c': self.vc, 'd': self.vd, 'w': self.vw, 'x': self.vx, 'y': self.vy, 'z': self.vz,'B':B,'X':W,'Y':H,'C':C,'W':input_latent["samples"].shape[2],'H':input_latent["samples"].shape[3]}
        input_stream = InputStream(self.expr)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        tree = parser.expr()
        print("Tree\n"+tree.toStringTree(recog=parser))
        visitor = TensorEvalVisitor(variables,variables['a'].shape)
        result = visitor.visit(tree)
        return result
