from comfy_api.latest import io
import torch

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
                io.String.Output()
            ],
        )

    @classmethod
    def execute(cls, script):
        return (script,)
