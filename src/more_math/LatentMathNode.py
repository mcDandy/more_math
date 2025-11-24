from inspect import cleandoc

from comfy_api.latest import ComfyExtension, io

from antlr4 import CommonTokenStream, InputStream
import torch

from .helper_functions import ThrowingErrorListener, getIndexTensorAlongDim

from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor

class LatentMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Latents.
    inputs:
        a, b, c, d:
            Latent, bound to variables with the same name. Defaults to zero latent if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Latent expression:
            String, describing expression to aply to latents.

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
            node_id="mrmth_LatentMathNode",
            display_name="Latent math",
            category="More math",
            inputs=[
                io.Latent.Input(id="a"),
                io.Latent.Input(id="b", optional=True),
                io.Latent.Input(id="c", optional=True),
                io.Latent.Input(id="d", optional=True),
                io.Float.Input(id="w", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0,optional=True, force_input=True),
                io.String.Input(id="Latent", default="a*(1-w)+b*w", tooltip="Expression to apply on input latents"),
            ],
            outputs=[
                io.Latent.Output(),
            ],
        )

    #RETURN_NAMES = ("image_output_name",)
    tooltip = cleandoc(__doc__)

    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node


    @classmethod
    def execute(cls, Latent, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:
        a = a["samples"]
        b = torch.zeros_like(a) if b is None else b["samples"]
        c = torch.zeros_like(a) if c is None else c["samples"]
        d = torch.zeros_like(a) if d is None else d["samples"]

        # support tensors with >=4 dims (e.g. 4D latents [B,C,H,W] or 5D [B,T,C,H,W])
        ndim = a.ndim
        # use negative indexing so that channel/height/width mapping works for 4D and 5D
        batch_dim = 0
        channel_dim = -3
        height_dim = -2
        width_dim = -1
        time_dim = None
        if ndim >= 5:
            # time/frame dim is the one before channels when present
            time_dim = -4

        B = getIndexTensorAlongDim(a, batch_dim)
        C = getIndexTensorAlongDim(a, channel_dim)
        H = getIndexTensorAlongDim(a, height_dim)
        W = getIndexTensorAlongDim(a, width_dim)

        # fill scalar/value tensors
        width_val = a.shape[width_dim]
        height_val = a.shape[height_dim]
        channel_count = a.shape[channel_dim]
        batch_count = a.shape[batch_dim]
        frame_count = a.shape[time_dim] if time_dim is not None else a.shape[batch_dim]
        T = a.shape[0]

        variables = {
            # core tensors and floats
            'a': a, 'b': b, 'c': c, 'd': d,
            'w': w, 'x': x, 'y': y, 'z': z,

             'X': W, 'Y': H,
            'B': B, 'batch': B,
            'C': C, 'channel': C,
            # scalar dims and counts
            'W': width_val, 'width': width_val,
            'H': height_val, 'height': height_val,
            'T': batch_count, 'batch_count': batch_count,
            'N': channel_count, 'channel_count': channel_count,
        }
        # expose time/frame if present
        if time_dim is not None:
            F = getIndexTensorAlongDim(a, time_dim)
            variables.update({'frame_idx': F, 'frame': F, 'frame_count': frame_count})

        input_stream = InputStream(Latent)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        parser.addErrorListener(ThrowingErrorListener())
        tree = parser.expr()
        visitor = TensorEvalVisitor(variables,a.shape)
        result1 = visitor.visit(tree)
        result = {"samples": result1}
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
