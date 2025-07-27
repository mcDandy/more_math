from .ConditioningMathNode import ConditioningMathNode
from .LatentMathNode import LatentMathNode
from .ImageMathNode import ImageMathNode

NODE_CLASS_MAPPINGS = {
    "mrmth_ConditioningMathNode": ConditioningMathNode,
    "mrmth_LatentMathNode": LatentMathNode,
    "mrmth_ImageMathNode": ImageMathNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "mrmth_ConditioningMathNode": "Conditioning math node",
    "mrmth_LatentMathNode": "Latent math node",
    "mrmth_ImageMathNode": "Image math node",
    "Tensor": "Tensor expression",
    "Latent": "Latent expression",
    "Image": "Image expression",
    "pooled_output": "Pooled output tensor expression"
}
