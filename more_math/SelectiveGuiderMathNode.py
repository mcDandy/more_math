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
                    types=[io.String, MrmthParseTree],
                ),
                io.DynamicCombo.Input("hook_mode_cfg", options=[
                    io.DynamicCombo.Option("single_target", [
                        io.Combo.Input("hook_target", options=["dit_block", "attn1", "attn2"], default="attn1"),
                        io.DynamicCombo.Input("hook_pos", options=[
                            io.DynamicCombo.Option("before_all", []),
                            io.DynamicCombo.Option("after_all", []),
                            io.DynamicCombo.Option("relative", [
                                io.Combo.Input(
                                    "hook_when",
                                    options=["before_x", "just_before_x", "just_after_x", "after_x"],
                                    default="after_x",
                                ),
                                io.Int.Input("layer_x", default=0, min=-999, max=999),
                            ]),
                        ]),
                    ]),
                    io.DynamicCombo.Option("all_targets", [
                        io.Combo.Input(
                            "hook_when",
                            options=["before_x", "just_before_x", "just_after_x", "after_x"],
                            default="after_x",
                        ),
                        io.Int.Input("layer_x", default=0, min=-999, max=999),
                    ]),
                ]),
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
        hook_mode_cfg={},
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
        hook_mode_cfg,
        remember_stack=False,
        stack=None,
    ):
        if V is None or not hasattr(V, "model_options"):
            raise ValueError("Vstupní guider musí mít model_options.")

        # DynamicCombo -> interní config
        mode = hook_mode_cfg.get("hook_mode_cfg", "all_targets")
        if mode == "single_target":
            hook_target = hook_mode_cfg.get("hook_target", "attn1")
            hook_pos = hook_mode_cfg.get("hook_pos", "relative")
            if hook_pos in ("before_all", "after_all"):
                hook_when = hook_pos
                layer_x = 0
            else:
                hook_when = hook_mode_cfg.get("hook_when", "after_x")
                layer_x = int(hook_mode_cfg.get("layer_x", 0))
        else:
            hook_target = "all"
            hook_when = hook_mode_cfg.get("hook_when", "after_x")
            layer_x = int(hook_mode_cfg.get("layer_x", 0))

        stack = stack if remember_stack else (copy.deepcopy(stack) if stack is not None else {})
        tree = parse_expr(Expression) if isinstance(Expression, str) else Expression

        MAX_HOOK_INDEX = 999

        def is_after_phase() -> bool:
            return hook_when in ("after_all", "after_x", "just_after_x")

        def resolve_x(total_blocks: int | None) -> int:
            x = int(layer_x)
            if x < 0 and total_blocks is not None:
                x = total_blocks + x  # -1 => last
            if total_blocks is not None:
                x = max(0, min(x, total_blocks - 1))
            return x

        def match_index(idx: int, total_blocks: int | None = None) -> bool:
            if hook_when == "before_all":
                return idx == 0
            if hook_when == "after_all":
                return total_blocks is not None and idx == (total_blocks - 1)

            x = resolve_x(total_blocks)

            if hook_when == "before_x":
                return idx < x
            if hook_when == "just_before_x":
                return idx == (x - 1 if x > 0 else 0)
            if hook_when == "just_after_x":
                return idx == x
            return idx > x  # after_x

        def target_indices():
            # full range režimy
            if hook_when in ("before_all", "after_all", "before_x", "after_x"):
                return range(0, MAX_HOOK_INDEX + 1)

            # záporné indexy bez total_blocks při registraci
            if int(layer_x) < 0:
                return range(0, MAX_HOOK_INDEX + 1)

            # just_* optimalizace
            if hook_when == "just_before_x":
                return [max(0, int(layer_x) - 1)]
            if hook_when == "just_after_x":
                return [int(layer_x)]

            return [int(layer_x)]

        def run_expr(inp: torch.Tensor, extra_vars: dict | None = None) -> torch.Tensor:
            # universal defaults: always defined
            variables = {
                "inp": inp,
                "sample": inp,

                # hook identity
                "hook_kind": "unknown",
                "block_name": "",
                "layer_key": "",
                "layer_id": -1.0,
                "i": -1.0,
                "total_blocks": -1.0,

                # attention-related (always present, valid flag says if real)
                "has_qkv": 0.0,
                "q": inp,
                "k": inp,
                "v": inp,
                "heads": 0.0,
                "dim_head": 0.0,
            } | generate_dim_variables(inp)

            if extra_vars:
                variables.update(extra_vars)

            for kf, vf in F.items():
                variables[kf] = vf if vf is not None else 0.0

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

                if not match_index(idx, total_blocks):
                    return extra_args["original_block"](args)

                btype = args.get("transformer_options", {}).get("block_type", "dit")
                meta = {
                    "hook_kind": "dit_block",
                    "layer_id": float(idx),
                    "i": float(idx),
                    "total_blocks": float(total_blocks) if total_blocks is not None else -1.0,
                    "block_name": btype,
                    "layer_key": f"dit.{btype}.{idx}",
                    "has_qkv": 0.0,
                }

                # BEFORE
                if not is_after_phase():
                    args2 = dict(args)
                    args2["img"] = run_expr(args["img"], meta)
                    return extra_args["original_block"](args2)

                # AFTER
                out = extra_args["original_block"](args)
                if isinstance(out, dict) and "img" in out:
                    out2 = dict(out)
                    out2["img"] = run_expr(out["img"], meta)
                    return out2
                return out

            patches_replace = topts.get("patches_replace", {}).copy()
            dit_map = patches_replace.get("dit", {}).copy()
            for li in target_indices():
                dit_map[("double_block", li)] = dit_wrap
                dit_map[("single_block", li)] = dit_wrap
            patches_replace["dit"] = dit_map
            topts["patches_replace"] = patches_replace
            patched["transformer_options"] = topts

        def register_attn(attn_name: str):
            def make_attn_replace(block_name: str):
                def attn_replace(q, k, v, extra_options):
                    idx = int(extra_options.get("block_index", -1))
                    total_blocks = extra_options.get("total_blocks", None)

                    if not match_index(idx, total_blocks):
                        return optimized_attention(q, k, v, extra_options["n_heads"], transformer_options=extra_options)

                    meta = {
                        "hook_kind": attn_name,
                        "block_name": block_name,
                        "layer_id": float(idx),
                        "i": float(idx),
                        "total_blocks": float(total_blocks) if total_blocks is not None else -1.0,
                        "has_qkv": 1.0,

                        "q": q,
                        "k": k,
                        "v": v,
                        "heads": float(extra_options.get("n_heads", 0)),
                        "dim_head": float(extra_options.get("dim_head", 0)),
                        "layer_key": f"{block_name}.{attn_name}.{idx}",
                    }

                    # BEFORE -> modify q
                    if not is_after_phase():
                        q2 = run_expr(q, meta)
                        return optimized_attention(q2, k, v, extra_options["n_heads"], transformer_options=extra_options)

                    # AFTER -> modify attn output
                    out = optimized_attention(q, k, v, extra_options["n_heads"], transformer_options=extra_options)
                    return run_expr(out, meta)
                return attn_replace

            nonlocal patched
            for blk in ("input", "middle", "output"):
                attn_replace = make_attn_replace(blk)
                for li in target_indices():
                    patched = comfy.model_patcher.set_model_options_patch_replace(
                        patched,
                        attn_replace,
                        attn_name,
                        blk,
                        li,
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