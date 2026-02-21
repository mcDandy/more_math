from inspect import cleandoc
from comfy_api.latest import io
from .helper_functions import checkLazyNew
from .Stack import MrmthStack
from .ParseTree import MrmthParseTree
import copy
import comfy.utils
from .modelLikeCommon import calculate_patches_autogrow


class ModelMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Model weights (state_dict) using Autogrow inputs.
    Functionally acts as a custom model merge.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_ModelMathNode",
            display_name="Model Math",
            category="More math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Model.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.MultiType.Input(
                    io.String.Input("Expression", default="I0*(1-F0)+I1*F0", multiline=False),
                    types=[io.String,MrmthParseTree],
                    tooltip="Expression to apply on weights",
                ),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["do nothing","error","tile", "pad"],
                    display_name="on size mismatch",
                    default="error",
                    tooltip="How to handle mismatched layer counts. For models, this usually defaults to broadcast (zero for missing layers)."
                ),
                MrmthStack.Input(id="stack", tooltip="Access stack between nodes",optional=True)
            ],
            outputs=[
                io.Model.Output(),
                MrmthStack.Output(),

            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Expression, V, F, length_mismatch="tile",stack={}):
        return checkLazyNew(Expression,V,F)

    @classmethod
    def execute(cls, V, F, Expression, length_mismatch="tile",stack={}) -> io.NodeOutput:
        # Determine reference model for cloning
        a = V.get("V0")
        stack = copy.deepcopy(stack) if stack is not None else {}

        if a is None:
            # Try finding first valid model
            for m in V.values():
                if m is not None:
                     a = m
                     break
        if a is None:
            raise ValueError("At least one input model is required.")

        layer_count = V.get("V0").model.state_dict().__len__() if hasattr(V.get("V0"), "model") and hasattr(V.get("V0").model, "state_dict") else 0
        pbar = comfy.utils.ProgressBar(layer_count)



        aliases = {"a": "V0", "b": "V1", "c": "V2", "d": "V3", "w": "F0", "x": "F1", "y": "F2", "z": "F3"}
        patches = calculate_patches_autogrow(Expression, V=V, F=F,pbar=pbar, mapping=aliases,stack=stack)

        out_model = a.clone()
        if patches:
            out_model.add_patches(patches, 1.0, 1.0)
        return (out_model,stack)
