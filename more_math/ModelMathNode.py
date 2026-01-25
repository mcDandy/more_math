from inspect import cleandoc
from comfy_api.latest import io
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
import re


class ModelMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Model weights (state_dict) using Autogrow inputs.
    Functionally acts as a custom model merge.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_ModelMathNode",
            display_name="Model Math",
            category="More math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Model.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.String.Input(id="Expression", default="I0*(1-F0)+I1*F0", tooltip="Expression to apply on weights"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["error", "passthrough", "pad"],
                    default="error",
                    tooltip="How to handle mismatched layer counts. For models, this usually defaults to broadcast (zero for missing layers)."
                )
            ],
            outputs=[
                io.Model.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Expression, V, F, length_mismatch="tile"):

        input_stream = InputStream(Expression)
        lexer = MathExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()

        # Support aliases
        aliases_img = {"a": "V0", "b": "V1", "c": "V2", "d": "V3"}
        aliases_flt = {"w": "F0", "x": "F1", "y": "F2", "z": "F3"}

        needed = []
        needed1 = []
        for token in filter(lambda t: t.type == MathExprParser.VARIABLE, stream.tokens):
            var_name = token.text

            if re.match(r"[VF][0-9]+", var_name):
                needed.append(var_name)
            elif var_name in aliases_img:
                needed.append(aliases_img[var_name])
            elif var_name in aliases_flt:
                needed.append(aliases_flt[var_name])
        for v in needed:
            if v.startswith("V"):
                if v not in V or V[v] is None:
                    needed1.append(v)
            elif v.startswith("F"):
                if v not in F or F[v] is None:
                    needed1.append(v)
        return needed1

    @classmethod
    def execute(cls, V, F, Expression, length_mismatch="tile") -> io.NodeOutput:
        # Determine reference model for cloning
        a = V.get("V0")
        if a is None:
            # Try finding first valid model
            for m in V.values():
                if m is not None:
                     a = m
                     break
        if a is None:
            raise ValueError("At least one input model is required.")

        # Prepare variables
        # V0..V3 map to a..d for backward compatibility in calculate_patches

        # Note: calculate_patches usually takes specific args. We might need to update it to support dynamic V/F or just pass everything.
        # Looking at Step 34, calculate_patches signature: (Model, a, b, c, d, w, x, y, z)
        # We need to verify if calculate_patches handles V/F. It probably doesn't.
        # We should check 'modelLikeCommon.py' to see if update is needed.

        # Assume for now we pass a,b,c,d,w,x,y,z as standard. 
        # But for full autogrow support (more than 4 inputs), calculate_patches needs update.
        # The prompt didn't explicitly ask to update modelLikeCommon, but "switch to Autogrow" implies full functionality.
        # I'll check modelLikeCommon.py after this block. 
        # For now, I will pass V and F to calculate_patches if I modify it, or I will stick to legacy args if I don't modify it.
        # However, to support V4+, I MUST modify calculate_patches.

        # Let's pass the V and F dicts to a modified calculate_patches, or overload it.
        # I will update modelLikeCommon.py as part of this task.

        from .modelLikeCommon import calculate_patches_autogrow

        # Map inputs to patchers if needed (Model.Input gives Model wrapper, need state_dict source?)
        # ModelMathNode inputs are Model wrappers (comfy.model_patcher.ModelPatcher).
        # So V items are ready to be used.

        aliases = {"a": "V0", "b": "V1", "c": "V2", "d": "V3", "w": "F0", "x": "F1", "y": "F2", "z": "F3"}
        patches = calculate_patches_autogrow(Expression, V=V, F=F, mapping=aliases)

        out_model = a.clone()
        if patches:
            out_model.add_patches(patches, 1.0, 1.0)
        return (out_model,)
