from inspect import cleandoc

from antlr4 import CommonTokenStream, InputStream

from .helper_functions import ThrowingErrorListener

from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.FloatEvalVisitor import FloatEvalVisitor

from comfy_api.latest import io

class FloatMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Latents.
    inputs:
        a, b, c, d:
            Floats, bound to variables with the same name. Defaults to 0.0 if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Latent expression:
            String, describing expression to mix latents. Valid functions are sin, cos, tan, abs, sqrt, min, max, norm. Valid operators are +, -, *, /, ^, %. Usable constants are e and pi.

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
            node_id="mrmth_FloatMathNode",
            category="More math",
            display_name="Float math",
            inputs=[
                io.Float.Input(id="a", force_input=True),
                io.Float.Input(id="b", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="c", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="d", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="w", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0,optional=True, force_input=True),
                io.String.Input(id="FloatFunc", default="a*(1-w)+b*w", tooltip="Expression to use on inputs"),
            ],
            outputs=[
                io.Float.Output(),
            ],
        )

    #RETURN_NAMES = ("image_output_name",)
    tooltip = cleandoc(__doc__)

    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node
    @classmethod
    def execute(cls, FloatFunc, a, b=0.0, c=0.0, d=0.0, w=0.0, x=0.0, y=0.0, z=0.0):



        variables = {'a': a, 'b': b, 'c': c, 'd': d, 'w': w, 'x': x, 'y': y, 'z': z}
        input_stream = InputStream(FloatFunc)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        parser.addErrorListener(ThrowingErrorListener())
        tree = parser.expr()
        visitor = FloatEvalVisitor(variables)
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
