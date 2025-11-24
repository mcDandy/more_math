from inspect import cleandoc

from comfy_api.latest import ComfyExtension, io
from comfy_api.input_impl import VideoFromComponents, VideoFromFile
from comfy_api.util import VideoCodec, VideoComponents, VideoContainer


from antlr4 import CommonTokenStream, InputStream
import torch

from .helper_functions import ThrowingErrorListener, getIndexTensorAlongDim

from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor

class VideoMathNode(io.ComfyNode):
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
            node_id="mrmth_VideoMathNode",
            display_name="Video math",
            category="More math",
            inputs=[
                io.Video.Input(id="a"),
                io.Video.Input(id="b", optional=True),
                io.Video.Input(id="c", optional=True),
                io.Video.Input(id="d", optional=True),
                io.Float.Input(id="w", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0,optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0,optional=True, force_input=True),
                io.String.Input(id="Audio", default="a*(1-w)+b*w", tooltip="Expression to apply on audio part of video"),
                io.String.Input(id="Images", default="a*(1-w)+b*w", tooltip="Expression to apply on image part of video"),
            ],
            outputs=[
                io.Video.Output(),
            ],
        )

    #RETURN_NAMES = ("image_output_name",)
    tooltip = cleandoc(__doc__)

    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node


    @classmethod
    def execute(cls, Audio,Images, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:

        ac = a.get_components()
        bc = b.get_components() if b is not None else VideoComponents(images=torch.zeros_like(ac.images), audio={'waveform':torch.zeros_like(ac.audio['waveform']),'sample_rate':ac.audio['sample_rate']}, frame_rate=ac.frame_rate,metadata=None)
        cc = c.get_components() if c is not None else VideoComponents(images=torch.zeros_like(ac.images), audio={'waveform':torch.zeros_like(ac.audio['waveform']),'sample_rate':ac.audio['sample_rate']}, frame_rate=ac.frame_rate,metadata=None)
        dc = d.get_components() if d is not None else VideoComponents(images=torch.zeros_like(ac.images), audio={'waveform':torch.zeros_like(ac.audio['waveform']),'sample_rate':ac.audio['sample_rate']}, frame_rate=ac.frame_rate,metadata=None)


        B = getIndexTensorAlongDim(ac.images, 0)
        X = getIndexTensorAlongDim(ac.images, 2)
        Y = getIndexTensorAlongDim(ac.images, 1)
        W = torch.full_like(Y, ac.images.shape[2], dtype=torch.float32)
        H = torch.full_like(Y, ac.images.shape[1], dtype=torch.float32)
        C = getIndexTensorAlongDim(ac.images, 3)
        R = torch.full_like(Y, float(ac.frame_rate), dtype=torch.float32)
        T = torch.full_like(Y, ac.images.shape[0], dtype=torch.float32)

        variables = {'a': ac.images, 'b': bc.images, 'c': cc.images, 'd': dc.images, 'w': w, 'x': x, 'y': y, 'z': z,
                     'X':X,'Y':Y,
                     'B':B,'frame':B,
                     'W':W,'width':W,
                     'H':H,'height':H,
                     'C':C,'channel':C,
                     'R':R,'frame_rate':R,
                     'frame_count':ac.images.shape[0],
                     'N':ac.images.shape[3],'channel_count':ac.images.shape[3]}

        input_stream = InputStream(Images)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        parser.addErrorListener(ThrowingErrorListener())
        tree = parser.expr()
        visitor = TensorEvalVisitor(variables,ac.images.shape)
        imgs = visitor.visit(tree)


        B = getIndexTensorAlongDim(ac.audio['waveform'], 0)
        C = getIndexTensorAlongDim(ac.audio['waveform'], 1)
        S = getIndexTensorAlongDim(ac.audio['waveform'], 2)
        R = torch.full_like(S, ac.audio['sample_rate'], dtype=torch.float32)
        T = torch.full_like(S, ac.audio['waveform'].shape[2], dtype=torch.float32)
        N= ac.audio['waveform'].shape[1]

        variables = {
            'a': ac.audio['waveform'], 'b': bc.audio['waveform'], 'c': cc.audio['waveform'], 'd': dc.audio['waveform'],
            'w': w, 'x': x, 'y': y, 'z': z,

            'B': B, 'batch': B,
            'C': C, 'channel': C,
            'S': S, 'sample': S,
            'R': R, 'sample_rate': R,
            'T': T, 'sample_count': T,
            'N': N, 'channel_count': N
        }

        input_stream = InputStream(Audio)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        tree = parser.expr()

        visitor = TensorEvalVisitor(variables, ac.audio['waveform'].shape)
        result_tensor = visitor.visit(tree)

        # Create output dictionary with the same sample rate
        audioo = {
            'waveform': result_tensor,
            'sample_rate': ac.audio['sample_rate']
        }





        out = VideoFromComponents(VideoComponents(images=imgs, audio=audioo, frame_rate=ac.frame_rate,metadata=ac.metadata))
        return (out,)


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
