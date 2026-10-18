from comfy_api.latest import io
from .helper_functions import parse_expr
from .ParseTree import MrmthParseTree
from .Parser.dead_code import remove_dead_code

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
        return (remove_dead_code(parse_expr(script)),)
