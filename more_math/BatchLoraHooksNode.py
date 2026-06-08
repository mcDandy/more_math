from __future__ import annotations

import copy
import torch

from comfy.patcher_extension import PatcherInjection
from comfy.weight_adapter.bypass import BypassForwardHook
from comfy_api.latest import io

from .helper_functions import parse_expr
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from .Stack import Stack
from .ParseTree import MrmthParseTree

@staticmethod
def _parse_strengths(Expression, stack):
    tree = None
    variables = {}
    if isinstance(Expression,str):
        tree = parse_expr(Expression)
    else:
        tree = Expression
    visitor = UnifiedMathVisitor(variables, [1],torch.device("cpu"),state_storage=stack)
    result = visitor.visit(tree)
    return (list(result), stack)

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
            node_id="mrmth_LoraBatchRescale",
            category="More math",
            display_name="Scale LoRA (Batch)",
            inputs=[
                io.Model.Input(id="model", tooltip="The model with bypass LoRA injections"),
                io.Clip.Input(id="clip", tooltip="The clip with bypass LoRA injections"),
                io.MultiType.Input(
                    io.String.Input("model_strength", default="[1.0]", multiline=False),
                    types=[io.String, MrmthParseTree],
                    tooltip="List of model-side LoRA strengths",
                ),                io.MultiType.Input(
                    io.String.Input("clip_strength", default="[1.0]", multiline=False),
                    types=[io.String, MrmthParseTree],
                    tooltip="List of clip-side LoRA strengths",
                ),
                Stack.Input(id="stack", default=None, optional=True)
            ],
            outputs=[
                io.Model.Output(id="model", tooltip="The model with scaled bypass LoRA injections", is_output_list=True),
                io.Clip.Output(id="clip", tooltip="The clip with scaled bypass LoRA injections", is_output_list=True),
                Stack.Output(id="stack", tooltip="The stack"),
            ],
        )

    @classmethod
    def execute(cls, model, clip, model_strength, clip_strength, stack=None):
        stack = copy.deepcopy(stack) if stack is not None else {}
        weights0, stack = _parse_strengths(model_strength, {})
        weights1, stack = _parse_strengths(clip_strength, {})
        scaled_models = []
        scaled_clips = []
        if len(weights0) != len(weights1):
            raise ValueError("model_strength and clip_strength must have the same number of elements. Model: {}, Clip: {}".format(len(weights0), len(weights1)))
        for w0,w1 in zip(weights0, weights1):
            scaled_model = model.clone()
            scaled_clip = clip.clone()
            cls._scale_bypass_injections(scaled_model, w0)
            clip_patcher = getattr(scaled_clip, "patcher", None)
            cls._scale_bypass_injections(clip_patcher, w1)
            scaled_models.append(scaled_model)
            scaled_clips.append(scaled_clip)

        return (scaled_models, scaled_clips, stack)
