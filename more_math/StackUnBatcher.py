from comfy_api.latest import io
from .Stack import MrmthStack

class StackUnBatcher(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_StackUnBatcher",
            category="More math",
            display_name="Stack UnBatcher",
            is_input_list=True,
            inputs=[
                MrmthStack.Input(id="stack", tooltip="Input stack to unbatch"),
            ],
            outputs=[
                MrmthStack.Output(id="unbatched", tooltip="Unbatched stack output"),
            ])

    @classmethod
    def execute(cls, stack):
        return (stack[-1],)