"""Color math node using integer color representation."""

from __future__ import annotations


from comfy_api.latest import io



class mintest(io.ComfyNode):
    """Apply expression math to Color values converted to packed RGB integers."""

    @classmethod
    def define_schema(cls) -> io.Schema:
        """Define node schema."""
        return io.Schema(
            node_id="mrmth_ag_mintest",
            category="More math",
            display_name="Minimal test",
            inputs=[
                io.Autogrow.Input(id="V", template=io.Autogrow.TemplatePrefix(io.Color.Input("values"), prefix="V", min=1, max=50)),
            ],
            outputs=[
                io.Color.Output(id="color"),
            ],
        )


    @classmethod
    def execute(
        cls,
        V
    ):
        """Execute color expression and return resulting color."""
        print(V)
        return V["V0"]
