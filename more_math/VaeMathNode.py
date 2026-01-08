from inspect import cleandoc
from comfy_api.latest import io
import copy
from .modelLikeCommon import calculate_patches
from .helper_functions import comonLazy


class VAEMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on VAE weights.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_VAEMathNode",
            display_name="VAE Math",
            category="More math",
            inputs=[
                io.Vae.Input(id="a", tooltip="Main VAE (base)"),
                io.Vae.Input(id="b", optional=True, lazy=True, tooltip="Optional 2nd VAE"),
                io.Vae.Input(id="c", optional=True, lazy=True, tooltip="Optional 3rd VAE"),
                io.Vae.Input(id="d", optional=True, lazy=True, tooltip="Optional 4th VAE"),
                io.Float.Input(id="w", default=0.0, lazy=True, optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0, lazy=True, optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0, lazy=True, optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0, lazy=True, optional=True, force_input=True),
                io.String.Input(id="Model", default="a*(1-w)+b*w", tooltip="Expression to apply on weights"),
            ],
            outputs=[
                io.Vae.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Model, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0):
        return comonLazy(Model, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:
        patcher_a = a.patcher
        patcher_b = b.patcher if b else None
        patcher_c = c.patcher if c else None
        patcher_d = d.patcher if d else None

        patches = calculate_patches(Model, patcher_a, patcher_b, patcher_c, patcher_d, w, x, y, z)

        # VAE does not have a clone method, so we shallow copy and clone the patcher
        out_vae = copy.copy(a)
        out_vae.patcher = a.patcher.clone()

        if patches:
            out_vae.patcher.add_patches(patches, 1.0, 1.0)

        return (out_vae,)
