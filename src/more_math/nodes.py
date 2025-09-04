import torch

from .NoiseMathNode import NoiseMathNode
from .FloatMathNode import FloatMathNode
from .ConditioningMathNode import ConditioningMathNode
from .LatentMathNode import LatentMathNode
from .ImageMathNode import ImageMathNode
from .AudioMathNode import AudioMathNode

from comfy_api.latest import ComfyExtension, io

class IntToFloatNode(io.ComfyNode):
    """
    Converts int to float.
    """
    @classmethod
    def define_schema(cls) -> io.Schema:
         """
         """
         return io.Schema(
             node_id="mrmth_IntToFloat",
             category="More math",
             inputs=[
                 io.Int.Input(id="value", default=0),
             ],
             outputs=[
                 io.Float.Output(),
             ],
         )
    @classmethod
    def execute(self,cls, value):
        return (float(value),)

class FloatToIntNode(io.ComfyNode):
    """
    Converts float to int.
    """
    @classmethod
    def define_schema(cls) -> io.Schema:
        """
        """
        return io.Schema(
            node_id="mrmth_FloatToInt",
            category="More math",
            inputs=[
                io.Float.Input(id="value", default=0.0),
            ],
            outputs=[
                io.Int.Output(),
            ],
        )
    @classmethod
    def execute(self, value):
        return (int(value),)


NODE_id_MAPPINGS = {
    "mrmth_ConditioningMathNode": "Conditioning math",
    "mrmth_LatentMathNode": "Latent math",
    "mrmth_ImageMathNode": "Image math",
    "mrmth_FloatMathNode": "Float math",
    "mrmth_NoiseMathNode": "Noise math",
    "mrmth_AudioMathNode": "Audio math",
    "mrmth_IntToFloat": "Int → Float",
    "mrmth_FloatToInt": "Float → Int",
    "Tensor": "Tensor expression",
    "Latent": "Latent expression",
    "Image": "Image expression",
    "FloatFunc": "Float expression",
    "pooled_output": "Pooled output tensor expression"
}

class MoreMathExtension(ComfyExtension):
    def __init__(self):
        pass
    @classmethod
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
            return [
                ConditioningMathNode,
                LatentMathNode,
                ImageMathNode,
                FloatMathNode,
                NoiseMathNode,
                IntToFloatNode,
                FloatToIntNode,
                AudioMathNode, 
            ]
async def comfy_entrypoint() -> MoreMathExtension:
    return MoreMathExtension()
