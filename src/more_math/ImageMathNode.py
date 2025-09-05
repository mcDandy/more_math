from inspect import cleandoc

from antlr4 import CommonTokenStream
from antlr4.atn.LexerActionExecutor import InputStream
import torch
from .helper_functions import ThrowingErrorListener, getIndexTensorAlongDim

from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor

from comfy_api.latest import ComfyExtension, io

class ImageMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Latents.
    inputs:
        a, b, c, d:
            Latent, bound to variables with the same name. Defaults to zero latent if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Image expression:
            String, describing expression to mix images. 
        
    outputs:
        LATENT:
            Returns a LATENT object that contains the result of the math expression applied to the input conditionings.
    """
    def __init__(self):
        pass

    @classmethod
    def define_schema(cls) -> io.Schema:
        """
        """
        return io.Schema(
            node_id="mrmth_ImageMathNode",
            category="More math",
            display_name="Image math",
            inputs=[
                io.Image.Input(id="a"),
                io.Image.Input(id="b", optional=True),
                io.Image.Input(id="c", optional=True),
                io.Image.Input(id="d", optional=True),
                io.Float.Input(id="w", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0,optional=True, force_input=True),
                io.String.Input(id="Image", default="a*(1-w)+b*w", tooltip="Expression to apply on input images"),
            ],
            outputs=[
                io.Image.Output(),
            ],
        )

    @classmethod
    def execute(scls, Image, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        b = torch.zeros_like(a) if b is None else b
        c = torch.zeros_like(a) if c is None else c
        d = torch.zeros_like(a) if d is None else d

        B = getIndexTensorAlongDim(a, 0)
        W = getIndexTensorAlongDim(a, 2)
        H = getIndexTensorAlongDim(a, 1)
        C = getIndexTensorAlongDim(a, 3)

        variables = {'a': a, 'b': b, 'c': c, 'd': d, 'w': w, 'x': x, 'y': y, 'z': z,'B':B,'X':W,'Y':H,'C':C,'W':a.shape[1],'H':a.shape[2] }
        input_stream = InputStream(Image)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        parser.addErrorListener(ThrowingErrorListener())
        tree = parser.expr()
        print("Tree\n"+tree.toStringTree(recog=parser))
        visitor = TensorEvalVisitor(variables,a.shape)
        result = visitor.visit(tree)
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
