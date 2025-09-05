from inspect import cleandoc
from math import e

from antlr4 import CommonTokenStream, InputStream
import torch

from .helper_functions import ThrowingErrorListener, getIndexTensorAlongDim

from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor

from comfy_api.latest import ComfyExtension, io

class NoiseMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Latents.
    inputs:
        a, b, c, d:
            Noise generators, bound to variables with the same name. Defaults to zero latent if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Latent expression:
            String, describing expression to mix noise.
        
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
            node_id="mrmth_NoiseMathNode",
            category="More math",
            inputs=[
                io.Noise.Input(id="a"),
                io.Noise.Input(id="b", optional=True),
                io.Noise.Input(id="c", optional=True),
                io.Noise.Input(id="d", optional=True),
                io.Float.Input(id="w", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0,optional=True, force_input=True),
                io.String.Input(id="Noise", default="a*(1-w)+b*w", tooltip="Expression to apply on input noise generators"),
            ],
            outputs=[
                io.Noise.Output(),
            ],
        )
    #RETURN_NAMES = ("image_output_name",)
    tooltip = cleandoc(__doc__)
    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    CATEGORY = "More math"

    @classmethod
    def execute(cls, Noise, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        return (NoiseExecutor(a, b, c, d, w, x, y, z, Noise),)

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

    


class NoiseExecutor():
    def __init__(self,a,b,c,d,w,x,y,z, Noise):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.expr = Noise
    seed = -1;
    def generate_noise(self, input_latent:torch.Tensor) -> torch.Tensor:
        if self.b is None:
            self.vb = torch.zeros_like(input_latent["samples"])
        else:
            self.vb = self.b.generate_noise(input_latent)
        if self.c is None:
            self.vc = torch.zeros_like(input_latent["samples"])
        else:
            self.vc = self.c.generate_noise(input_latent)
        if self.d is None:
            self.vd = torch.zeros_like(input_latent["samples"])
        else:
            self.vd = self.d.generate_noise(input_latent)

        B = getIndexTensorAlongDim(input_latent["samples"], 0)
        W = getIndexTensorAlongDim(input_latent["samples"], 3)
        H = getIndexTensorAlongDim(input_latent["samples"], 2)
        C = getIndexTensorAlongDim(input_latent["samples"], 1)

        variables = {'a': self.a.generate_noise(input_latent), 'b': self.vb, 'c': self.vc, 'd': self.vd, 'w': self.w, 'x': self.x, 'y': self.y, 'z': self.z,'B':B,'X':W,'Y':H,'C':C,'W':input_latent["samples"].shape[3],'H':input_latent["samples"].shape[2],'I':input_latent["samples"]}
        input_stream = InputStream(self.expr)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        parser.addErrorListener(ThrowingErrorListener())
        tree = parser.expr()
        print("Tree\n"+tree.toStringTree(recog=parser))
        visitor = TensorEvalVisitor(variables,variables['a'].shape)
        result = visitor.visit(tree)
        return result
