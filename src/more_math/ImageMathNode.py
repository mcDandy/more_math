from inspect import cleandoc
from math import e

from antlr4 import CommonTokenStream
from antlr4.atn.LexerActionExecutor import InputStream
import torch

from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor

class ImageMathNode:
    """
    This node enables the use of math expressions on Latents.
    INPUTS:
        a, b, c, d:
            Latent, bound to variables with the same name. Defaults to zero latent if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Image expression:
            String, describing expression to mix images. Valid functions are sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh, abs, sqrt, ln, log, exp, pow, min, max, norm, floor, ceil, round, gamma. Valid operators are +, -, *, /, %, ^,!˛&,|. Usable constants are e and pi.
        
    OUTPUTS:
        LATENT:
            Returns a LATENT object that contains the result of the math expression applied to the input conditionings.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
        """
        return {
            "required": {
                "a": ("IMAGE", {

                }),

                "Image": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "a*(1-w)+b*w",
                    "description": "Describes composition of the image. Valid functions are sin,cos,tan,abs,sqrt,min,max. Valid operators are +,-,*,/,^,%"

                }),
            },
            "optional": {
                "b": ("IMAGE", {
                    "default": 0,
                }),
                "c": ("IMAGE", {
                    "default": 0,
                }),
                "d": ("IMAGE", {
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

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image_output_name",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "imgMathNode"

    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    CATEGORY = "More math"

    def imgMathNode(self, Image, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        b = torch.zeros_like(a) if b is None else b
        c = torch.zeros_like(a) if c is None else c
        d = torch.zeros_like(a) if d is None else d



        variables = {'a': a, 'b': b, 'c': c, 'd': d, 'w': w, 'x': x, 'y': y, 'z': z}
        input_stream = InputStream(Image)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        tree = parser.expr()
        print("Tensor\n"+tree.toStringTree(recog=parser))
        visitor = TensorEvalVisitor(variables,a.shape)
        result = visitor.visit(tree)
        print("Result:", result)
        return (result,)


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
