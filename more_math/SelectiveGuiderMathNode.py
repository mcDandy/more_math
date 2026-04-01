import copy
import torch
import comfy.model_patcher
from comfy_api.latest import io
import comfy.hooks
import logging
import comfy.patcher_extension

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
        hit_flags = {"attn": False, "dit": False}
        
        # Lokální stav pro sledování aktuálního timestepu přes všechny volání hooků
        step_states = {
            "attn1": {"ts": None, "hit": False},
            "attn2": {"ts": None, "hit": False},
            "dit_block": {"ts": None, "hit": False},
        }

        def is_after_phase() -> bool:
            return hook_when in ("after_all", "after_x", "just_after_x")

        def resolve_x(total_blocks: int | None) -> int:
            x = int(layer_x)
            if x < 0 and total_blocks is not None:
                x = total_blocks + x
            if total_blocks is not None:
                x = max(0, min(x, total_blocks - 1))
            return x

        def match_index(idx: int, total_blocks: int | None, stage: str, topts: dict, hook_kind: str) -> bool:
            if hook_when == "before_all":
                ts_val = topts.get("sigmas")
                try:
                    if torch.is_tensor(ts_val) and ts_val.numel() > 0:
                        ts = float(ts_val[0].item())
                    elif isinstance(ts_val, (list, tuple)) and len(ts_val) > 0:
                        ts = float(ts_val[0])
                    else:
                        ts = float(ts_val)
                except:
                    ts = -999.0

                # Zkontroluj, jestli už byl operátor v tomto timestepu a pro daný druh aplikován
                state = step_states.setdefault(hook_kind, {"ts": None, "hit": False})
                if state["ts"] != ts:
                    state["ts"] = ts
                    state["hit"] = False

                if not state["hit"]:
                    state["hit"] = True
                    return True
                return False
            
            if hook_when == "after_all":
                # U after_all nelze 100% předpovědět finální krok bez plného grafu, pofallbackujeme na indexování
                if total_blocks is not None:
                    return idx == (total_blocks - 1)
                else: 
                    return stage == "output" and idx >= 8

            x = resolve_x(total_blocks)
            if hook_when == "before_x":
                return idx < x
            if hook_when == "just_before_x":
                return idx == (x - 1 if x > 0 else 0)
            if hook_when == "just_after_x":
                return idx == x
            return idx > x

        def target_indices():
            if hook_when in ("before_all", "after_all", "before_x", "after_x"):
                return range(0, MAX_HOOK_INDEX + 1)
            if int(layer_x) < 0:
                return range(0, MAX_HOOK_INDEX + 1)
            if hook_when == "just_before_x":
                return [max(0, int(layer_x) - 1)]
            if hook_when == "just_after_x":
                return [int(layer_x)]
            return [int(layer_x)]

        def side_from_cond_or_uncond(cond_or_uncond):
            if isinstance(cond_or_uncond, (list, tuple)) and len(cond_or_uncond) > 0:
                vals = list(cond_or_uncond)
                uniq = set(vals)
                if len(uniq) == 1:
                    idx = int(vals[0])
                    if idx == 0:
                        return ("positive", 0)
                    if idx == 1:
                        return ("negative", 1)
                return ("mixed", -1)
            return ("unknown", -1)

        def run_expr(inp: torch.Tensor, extra_vars: dict | None = None) -> torch.Tensor:
            variables = {
                "inp": inp,
                "sample": inp,
                "hook_kind": "unknown",
                "block_name": "",
                "layer_key": "",
                "layer_id": -1.0,
                "layer": -1.0,
                "i": -1.0,
                "total_blocks": -1.0,
                "has_qkv": 0.0,
                "q": inp,
                "k": inp,
                "v": inp,
                "heads": 0.0,
                "dim_head": 0.0,
                "cond_side": "unknown",
                "cond_index": -1.0,
                "is_positive": 0.0,
                "is_negative": 0.0,
            } | generate_dim_variables(inp)

            if extra_vars:
                variables.update(extra_vars)

            for kf, vf in F.items():
                variables[kf] = vf if vf is not None else 0.0

            visitor = UnifiedMathVisitor(variables, inp.shape, inp.device, state_storage=stack)
            out = visitor.visit(tree)
            return as_tensor(out, inp.shape).to(inp.device)

        def register_dit(patched_dict, forced_side=None):
            topts = patched_dict["transformer_options"]

            def dit_wrap(args, extra_args):
                idx = int(args.get("transformer_options", {}).get("block_index", -1))
                total_blocks = args.get("transformer_options", {}).get("total_blocks", None)

                if not match_index(idx, total_blocks, "dit", args.get("transformer_options", {}), "dit_block"):
                    return extra_args["original_block"](args)
                if not hit_flags["dit"]:
                  logging.warning(f"[SelectiveGuiderMathNode] DIT HIT idx={idx} total={total_blocks}")
                  hit_flags["dit"] = True
                btype = args.get("transformer_options", {}).get("block_type", "dit")
                co = args.get("transformer_options", {}).get("cond_or_uncond", None)
                auto_side, auto_idx = side_from_cond_or_uncond(co)
                side = forced_side if forced_side is not None else auto_side
                idx_side = 0 if side == "positive" else (1 if side == "negative" else auto_idx)

                meta = {
                    "hook_kind": "dit_block",
                    "layer_id": float(idx),
                    "layer": float(idx),
                    "i": float(idx),
                    "total_blocks": float(total_blocks) if total_blocks is not None else -1.0,
                    "block_name": btype,
                    "layer_key": f"dit.{btype}.{idx}",
                    "has_qkv": 0.0,
                    "cond_side": side,
                    "cond_index": float(idx_side),
                    "is_positive": 1.0 if side == "positive" else 0.0,
                    "is_negative": 1.0 if side == "negative" else 0.0,
                }

                if not is_after_phase():
                    args2 = dict(args)
                    args2["img"] = run_expr(args["img"], meta)
                    return extra_args["original_block"](args2)

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
            patched_dict["transformer_options"] = topts

        def register_attn(patched_dict, attn_name: str, forced_side=None):
            topts = patched_dict["transformer_options"].copy()

            def attn_override(original_attn, q, k, v, heads, **kwargs):
                transformer_options = kwargs.get("transformer_options", {})

                blk = transformer_options.get("block", None)  # ("input"/"middle"/"output", idx)
                if isinstance(blk, (tuple, list)) and len(blk) >= 2:
                    stage = str(blk[0])
                    layer_id = int(blk[1])
                else:
                    stage = "unknown"
                    layer_id = int(transformer_options.get("block_index", -1))

                idx = layer_id
                total_blocks = None

                if not match_index(idx, total_blocks, stage, transformer_options, attn_name):
                    return original_attn(q, k, v, heads, **kwargs)

                co = transformer_options.get("cond_or_uncond", None)
                auto_side, auto_idx = side_from_cond_or_uncond(co)
                side = forced_side if forced_side is not None else auto_side
                idx_side = 0 if side == "positive" else (1 if side == "negative" else auto_idx)

                if not hit_flags["attn"]:
                    logging.warning(f"[SelectiveGuiderMathNode] ATTN HIT stage={stage} layer_id={layer_id} side={side}")
                    hit_flags["attn"] = True

                meta = {
                    "hook_kind": attn_name,
                    "block_name": stage,
                    "layer_id": float(layer_id),
                    "layer": float(layer_id),
                    "i": float(layer_id),
                    "total_blocks": -1.0,
                    "has_qkv": 1.0,
                    "q": q,
                    "k": k,
                    "v": v,
                    "heads": float(heads),
                    "dim_head": float(q.shape[-1] // heads) if heads > 0 else 0.0,
                    "layer_key": f"{stage}.{layer_id}.{attn_name}",
                    "cond_side": side,
                    "cond_index": float(idx_side),
                    "is_positive": 1.0 if side == "positive" else 0.0,
                    "is_negative": 1.0 if side == "negative" else 0.0,
                }

                if not is_after_phase():
                    q2 = run_expr(q, meta)
                    return original_attn(q2, k, v, heads, **kwargs)

                out = original_attn(q, k, v, heads, **kwargs)
                return run_expr(out, meta)

            topts["optimized_attention_override"] = attn_override
            patched_dict["transformer_options"] = topts
            return patched_dict

        def build_transformers_for_side(side_label=None):
            p = comfy.model_patcher.create_model_options_clone(V.model_options)
            p.setdefault("transformer_options", {})
            if hook_target in ("all", "dit_block"):
                register_dit(p, forced_side=side_label)
            if hook_target in ("all", "attn1"):
                p = register_attn(p, "attn1", forced_side=side_label)
            if hook_target in ("all", "attn2"):
                p = register_attn(p, "attn2", forced_side=side_label)
            return p["transformer_options"]

        def attach_side_hook(side_name: str):
            if not hasattr(V, "original_conds") or side_name not in V.original_conds:
                return
            tdict = build_transformers_for_side(side_name)
            hook = comfy.hooks.TransformerOptionsHook(
                transformers_dict=tdict,
                hook_scope=comfy.hooks.EnumHookScope.HookedOnly,
            )
            hg = comfy.hooks.HookGroup()
            hg.add(hook)

            new_conds = []
            for c in V.original_conds[side_name]:
                cc = c.copy()
                old = cc.get("hooks", None)
                cc["hooks"] = comfy.hooks.HookGroup.combine_all_hooks([old, hg])
                new_conds.append(cc)
            V.original_conds[side_name] = new_conds

        if hasattr(V, "original_conds"):
            attach_side_hook("positive")
            attach_side_hook("negative")
            logging.warning(f"[SelectiveGuiderMathNode] has original_conds: {list(V.original_conds.keys())}")
            for side in ("positive", "negative"):
                if side in V.original_conds:
                    cnt = sum(1 for c in V.original_conds[side] if c.get("hooks", None) is not None)
                    logging.warning(f"[SelectiveGuiderMathNode] side={side} conds_with_hooks={cnt}/{len(V.original_conds[side])}")
        else:
            patched = comfy.model_patcher.create_model_options_clone(V.model_options)
            patched.setdefault("transformer_options", {})
            if hook_target in ("all", "dit_block"):
                register_dit(patched, forced_side=None)
            if hook_target in ("all", "attn1"):
                patched = register_attn(patched, "attn1", forced_side=None)
            if hook_target in ("all", "attn2"):
                patched = register_attn(patched, "attn2", forced_side=None)
            V.model_options = patched

        if hasattr(V, "model_patcher") and V.model_patcher is not None and not getattr(V, "_mrmth_debug_callbacks_added", False):
            def _on_register_all_hook_patches(model_patcher, hooks, target_dict, model_options, registered):
                try:
                    reg_len = len(registered) if registered is not None else 0
                    in_len = len(hooks) if hooks is not None else 0
                    tr_count = len(registered.get_type(comfy.hooks.EnumHookType.TransformerOptions)) if registered is not None else 0
                    logging.warning(f"[SelectiveGuiderMathNode] REGISTER hooks_in={in_len} registered={reg_len} transformer_registered={tr_count}")
                    if model_options is not None:
                        rh = model_options.get("registered_hooks", None)
                        logging.warning(f"[SelectiveGuiderMathNode] model_options.registered_hooks={'set' if rh is not None else 'None'}")
                except Exception as e:
                    logging.warning(f"[SelectiveGuiderMathNode] REGISTER debug error: {e}")

            def _on_apply_hooks(model_patcher, hooks):
                try:
                    hl = len(hooks) if hooks is not None else 0
                    logging.warning(f"[SelectiveGuiderMathNode] APPLY hooks_len={hl}")
                except Exception as e:
                    logging.warning(f"[SelectiveGuiderMathNode] APPLY debug error: {e}")

            V.model_patcher.add_callback_with_key(
                comfy.patcher_extension.CallbacksMP.ON_REGISTER_ALL_HOOK_PATCHES,
                "mrmth_selective_debug",
                _on_register_all_hook_patches,
            )
            V.model_patcher.add_callback_with_key(
                comfy.patcher_extension.CallbacksMP.ON_APPLY_HOOKS,
                "mrmth_selective_debug",
                _on_apply_hooks,
            )
            V._mrmth_debug_callbacks_added = True

        stack = stack if remember_stack else copy.deepcopy(stack)
        # do execute(), před register_*:
        return (V, stack)