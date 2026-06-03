from __future__ import annotations

import copy

import comfy
from comfy.patcher_extension import PatcherInjection
from comfy.weight_adapter.bypass import BypassForwardHook
from comfy_api.latest import io


class BatchLoraHooksNode(io.ComfyNode):
    """Scale existing bypass LoRA injections on a model/clip pair."""

    @staticmethod
    def _get_bypass_hooks(injections):
        if injections is None:
            return []

        hooks = []
        for injection in injections:
            closure = getattr(getattr(injection, "inject", None), "__closure__", None)
            if not closure:
                continue
            for cell in closure:
                cell_value = cell.cell_contents
                if hasattr(cell_value, "hooks") and hasattr(cell_value, "create_injections"):
                    manager_hooks = getattr(cell_value, "hooks", None)
                    if manager_hooks:
                        hooks.extend(manager_hooks)
                    break
        return hooks

    @staticmethod
    def _build_bypass_injection(hooks, scale: float):
        scaled_hooks = []
        for hook in hooks:
            adapter = copy.deepcopy(hook.adapter)
            scaled_hooks.append(BypassForwardHook(hook.module, adapter, multiplier=hook.multiplier * scale))

        def inject_all(model_patcher):
            for hook in scaled_hooks:
                hook.inject()

        def eject_all(model_patcher):
            for hook in scaled_hooks:
                hook.eject()

        return [PatcherInjection(inject=inject_all, eject=eject_all)]

    @classmethod
    def _scale_bypass_injections(cls, patcher, scale: float):
        if patcher is None:
            return

        injections = getattr(patcher, "get_injections", lambda _key: None)("bypass_lora")
        if injections is None:
            return

        hooks = cls._get_bypass_hooks(injections)
        if not hooks:
            return

        was_injected = getattr(patcher, "is_injected", False)
        if was_injected:
            patcher.eject_model()

        patcher.set_injections("bypass_lora", cls._build_bypass_injection(hooks, scale))

        if was_injected:
            patcher.inject_model()

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_BatchLoraHooksNode",
            category="More math",
            display_name="Scale LoRA hooks",
            inputs=[
                io.Model.Input(id="model", tooltip="The model with bypass LoRA injections"),
                io.Clip.Input(id="clip", tooltip="The clip with bypass LoRA injections"),
                io.Float.Input(id="model_strength", default=1.0, tooltip="Multiplier for model-side LoRA strength"),
                io.Float.Input(id="clip_strength", default=1.0, tooltip="Multiplier for clip-side LoRA strength"),
            ],
            outputs=[
                io.Model.Output(id="model", tooltip="The model with scaled bypass LoRA injections"),
                io.Clip.Output(id="clip", tooltip="The clip with scaled bypass LoRA injections"),
            ],
        )

    @classmethod
    def execute(cls, model, clip, model_strength, clip_strength):
        scaled_model = model.clone()
        scaled_clip = clip.clone()

        cls._scale_bypass_injections(scaled_model, model_strength)
        clip_patcher = getattr(scaled_clip, "patcher", None)
        cls._scale_bypass_injections(clip_patcher, clip_strength)

        return (scaled_model, scaled_clip)
