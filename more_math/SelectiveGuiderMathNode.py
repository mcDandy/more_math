import copy
import torch
import comfy.model_patcher
from comfy_api.latest import io

from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from .helper_functions import checkLazyNew, generate_dim_variables, parse_expr, as_tensor
from .Stack import MrmthStack
from .ParseTree import MrmthParseTree
from comfy.ldm.modules.attention import optimized_attention


class SelectiveGuiderMathNode(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_SelectiveGuiderMathNode",
            category="More math",
            display_name="Selective guider math",
            inputs=[
                io.Guider.Input("V"),
                io.Autogrow.Input(
                    id="F",
                    template=io.Autogrow.TemplatePrefix(
                        io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True),
                        prefix="F",
                        min=1,
                        max=50,
                    ),
                ),
                io.MultiType.Input(
                    io.String.Input("Expression", default="push(0, inp); inp", multiline=False),
                    types=[io.String, MrmthParseTree]
                ),
                io.Combo.Input(
                    id="hook_target",
                    options=["all", "dit_block", "attn1", "attn2"],
                    default="all",
                ),
                io.Combo.Input(
                    id="hook_when",
                    options=["before_x", "just_before_x", "just_after_x", "after_x"],
                    default="after_x",
                ),
                io.Int.Input(id="layer_x", default=0, min=-999, max=999),
                io.Boolean.Input(id="remember_stack", default=False),
                MrmthStack.Input(id="stack", optional=True),
            ],
            outputs=[io.Guider.Output(), MrmthStack.Output()],
        )

    @classmethod
    def check_lazy_status(
        cls,
        V,
        F,
        Expression,
        hook_target="all",
        hook_when="after_x",
        layer_x=0,
        remember_stack=False,
        stack={},
    ):
        return checkLazyNew(Expression, {}, F)

    @classmethod
    def execute(
        cls,
        V,
        F,
        Expression,
        hook_target="all",
        hook_when="after_x",
        layer_x=0,
        remember_stack=False,
        stack=None,
    ):
        if V is None or not hasattr(V, "model_options"):
            raise ValueError("Vstupní guider musí mít model_options.")

        stack = stack if remember_stack else (copy.deepcopy(stack) if stack is not None else {})
        tree = parse_expr(Expression) if isinstance(Expression, str) else Expression

        def match_when(idx: int, total_blocks: int | None = None) -> bool:
            x = int(layer_x)

            # záporné indexy od konce
            if x < 0 and total_blocks is not None:
                x = total_blocks + x  # -1 => last

            # clamp
            if total_blocks is not None:
                x = max(0, min(x, total_blocks - 1))

            if hook_when == "before_x":
                return idx < x
            if hook_when == "just_before_x":
                # pro x==0 zůstane 0 (užitečné chování místo -1)
                return idx == (x - 1 if x > 0 else 0)
            if hook_when == "just_after_x":
                return idx == x
            return idx >= x  # after_x

        def run_expr(inp: torch.Tensor) -> torch.Tensor:
            stack["hook_last_inp"] = inp.detach()

            variables = {
                "inp": inp,
                "sample": inp,
            } | generate_dim_variables(inp)

            for k, v in F.items():
                variables[k] = v if v is not None else 0.0

            visitor = UnifiedMathVisitor(variables, inp.shape, inp.device, state_storage=stack)
            out = visitor.visit(tree)
            return as_tensor(out, inp.shape).to(inp.device)

        patched = comfy.model_patcher.create_model_options_clone(V.model_options)
        patched.setdefault("transformer_options", {})

        def register_dit():
            topts = patched["transformer_options"]

            def dit_wrap(args, extra_args):
                idx = int(args.get("transformer_options", {}).get("block_index", -1))
                total_blocks = args.get("transformer_options", {}).get("total_blocks", None)
                if not match_when(idx, total_blocks):
                    return extra_args["original_block"](args)

                args2 = dict(args)
                args2["img"] = run_expr(args["img"])
                return extra_args["original_block"](args2)

            patches_replace = topts.get("patches_replace", {}).copy()
            dit_map = patches_replace.get("dit", {}).copy()
            dit_map[("double_block", int(layer_x))] = dit_wrap
            dit_map[("single_block", int(layer_x))] = dit_wrap
            patches_replace["dit"] = dit_map
            topts["patches_replace"] = patches_replace
            patched["transformer_options"] = topts

        def register_attn(attn_name: str):

            def attn_replace(q, k, v, extra_options):
                idx = int(extra_options.get("block_index", -1))
                total_blocks = extra_options.get("total_blocks", None)
                if not match_when(idx, total_blocks):
                    return optimized_attention(q, k, v, extra_options["n_heads"], transformer_options=extra_options)

                q2 = run_expr(q)
                return optimized_attention(q2, k, v, extra_options["n_heads"], transformer_options=extra_options)

            nonlocal patched
            for blk in ("input", "middle", "output"):
                patched = comfy.model_patcher.set_model_options_patch_replace(
                    patched,
                    attn_replace,
                    attn_name,
                    blk,
                    int(layer_x),
                )

        if hook_target in ("all", "dit_block"):
            register_dit()
        if hook_target in ("all", "attn1"):
            register_attn("attn1")
        if hook_target in ("all", "attn2"):
            register_attn("attn2")

        V.model_options = patched

        stack = stack if remember_stack else copy.deepcopy(stack)
        return (V, stack)