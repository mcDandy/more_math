from inspect import cleandoc
from antlr4 import CommonTokenStream, InputStream
import torch

from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor

from comfy_api.latest import io

class ConditioningMathNode(io.ComfyNode):
    """
    This node enables the use of math on conditionings. It is recommended to keep the Tensor expression the same as the pooled_output expression.
    inputs:
        a, b, c, d:
            Conditioning, bound to variables with the same name. Defaults to zero conditioning if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Tensor expression:
            String, describing expression to mix tensor part of conditioning. Tensor probably describes the composition of the image as it has the say what is on the image.
        Pooled output expression:
            String, describing expression to mix pooled_output part of conditioning. pooled_output is Tensor compressed into 1 token.

    outputs:
        CONDITIONING:
            Returns a CONDITIONING object that contains the result of the math expression applied to the input conditionings.
    """
    def __init__(self):
        pass

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ConditioningMathNode",
            display_name="Conditioning math",
            category="More math",
            inputs=[
                io.Conditioning.Input(id="a"),
                io.Conditioning.Input(id="b", optional=True),
                io.Conditioning.Input(id="c", optional=True),
                io.Conditioning.Input(id="d", optional=True),
                io.Float.Input(id="w", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0,optional=True, force_input=True),
                io.String.Input(id="Tensor", default="a*(1-w)+b*w", tooltip="Describes composition of the image."),
                io.String.Input(id="pooled_output", default="a*(1-w)+b*w", tooltip="Composition of the image condensed into one vector"),
            ],
            outputs=[
                io.Conditioning.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    @classmethod
    def execute(cls, Tensor,pooled_output, a, b=None, c=None, d=None,w=0.0,x=0.0,y=0.0,z=0.0):
        if b is None:
           b = [[torch.zeros_like(a[0][0]), {"pooled_output": torch.zeros_like(a[0][1]["pooled_output"]) if a[0][1]["pooled_output"] else None}]]
        if c is None:
           c = [[torch.zeros_like(a[0][0]), {"pooled_output": torch.zeros_like(a[0][1]["pooled_output"]) if a[0][1]["pooled_output"] else None}]]
        if d is None:
           d = [[torch.zeros_like(a[0][0]), {"pooled_output": torch.zeros_like(a[0][1]["pooled_output"]) if a[0][1]["pooled_output"] else None}]]


        ta = a[0][0].clone()
        tb = b[0][0].clone()
        tc = c[0][0].clone()
        td = d[0][0].clone()
        pa = None
        pb = None
        pc = None
        pd = None
        if a[0][1]["pooled_output"] is not None:
            pa = a[0][1]["pooled_output"].clone()
            pb = b[0][1]["pooled_output"].clone()
            pc = c[0][1]["pooled_output"].clone()
            pd = d[0][1]["pooled_output"].clone()

        print(ta.shape,pa.shape if pa != None else 0);

        variables = {'a': ta, 'b': tb, 'c': tc, 'd': td, 'w': w, 'x': x, 'y': y, 'z': z}
        input_stream = InputStream(Tensor)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        tree = parser.expr()
        visitor = TensorEvalVisitor(variables,ta.shape)
        result1 = visitor.visit(tree)

        if a[0][1]["pooled_output"]:
            variables = {'a': pa, 'b': pb, 'c': pc, 'd': pd, 'w': w, 'x': x, 'y': y, 'z': z}
            input_stream = InputStream(Tensor)
            lexer = MathExprLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = MathExprParser(stream)
            tree = parser.expr()
            visitor = TensorEvalVisitor(variables,pa.shape)
            result2 = visitor.visit(tree)
        else:
            result2 = None
            print("No pooled_output found in input conditioning, skipping pooled_output calculation.")

        result = [[result1, {"pooled_output": result2}]]
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
