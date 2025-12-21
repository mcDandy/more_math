from inspect import cleandoc
from comfy_api.latest import io
from antlr4 import CommonTokenStream, InputStream
from .Parser.MathExprLexer import MathExprLexer
from .helper_functions import comonLazy
from .modelLikeCommon import calculate_patches

import copy


class ModelMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Model weights (state_dict).
    Functionally acts as a custom model merge.
    """
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ModelMathNode",
            display_name="Model Math",
            category="More math",
            inputs=[
                io.Model.Input(id="a", tooltip="Main model (base)"),
                io.Model.Input(id="b", optional=True,lazy=True, tooltip="Optional 2nd model"),
                io.Model.Input(id="c", optional=True,lazy=True, tooltip="Optional 3rd model"),
                io.Model.Input(id="d", optional=True,lazy=True, tooltip="Optional 4th model"),
                io.Float.Input(id="w", default=0.0, optional=True,lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True,lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True,lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True,lazy=True, force_input=True),
                io.String.Input(id="Model", default="a*(1-w)+b*w", tooltip="Expression to apply on weights"),
            ],
            outputs=[
                io.Model.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Model, a, b=[], c=[], d=[],w=0,x=0,y=0,z=0):
        return comonLazy(Model, a, b, c, d)

    @classmethod
    def execute(cls, Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:
        patches = calculate_patches(Model, a, b, c, d, w, x, y, z)
        out_model = a.clone()
        if patches:
            out_model.add_patches(patches, 1.0, 1.0)
        return (out_model,)