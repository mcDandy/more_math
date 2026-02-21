import antlr4
from comfy_api.latest import io

@io.comfytype(io_type="PARSER")
class MrmthParseTree(io.ComfyTypeIO):
    Type = antlr4.Parser  # Python type hint

    class Input(io.Input):
        def __init__(self, id: str, **kwargs):
            super().__init__(id, **kwargs)

    class Output(io.Output):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
