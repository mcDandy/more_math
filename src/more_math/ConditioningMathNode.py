from inspect import cleandoc
from antlr4 import CommonTokenStream, InputStream
import torch

from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor



class ConditioningMathNode:
    """
    This node enables the use of math on conditionings. It is recommended to keep the Tensor expression the same as the pooled_output expression.
    INPUTS:
        a, b, c, d:
            Conditioning, bound to variables with the same name. Defaults to zero conditioning if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Tensor expression:
            String, describing expression to mix tensor part of conditioning. Tensor probably describes the composition of the image as it has the say what is on the image. Valid functions are sin, cos, tan, abs, sqrt, min, max, norm. Valid operators are +, -, *, /, ^, %. Usable constants are e and pi.
        Pooled output expression:
            String, describing expression to mix pooled_output part of conditioning. pooled_output does not have that much say in the image but can change some details of the image or completly change the image in some cases, probably also used for positional and temporal conditioning. Expression uses same syntax as Tensor expression.
        
    OUTPUTS:
        CONDITIONING:
            Returns a CONDITIONING object that contains the result of the math expression applied to the input conditionings.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
        """
        return {
            "required": {
                "a": ("CONDITIONING", {

                }),

                "Tensor": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "a*(1-w)+b*w",
                    "description": "Describes composition of the image. Valid functions are sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh, abs, sqrt, ln, log, exp, pow, min, max, norm, floor, ceil, round, gamma. Valid operators are +, -, *, /, %, ^,!˛&,|. Usable constants are e and pi."

                }),
                "pooled_output": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "a*(1-w)+b*w",
                    "description": "Can change some details of the image, probably also used for positional and temporal conditioning."
                }),
            },
            "optional": {
                "b": ("CONDITIONING", {
                    "default": 0,
                }),
                "c": ("CONDITIONING", {
                    "default": 0,
                }),
                "d": ("CONDITIONING", {
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

    RETURN_TYPES = ("CONDITIONING",)
    #RETURN_NAMES = ("image_output_name",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "condMathNode"

    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    CATEGORY = "More math"

    def condMathNode(self, Tensor,pooled_output, a, b=None, c=None, d=None,w=0.0,x=0.0,y=0.0,z=0.0):
        if b is None:
           b = [[torch.zeros_like(a[0][0]), {"pooled_output": torch.zeros_like(a[0][1]["pooled_output"])}]] 
        if c is None:
           c = [[torch.zeros_like(a[0][0]), {"pooled_output": torch.zeros_like(a[0][1]["pooled_output"])}]] 
        if d is None:
           d = [[torch.zeros_like(a[0][0]), {"pooled_output": torch.zeros_like(a[0][1]["pooled_output"])}]]


        ta = a[0][0].clone()
        tb = b[0][0].clone()
        pa = a[0][1]["pooled_output"].clone()
        pb = b[0][1]["pooled_output"].clone()
        tc = c[0][0].clone()
        td = d[0][0].clone()
        pc = c[0][1]["pooled_output"].clone()
        pd = d[0][1]["pooled_output"].clone()
   
        variables = {'a': ta, 'b': tb, 'c': tc, 'd': td, 'w': w, 'x': x, 'y': y, 'z': z}
        input_stream = InputStream(Tensor)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        tree = parser.expr()
        print("Tensor\n"+tree.toStringTree(recog=parser))
        visitor = TensorEvalVisitor(variables,ta.shape)
        result1 = visitor.visit(tree)
        

        variables = {'a': pa, 'b': pb, 'c': pc, 'd': pd, 'w': w, 'x': x, 'y': y, 'z': z}
        input_stream = InputStream(Tensor)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        tree = parser.expr()
        print("pooled_output\n"+tree.toStringTree(recog=parser))
        visitor = TensorEvalVisitor(variables,pa.shape)
        result2 = visitor.visit(tree)


        result = [[result1, {"pooled_output": result2}]]
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
