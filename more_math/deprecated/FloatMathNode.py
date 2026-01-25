from inspect import cleandoc

from ..helper_functions import parse_expr
from ..Parser.UnifiedMathVisitor import UnifiedMathVisitor

from ..helper_functions import commonLazy
from comfy_api.latest import io


class FloatMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Floats.

    Inputs:
        a, b, c, d: Floats, bound to variables with the same name.
        w, x, y, z: Floats, bound to variables of the expression.
        FloatFunc: String, describing math expression.
                   Valid functions: sin, cos, tan, abs, sqrt, min, max, norm, etc.
                   Operators: +, -, *, /, ^, %.
                   Constants: e, pi.

    Outputs:
        FLOAT: The result of evaluating the math expression.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_FloatMathNode",
            display_name="Float math",
            inputs=[
                io.Float.Input(id="a", force_input=True),
                io.Float.Input(id="b", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="c", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="d", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="FloatFunc", default="a*(1-w)+b*w", tooltip="Expression to use on inputs"),
            ],
            outputs=[
                io.Float.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, FloatFunc, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0,):
        return commonLazy(FloatFunc, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, FloatFunc, a, b=0.0, c=0.0, d=0.0, w=0.0, x=0.0, y=0.0, z=0.0):

        variables = {
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            "w": w, "x": x, "y": y, "z": z
        }
        tree = parse_expr(FloatFunc);
        visitor = UnifiedMathVisitor(variables, [1])
        result = visitor.visit(tree)
        return (result,)
