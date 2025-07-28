from .ConditioningMathNode import ConditioningMathNode
from .LatentMathNode import LatentMathNode
from .ImageMathNode import ImageMathNode

class IntToFloatNode:
    """
    Converts int to float.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "convert"
    CATEGORY = "More math"

    def convert(self, value):
        return (float(value),)

class FloatToIntNode:
    """
    Converts float to int.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "convert"
    CATEGORY = "More math"

    def convert(self, value):
        return (int(value),)

NODE_CLASS_MAPPINGS = {
    "mrmth_ConditioningMathNode": ConditioningMathNode,
    "mrmth_LatentMathNode": LatentMathNode,
    "mrmth_ImageMathNode": ImageMathNode,
    "mrmth_IntToFloat": IntToFloatNode,
    "mrmth_FloatToInt": FloatToIntNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "mrmth_ConditioningMathNode": "Conditioning math node",
    "mrmth_LatentMathNode": "Latent math node",
    "mrmth_ImageMathNode": "Image math node",
     "mrmth_IntToFloat": "Int → Float",
    "mrmth_FloatToInt": "Float → Int",
    "Tensor": "Tensor expression",
    "Latent": "Latent expression",
    "Image": "Image expression",
    "pooled_output": "Pooled output tensor expression"
}



