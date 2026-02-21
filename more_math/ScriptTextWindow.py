from comfy_api.latest import io
import torch
from .helper_functions import parse_expr
from .ParseTree import MrmthParseTree

class ScriptTextInput(io.ComfyNode):

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ScriptInput",
            category="More math",
            display_name="Script input",
            inputs=[
                io.String.Input(id="script", multiline=True),
            ],
            outputs=[
                MrmthParseTree.Output()
            ],
        )

    @classmethod
    def execute(cls, script):
        expr = parse_expr(script)
        return (expr,)
