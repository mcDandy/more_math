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
                    io.String.Input("Expression", default="print([layer, layer_key, hook_kind, cond_side, activations_shape]); inp", multiline=False),
                    types=[io.String, MrmthParseTree],
                ),
                io.Int.Input("layer_x", default=0, min=-999, max=999),
            ],
            outputs=[io.Guider.Output(), MrmthStack.Output()],
        )

    @classmethod
    def check_lazy_status(
        cls,
        V,
        F,
        Expression,
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
        layer_x=0,
        remember_stack=False,
        stack=None,
    ):
        if V is None or not hasattr(V, "model_options"):
            raise ValueError("Vstupní guider musí mít model_options.")

        hook_target = "all"
        hook_when = "just_after_x"

        stack = stack if remember_stack else (copy.deepcopy(stack) if stack is not None else {})
        tree = parse_expr(Expression) if isinstance(Expression, str) else Expression

        MAX_HOOK_INDEX = 999
        hit_flags = {"attn1": False, "attn2": False, "dit": False, "attn_unknown": False, "unet": False}

        def resolve_attn_kind(transformer_options: dict, q: torch.Tensor | None = None, k: torch.Tensor | None = None, v: torch.Tensor | None = None) -> str:
            raw = transformer_options.get(
                "attn_name",
                transformer_options.get(
                    "attn_type",
                    transformer_options.get(
                        "block_attn",
                        transformer_options.get("transformer_index", None),
                    ),
                ),
            )

            if isinstance(raw, str):
                r = raw.lower()
                if r in ("attn1", "self", "self_attn", "self_attention"):
                    return "attn1"
                if r in ("attn2", "cross", "cross_attn", "cross_attention"):
                    return "attn2"
                return "attn_unknown"

            if isinstance(raw, (int, float)):
                if int(raw) == 0:
                    return "attn1"
                if int(raw) == 1:
                    return "attn2"

            # Fallback heuristika: self-attn má obvykle stejný zdroj pro q/k/v
            if isinstance(q, torch.Tensor) and isinstance(k, torch.Tensor) and isinstance(v, torch.Tensor):
                if (q.data_ptr() == k.data_ptr()) and (k.data_ptr() == v.data_ptr()):
                    return "attn1"
                return "attn_unknown"

            return "attn_unknown"

        def resolve_x(total_blocks: int | None) -> int:
            x = int(layer_x)
            if x < 0 and total_blocks is not None:
                x = total_blocks + x
            if total_blocks is not None:
                x = max(0, min(x, total_blocks - 1))
            return x

        def match_index(idx: int, total_blocks: int | None, stage: str, topts: dict, hook_kind: str) -> bool:
            x = resolve_x(total_blocks)
            return idx == x

        def target_indices():
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
            # v run_expr(...) rozšiř výchozí proměnné:
            variables = {
                "inp": inp,
                "sample": inp,
                "hook_kind": "unknown",
                "hook_domain": "unknown",
                "attn_kind": "none",
                "attn_mode": "unknown",
                "transformer_index": -1.0,
                "is_dit": 0.0,
                "is_unet_block": 0.0,
                "is_time_emb": 0.0,
                "is_attn1": 0.0,
                "is_attn2": 0.0,
                "is_self_attention": 0.0,
                "is_cross_attention": 0.0,
                "has_context": 0.0,
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
                "query_tokens": -1.0,
                "context_tokens": -1.0,
                "value_tokens": -1.0,
                "activations_shape": [],
                "activation_rank": -1.0,
                "activation_b": -1.0,
                "activation_c": -1.0,
                "activation_t": -1.0,
                "activation_h": -1.0,
                "activation_w": -1.0,
                "cond_side": "unknown",
                "cond_index": -1.0,
                "is_positive": 0.0,
                "is_negative": 0.0,
                "is_attn1_hook": 0.0,
                "is_attn2_hook": 0.0,
                "attention_relation": "unknown",
            } | generate_dim_variables(inp)

            if extra_vars:
                variables.update(extra_vars)

            for kf, vf in F.items():
                variables[kf] = vf if vf is not None else 0.0

            act_shape = variables.get("activations_shape", [])
            if isinstance(act_shape, (list, tuple)):
                variables["activation_rank"] = float(len(act_shape))
                if len(act_shape) >= 1:
                    variables["activation_b"] = float(act_shape[0])
                if len(act_shape) >= 2:
                    variables["activation_c"] = float(act_shape[1])
                if len(act_shape) == 4:
                    variables["activation_h"] = float(act_shape[2])
                    variables["activation_w"] = float(act_shape[3])
                elif len(act_shape) >= 5:
                    variables["activation_t"] = float(act_shape[2])
                    variables["activation_h"] = float(act_shape[3])
                    variables["activation_w"] = float(act_shape[4])

            qv = variables.get("q", inp)
            kv = variables.get("k", inp)
            vv = variables.get("v", inp)

            if variables.get("attn_kind") == "attn1":
                variables["is_attn1_hook"] = 1.0
            elif variables.get("attn_kind") == "attn2":
                variables["is_attn2_hook"] = 1.0

            if hasattr(qv, "shape") and len(qv.shape) >= 2:
                variables["query_tokens"] = float(qv.shape[-2])
            if hasattr(kv, "shape") and len(kv.shape) >= 2:
                variables["context_tokens"] = float(kv.shape[-2])
                variables["has_context"] = 1.0
            if hasattr(vv, "shape") and len(vv.shape) >= 2:
                variables["value_tokens"] = float(vv.shape[-2])

            qt = variables["query_tokens"]
            kt = variables["context_tokens"]

            if variables["has_context"] == 1.0 and qt > 0 and kt > 0:
                if qt != kt:
                    variables["is_cross_attention"] = 1.0
                    variables["is_self_attention"] = 0.0
                    variables["attention_relation"] = "cross"
                else:
                    variables["is_cross_attention"] = 0.0
                    variables["is_self_attention"] = 1.0
                    variables["attention_relation"] = "self"
            else:
                variables["is_cross_attention"] = 0.0
                variables["is_self_attention"] = 0.0
                variables["attention_relation"] = "unknown"

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
                    "hook_domain": "diffusion",
                    "attn_kind": "none",
                    "is_dit": 1.0,
                    "is_attn1": 0.0,
                    "is_attn2": 0.0,
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

        def register_attn(patched_dict, forced_side=None):
            topts = patched_dict["transformer_options"].copy()

            def attn_override(original_attn, q, k, v, heads, **kwargs):
                transformer_options = kwargs.get("transformer_options", {})
                attn_kind = resolve_attn_kind(transformer_options, q=q, k=k, v=v)
                t_index = int(transformer_options.get("transformer_index", -1))

                if hook_target == "attn1" and attn_kind != "attn1":
                    return original_attn(q, k, v, heads, **kwargs)
                if hook_target == "attn2" and attn_kind != "attn2":
                    return original_attn(q, k, v, heads, **kwargs)

                blk = transformer_options.get("block", None)
                if isinstance(blk, (tuple, list)) and len(blk) >= 2:
                    stage = str(blk[0])
                    layer_id = int(blk[1])
                else:
                    stage = "unknown"
                    layer_id = int(transformer_options.get("block_index", -1))

                idx = layer_id
                total_blocks = None

                if not match_index(idx, total_blocks, stage, transformer_options, attn_kind):
                    return original_attn(q, k, v, heads, **kwargs)

                co = transformer_options.get("cond_or_uncond", None)
                auto_side, auto_idx = side_from_cond_or_uncond(co)
                side = forced_side if forced_side is not None else auto_side
                idx_side = 0 if side == "positive" else (1 if side == "negative" else auto_idx)

                if not hit_flags.get(attn_kind, False):
                    logging.warning(f"[SelectiveGuiderMathNode] {attn_kind.upper()} HIT stage={stage} layer_id={layer_id} side={side}")
                    hit_flags[attn_kind] = True

                # v register_attn -> attn_override(...), před `meta = { ... }` přidej ---
                act_shape = transformer_options.get("activations_shape", [])
                if not isinstance(act_shape, (list, tuple)):
                    act_shape = []

                act_h = float(act_shape[2]) if len(act_shape) >= 4 else -1.0
                act_w = float(act_shape[3]) if len(act_shape) >= 4 else -1.0

                meta = {
                    "hook_kind": attn_kind,
                    "hook_domain": "attention",
                    "attn_kind": attn_kind,
                    "transformer_index": float(t_index),
                    "is_dit": 0.0,
                    "is_attn1": 1.0 if attn_kind == "attn1" else 0.0,
                    "is_attn2": 1.0 if attn_kind == "attn2" else 0.0,
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
                    "layer_key": f"{stage}.{layer_id}.{attn_kind}.{t_index}",
                    "cond_side": side,
                    "cond_index": float(idx_side),
                    "is_positive": 1.0 if side == "positive" else 0.0,
                    "is_negative": 1.0 if side == "negative" else 0.0,
                } | {
                    "activations_shape": list(act_shape),
                    "activation_b": float(act_shape[0]) if len(act_shape) > 0 else -1.0,
                    "activation_c": float(act_shape[1]) if len(act_shape) > 1 else -1.0,
                    "activation_h": float(act_shape[2]) if len(act_shape) > 2 else -1.0,
                    "activation_w": float(act_shape[3]) if len(act_shape) > 3 else -1.0,
                }

                out = original_attn(q, k, v, heads, **kwargs)
                return run_expr(out, meta)

            topts["optimized_attention_override"] = attn_override
            patched_dict["transformer_options"] = topts
            return patched_dict

        def register_unet_blocks(patched_dict, forced_side=None):
            topts = patched_dict["transformer_options"].copy()
            patches = topts.get("patches", {}).copy()

            def _parse_block(transformer_options: dict, fallback_stage: str):
                blk = transformer_options.get("block", None)
                if isinstance(blk, (tuple, list)) and len(blk) >= 2:
                    return str(blk[0]), int(blk[1])
                return fallback_stage, int(transformer_options.get("block_index", -1))

            def _apply_block_expr(t: torch.Tensor, transformer_options: dict, stage: str, idx: int):
                if not match_index(idx, None, stage, transformer_options, "unet_block"):
                    return t

                co = transformer_options.get("cond_or_uncond", None)
                auto_side, auto_idx = side_from_cond_or_uncond(co)
                side = forced_side if forced_side is not None else auto_side
                idx_side = 0 if side == "positive" else (1 if side == "negative" else auto_idx)

                if not hit_flags["unet"]:
                    logging.warning(f"[SelectiveGuiderMathNode] UNET BLOCK HIT stage={stage} layer_id={idx} side={side}")
                    hit_flags["unet"] = True

                meta = {
                    "hook_kind": "unet_block",
                    "hook_domain": "diffusion",
                    "attn_kind": "none",
                    "is_dit": 0.0,
                    "is_unet_block": 1.0,
                    "is_time_emb": 1.0 if stage == "time_emb" else 0.0,
                    "is_attn1": 0.0,
                    "is_attn2": 0.0,
                    "block_name": stage,
                    "layer_id": float(idx),
                    "layer": float(idx),
                    "i": float(idx),
                    "total_blocks": -1.0,
                    "has_qkv": 0.0,
                    "layer_key": f"unet.{stage}.{idx}",
                    "cond_side": side,
                    "cond_index": float(idx_side),
                    "is_positive": 1.0 if side == "positive" else 0.0,
                    "is_negative": 1.0 if side == "negative" else 0.0,
                }
                return run_expr(t, meta)

            def input_block_patch(h, transformer_options):
                stage, idx = _parse_block(transformer_options, "input")
                return _apply_block_expr(h, transformer_options, stage, idx)

            def output_block_patch(h, hsp, transformer_options):
                stage, idx = _parse_block(transformer_options, "output")
                h2 = _apply_block_expr(h, transformer_options, stage, idx)
                return h2, hsp

            def middle_patch(x, extra_options):
                stage, idx = _parse_block(extra_options, "middle")
                return _apply_block_expr(x, extra_options, stage, idx)

            def emb_patch(emb, model_channels, transformer_options):
                # začátek timestep pipeline
                return _apply_block_expr(emb, transformer_options, "time_emb", 0)

            patches["input_block_patch"] = list(patches.get("input_block_patch", [])) + [input_block_patch]
            patches["output_block_patch"] = list(patches.get("output_block_patch", [])) + [output_block_patch]
            patches["middle_patch"] = list(patches.get("middle_patch", [])) + [middle_patch]
            patches["emb_patch"] = list(patches.get("emb_patch", [])) + [emb_patch]

            topts["patches"] = patches
            patched_dict["transformer_options"] = topts
            return patched_dict

        def register_model_edges(patched_dict, forced_side=None):
            topts = patched_dict["transformer_options"].copy()
            wrappers = topts.get("wrappers", {}).copy()
            wtype = comfy.patcher_extension.WrappersMP.DIFFUSION_MODEL
            bucket = wrappers.get(wtype, {}).copy()
            key = "mrmth_model_edges"

            def model_edges_wrapper(executor, x, *args, **kwargs):
                # BEGIN (all the way at the beginning)
                pre_meta = {
                    "hook_kind": "model_begin",
                    "hook_domain": "diffusion",
                    "attn_kind": "none",
                    "block_name": "model",
                    "layer_id": -1.0,
                    "layer": -1.0,
                    "i": -1.0,
                    "total_blocks": -1.0,
                    "has_qkv": 0.0,
                    "layer_key": "model.begin",
                }
                xin = run_expr(x, pre_meta) if isinstance(x, torch.Tensor) else x

                out = executor(xin, *args, **kwargs)

                # END (all the way at the end)
                if isinstance(out, torch.Tensor):
                    post_meta = {
                        "hook_kind": "model_end",
                        "hook_domain": "diffusion",
                        "attn_kind": "none",
                        "block_name": "model",
                        "layer_id": -1.0,
                        "layer": -1.0,
                        "i": -1.0,
                        "total_blocks": -1.0,
                        "has_qkv": 0.0,
                        "layer_key": "model.end",
                    }
                    return run_expr(out, post_meta)
                return out

            bucket[key] = list(bucket.get(key, [])) + [model_edges_wrapper]
            wrappers[wtype] = bucket
            topts["wrappers"] = wrappers
            patched_dict["transformer_options"] = topts
            return patched_dict

        def build_transformers_for_side(side_label=None):
            p = comfy.model_patcher.create_model_options_clone(V.model_options)
            p.setdefault("transformer_options", {})
            if hook_target in ("all", "dit_block"):
                register_dit(p, forced_side=side_label)
            if hook_target in ("all", "unet_block"):
                p = register_unet_blocks(p, forced_side=side_label)
            if hook_target in ("all", "attn1", "attn2"):
                p = register_attn(p, forced_side=side_label)
            if hook_target in ("all", "unet_block"):
                p = register_model_edges(p, forced_side=side_label)
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

        # po parse_expr(...)
        if hasattr(V, "original_conds"):
            if not hasattr(V, "_mrmth_base_original_conds"):
                V._mrmth_base_original_conds = copy.deepcopy(V.original_conds)
            else:
                V.original_conds = copy.deepcopy(V._mrmth_base_original_conds)

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
            if hook_target in ("all", "unet_block"):
                patched = register_unet_blocks(patched, forced_side=None)
            if hook_target in ("all", "attn1", "attn2"):
                patched = register_attn(patched, forced_side=None)
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
        return (V, stack)