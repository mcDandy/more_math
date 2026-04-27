class StackUnBatcher:
      @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_StackUnBatcher",
            category="More math",
            display_name="Stack UnBatcher",
            inputs=[
                io.Stack.Input(id="stack", tooltip="Input stack to unbatch"),
            ],
            outputs=[
                io.Stack.Output(id="unbatched", tooltip="Unbatched stack output"),
            ],´ú