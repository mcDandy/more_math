from .SigmasMathNode import SigmasMathNode
from .GuiderMathNode import GuiderMathNode
from .deprecated.NoiseMathNode import NoiseMathNodeOLD
from .deprecated.AudioMathNode import AudioMathNodeOLD
from .deprecated.ConditioningMathNode import ConditioningMathNodeOLD
from .deprecated.ImageMathNode import ImageMathNodeOLD
from .deprecated.LatentMathNode import LatentMathNodeOLD
from .deprecated.MaskMathNode import MaskMathNodeOLD
from .deprecated.ModelMathNode import ModelMathNodeOLD
from .deprecated.VaeMathNode import VAEMathNodeOLD
from .deprecated.ClipMathNode import CLIPMathNodeOLD
from .deprecated.VideoMathNode import VideoMathNodeOLD

from .FloatMathNode import FloatMathNode
from .ConditioningMathNode import ConditioningMathNode
from .LatentMathNode import LatentMathNode
from .ImageMathNode import ImageMathNode
from .MaskMathNode import MaskMathNode
from .VideoMathNode import VideoMathNode
from .ModelMathNode import ModelMathNode
from .VaeMathNode import VAEMathNode
from .ClipMathNode import CLIPMathNode
from .SpectrogramToAudioNode import SpectrogramToAudio
from .AudioToSpectrogramNode import AudioToSpectrogram

from .NoiseMathNode import NoiseMathNode
from .AudioMathNode import AudioMathNode

from comfy_api.latest import ComfyExtension, io


class IntToFloatNode(io.ComfyNode):
    """
    Converts int to float.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        """ """
        return io.Schema(
            node_id="mrmth_IntToFloat",
            display_name="Int -> Float",
            category="More math",
            inputs=[
                io.Int.Input(id="value", default=0),
            ],
            outputs=[
                io.Float.Output(),
            ],
        )

    @classmethod
    def execute(cls, value):
        return (float(value),)


class FloatToIntNode(io.ComfyNode):
    """
    Converts float to int.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        """ """
        return io.Schema(
            node_id="mrmth_FloatToInt",
            category="More math",
            display_name="Float -> Int",
            inputs=[
                io.Float.Input(id="value", default=0.0),
            ],
            outputs=[
                io.Int.Output(),
            ],
        )

    @classmethod
    def execute(cls, value):
        return (int(value),)


class MoreMathExtension(ComfyExtension):
    def __init__(self):
        pass

    @classmethod
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [
            ConditioningMathNode,
            ConditioningMathNodeOLD,
            ModelMathNode,
            ModelMathNodeOLD,
            CLIPMathNode,
            CLIPMathNodeOLD,
            VAEMathNode,
            VAEMathNodeOLD,
            LatentMathNode,
            LatentMathNodeOLD,
            ImageMathNode,
            ImageMathNodeOLD,
            MaskMathNode,
            MaskMathNodeOLD,
            FloatMathNode,
            NoiseMathNodeOLD,
            IntToFloatNode,
            FloatToIntNode,
            AudioMathNodeOLD,
            VideoMathNode,
            VideoMathNodeOLD,
            AudioToSpectrogram,
            SpectrogramToAudio,
            SigmasMathNode,
            GuiderMathNode,
            NoiseMathNode,
            AudioMathNode
        ]


async def comfy_entrypoint() -> MoreMathExtension:
    return MoreMathExtension()
