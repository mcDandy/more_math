from inspect import cleandoc
import torch

from .helper_functions import parse_expr, get_v_variable, checkLazyNew
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor

from comfy_api.latest import io
from .Stack import MrmthStack
from .ParseTree import MrmthParseTree
import copy


class FloatMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Floats.

    Inputs:
        V: Autogrow float inputs (V0, V1, ...)
        FloatFunc: String, describing math expression.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_FloatMathNode",
            category="More math",
            display_name="Float math",
            inputs=[
                io.Autogrow.Input(
                    id="V",
                    template=io.Autogrow.TemplatePrefix(
                        io.Float.Input("values"), prefix="V", min=1, max=50
                    ),
                ),
                io.MultiType.Input(
                    io.String.Input("FloatFunc", default="a*(1-w)+b*w", multiline=False),
                    types=[io.String, MrmthParseTree],
                    tooltip="Expression to use on inputs",
                ),
                io.Bool.Input(
                    id="remember_stack",
                    default=False,
                    display_name="Remember stack across batch",
                    tooltip=(
                        "If enabled, stack is copied at output leading to changes being remembered during batch operations (node runs multiple times in sucession). If disabled each batch gets it's own copy of the stack."
                    ),
                ),
                MrmthStack.Input(
                    id="stack", tooltip="Access stack between nodes", optional=True
                ),
            ],
            outputs=[
                io.Float.Output(),
                MrmthStack.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, FloatFunc, V, remember_stack=False, stack={}):
        # remember_stack ani stack nemění lazy logiku
        return checkLazyNew(FloatFunc, V, V)

    @classmethod
    def execute(cls, FloatFunc, V, remember_stack=False, stack={}):
        work_stack = stack if remember_stack else (copy.deepcopy(stack) if stack is not None else {})

        variables = {}
        # Populate aliases
        variables["a"] = V.get("V0", 0.0)
        variables["b"] = V.get("V1", 0.0)
        variables["c"] = V.get("V2", 0.0)
        variables["d"] = V.get("V3", 0.0)
        variables["w"] = V.get("V4", 0.0)
        variables["x"] = V.get("V5", 0.0)
        variables["y"] = V.get("V6", 0.0)
        variables["z"] = V.get("V7", 0.0)

        # Populate all V inputs
        for k, val in V.items():
            variables[k] = val if val is not None else 0.0

        v_stacked, v_cnt = get_v_variable(variables)
        if v_stacked is not None:
            variables["V"] = v_stacked
            variables["Vcnt"] = float(v_cnt)
            variables["V_count"] = float(v_cnt)

        tree = None
        if isinstance(FloatFunc, str):
            tree = parse_expr(FloatFunc)
        else:
            tree = FloatFunc
        # scalar execution
        visitor = UnifiedMathVisitor(variables, [1], state_storage=work_stack)
        result = visitor.visit(tree)

        # Result might be float or tensor(scalar)
        if torch.is_tensor(result):
            result = result.flatten()[0].item()
        returned_stack = work_stack if remember_stack else copy.deepcopy(work_stack)
        return (float(result), returned_stack)