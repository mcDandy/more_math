from inspect import cleandoc
from comfy_api.latest import io
import copy
from .helper_functions import checkLazyNew
from .Stack import MrmthStack
from .ParseTree import MrmthParseTree
from .loraDictCommon import calculate_lora_dict_autogrow


class LoraMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions directly on raw LoRA
    tensors (LORA_MODEL: dict of lora_up.weight / lora_down.weight / alpha /
    diff tensors) using Autogrow inputs.

    Unlike Model/VAE/CLIP Math, these tensors are not attached to a
    ModelPatcher, so there is no base-vs-patched distinction - the tensors
    already *are* the LoRA's deltas - and therefore no V{n}_d.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_LoraMathNode",
            display_name="Lora Math",
            category="More math",
            inputs=[
                io.Autogrow.Input(id="V", template=io.Autogrow.TemplatePrefix(io.LoraModel.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.MultiType.Input(
                    io.String.Input("Expression", default="V0", multiline=False),
                    types=[io.String, MrmthParseTree],
                    tooltip="Expression to apply on LoRA tensors",
                ),
                io.Boolean.Input(
                    id="use_compute_device",
                    default=True,
                    display_name="Move tensors to GPU",
                    tooltip="Temporarily copies LoRA tensors to the compute device for math and moves the result back afterwards.",
                ),
                MrmthStack.Input(id="stack", tooltip="Access stack between nodes", optional=True)
            ],
            outputs=[
                io.LoraModel.Output(),
                MrmthStack.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Expression, V, F, use_compute_device=True, stack={}):
        return checkLazyNew(Expression, V, F)

    @classmethod
    def execute(cls, V, F, Expression, use_compute_device=True, stack={}) -> io.NodeOutput:
        if not any(v is not None for v in V.values()):
            raise ValueError("At least one input LoRA is required.")
        stack = copy.deepcopy(stack) if stack is not None else {}

        aliases = {"a": "V0", "b": "V1", "c": "V2", "d": "V3", "w": "F0", "x": "F1", "y": "F2", "z": "F3"}
        result = calculate_lora_dict_autogrow(Expression, V=V, F=F, mapping=aliases, stack=stack, use_compute_device=use_compute_device)
        return (result, stack)
