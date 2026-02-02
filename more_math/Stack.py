from comfy_api.latest import io

@io.comfytype(io_type="STACK")
class MrmthStack(io.ComfyTypeIO):
    Type = dict  # Python type hint

    class Input(io.Input):
        def __init__(self, id: str, **kwargs):
            super().__init__(id, **kwargs)

    class Output(io.Output):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
