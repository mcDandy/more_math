from .helper_functions import (
    parse_expr,
    get_v_variable,
    get_f_variable,
    checkLazyNew
)
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io
import torch
from .Stack import MrmthStack
import copy
from .ParseTree import MrmthParseTree

class StringMathNode(io.ComfyNode):
    """
    Enables math expressions on Audio.

    Inputs:
        I: Autogrow image inputs (I0, I1, ...)
        F: Autogrow float inputs (F0, F1, ...)
        Image: Expression
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_AudioMathNode",
            category="More math",
            display_name="Audio math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.String.Input("values", optional=True), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.MultiType.Input(
                    io.String.Input("Expression", default="", multiline=False),
                    types=[io.String,MrmthParseTree],
                    tooltip="3D model file or path string",
                ),
                io.Int.Input(id="batching", default=0),
                io.Boolean.Input(
                    id="remember_stack",
                    default=False,
                    display_name="Remember stack across batch",
                    tooltip=(
                        "If enabled, stack is copied at output leading to changes being remembered during batch operations (node runs multiple times in sucession). If disabled each batch gets it's own copy of the stack."
                    ),
                ),
                MrmthStack.Input(id="stack", tooltip="Access stack between nodes",optional=True)
            ],
            outputs=[
                io.Audio.Output(is_output_list=True),
                MrmthStack.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Expression, V, F,batching=0, remember_stack=False,stack={}):
        return checkLazyNew(Expression,V,F)


    @classmethod
    def execute(cls, V, F, Expression, batching=0, remember_stack=False, stack={}):

        variables = {
            "a": V.get(0,""), "b": V.get(1,""), "c": V.get(2,""), "d": V.get(3,""),
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0
        }

        v_stacked, v_cnt = get_v_variable(V, length_mismatch="do nothing")
        if v_stacked is not None:
             variables["V"] = v_stacked
             variables["Vcnt"] = float(v_cnt)
             variables["V_count"] = float(v_cnt)

        f_stacked, f_cnt = get_f_variable(F)
        if f_stacked is not None:
             variables["F"] = f_stacked
             variables["Fcnt"] = float(f_cnt)
             variables["F_count"] = float(f_cnt)

        for k, val in F.items():
            variables[k] = val if val is not None else 0.0

        tree = None
        if isinstance(Expression,str):
            tree = parse_expr(Expression)
        else:
            tree = Expression
        visitor = UnifiedMathVisitor(variables, len(V[0]),torch.device("cpu"),state_storage=stack)
        result = visitor.visit(tree)
        result = str(result)

        if batching and batching > 0:
            def chunks(s, n):
                """Produce `n`-character chunks from `s`."""
                for start in range(0, len(s), n):
                    yield s[start:start+n]

            stack = stack if remember_stack else copy.deepcopy(stack)
            return (chunks(result,batching), stack)
        else:
            stack = stack if remember_stack else copy.deepcopy(stack)

            return (result, stack)
