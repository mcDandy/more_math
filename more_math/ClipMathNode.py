from comfy_api.latest import io
from .modelLikeCommon import calculate_patches
from inspect import cleandoc
from .helper_functions import comonLazy

class CLIPMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on CLIP weights.
    """
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_CLIPMathNode",
            display_name="CLIP Math",
            category="More math",
            inputs=[
                io.Clip.Input(id="a", tooltip="Main CLIP (base)"),
                io.Clip.Input(id="b", optional=True,lazy=True, tooltip="Optional 2nd CLIP"),
                io.Clip.Input(id="c", optional=True,lazy=True, tooltip="Optional 3rd CLIP"),
                io.Clip.Input(id="d", optional=True,lazy=True, tooltip="Optional 4th CLIP"),
                io.Float.Input(id="w", default=0.0, optional=True,lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True,lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True,lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True,lazy=True, force_input=True),
                io.String.Input(id="Model", default="a*(1-w)+b*w", tooltip="Expression to apply on weights"),
            ],
            outputs=[
                io.Clip.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)
    @classmethod
    def check_lazy_status(cls, Model, a, b=[], c=[], d=[],w=0,x=0,y=0,z=0):
        return comonLazy(Model, a, b, c, d,w,x,y,z)

    @classmethod
    def execute(cls, Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:
        patcher_a = a.patcher
        patcher_b = b.patcher if b else None
        patcher_c = c.patcher if c else None
        patcher_d = d.patcher if d else None

        patches = calculate_patches(Model, patcher_a, patcher_b, patcher_c, patcher_d, w, x, y, z)

        out_clip = a.clone()
        if patches:
            out_clip.add_patches(patches, 1.0, 1.0)
        return (out_clip,)
