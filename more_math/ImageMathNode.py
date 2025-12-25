import torch
from .helper_functions import getIndexTensorAlongDim, comonLazy, eval_tensor_expr, make_zero_like

from comfy_api.latest import io


class ImageMathNode(io.ComfyNode):
    """
    Enables math expressions on Images.
    
    Inputs:
        a, b, c, d: Image inputs (b, c, d default to zero if not provided)
        w, x, y, z: Float variables for expressions
        Image: Expression to apply on input images
    
    Outputs:
        IMAGE: Result of applying expression to input images
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ImageMathNode",
            category="More math",
            display_name="Image math",
            inputs=[
                io.Image.Input(id="a"),
                io.Image.Input(id="b", optional=True, lazy=True),
                io.Image.Input(id="c", optional=True, lazy=True),
                io.Image.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Image", default="a*(1-w)+b*w", tooltip="Expression to apply on input images"),
            ],
            outputs=[
                io.Image.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Image, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0):
        return comonLazy(Image, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, Image, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        b = make_zero_like(a) if b is None else b
        c = make_zero_like(a) if c is None else c
        d = make_zero_like(a) if d is None else d

        # Permute to B, C, H, W for processing
        a = a.permute(0, 3, 1, 2)
        b = b.permute(0, 3, 1, 2)
        c = c.permute(0, 3, 1, 2)
        d = d.permute(0, 3, 1, 2)

        variables = {
            'a': a, 'b': b, 'c': c, 'd': d,
            'w': w, 'x': x, 'y': y, 'z': z,
            'X': getIndexTensorAlongDim(a, 3),
            'Y': getIndexTensorAlongDim(a, 2),
            'B': getIndexTensorAlongDim(a, 0), 'batch': getIndexTensorAlongDim(a, 0),
            'C': getIndexTensorAlongDim(a, 1), 'channel': getIndexTensorAlongDim(a, 1),
            'W': a.shape[3], 'width': a.shape[3],
            'H': a.shape[2], 'height': a.shape[2],
            'T': a.shape[0], 'batch_count': a.shape[0],
            'N': a.shape[1], 'channel_count': a.shape[1],
        }

        result = eval_tensor_expr(Image, variables, a.shape)

        # Permute back to B, H, W, C
        result = result.permute(0, 2, 3, 1)
        return (result,)
