from comfy_api.latest import io
import folder_paths
from .Stack import MrmthStack
import comfy
import os
from .helper_functions import parse_expr
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
import torch
import copy
from .ParseTree import MrmthParseTree

class BatchLoraNode(io.ComfyNode):
    """
    A node that applies a batch of LoRA weights to a model.
    """

    @staticmethod
    def _parse_strengths(Expression, stack,lora_list,lora_count):
        tree = None
        variables = {"lora_names": lora_list, "lora_count": lora_count}
        if isinstance(Expression,str):
            tree = parse_expr(Expression)
        else:
            tree = Expression
        visitor = UnifiedMathVisitor(variables, [1],torch.device("cpu"),state_storage=stack)
        print(stack)
        result = visitor.visit(tree)
        return (list(result), stack)
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_BatchLoraNode",
            category="More math",
            display_name="Batch LoRa apply",
            inputs=[
                io.Model.Input(id="model", tooltip="The model to apply the LoRA weights to"),
                io.Clip.Input(id="clip", tooltip="The clip to apply the LoRA weights to"),
                io.String.Input(id="folder", tooltip="The sub-folder containing the LoRA weights"),
                io.Boolean.Input(id="add_no_lora", tooltip="Whether to add a model execution without a lora"),
                io.MultiType.Input(
                    io.String.Input("model_strength", default="1.0", multiline=False),
                    types=[io.String,MrmthParseTree],
                    tooltip="strength of lora applied to model",
                ),                io.MultiType.Input(
                    io.String.Input("clip_strength", default="1.0", multiline=False),
                    types=[io.String,MrmthParseTree],
                    tooltip="strength of lora applied to clip",
                ),
                MrmthStack.Input(id="stack", tooltip="The stack", optional=True),
            ],
            outputs=[
                io.Model.Output(id="model", tooltip="The model with the LoRA weights applied", is_output_list=True),
                io.Clip.Output(id="clip", tooltip="The clip with the LoRA weights applied", is_output_list=True),
                MrmthStack.Output(id="stack", tooltip="The stack"),
            ],
        )

    @classmethod
    def execute(cls, model, clip, folder, add_no_lora, model_strength, clip_strength, stack=None):
        paths = folder_paths.get_folder_paths("loras")
        print(paths)
        lora_path = folder_paths.get_filename_list("loras")
        stack = copy.deepcopy(stack) if stack is not None else {}
        selected_folder = os.path.normpath(folder)
        if selected_folder:
            lora_path = [
                lora
                for lora in lora_path
                if os.path.normpath(lora) == selected_folder
                or os.path.normpath(lora).startswith(selected_folder + os.sep)
            ]

        print("BatchLoraNode: Found LoRA weights:", lora_path)

        model_strengths, stack = cls._parse_strengths(model_strength, stack, lora_path, len(lora_path))
        clip_strengths, stack = cls._parse_strengths(clip_strength, stack, lora_path, len(lora_path))
        print(stack)
        model_lora = [model] if add_no_lora else []
        clip_lora = [clip] if add_no_lora else []
        for index, lora in enumerate(lora_path):
            model = model.clone()
            clip = clip.clone()
            full_lora_path = folder_paths.get_full_path("loras", lora)
            if full_lora_path is None:
                print(f"BatchLoraNode: Skipping missing LoRA: {lora}")
                continue

            model_strength_value = model_strengths[index] if index < len(model_strengths) else model_strengths[-1]
            clip_strength_value = clip_strengths[index] if index < len(clip_strengths) else clip_strengths[-1]

            loraw = comfy.utils.load_torch_file(full_lora_path, safe_load=True)
            modellr, cliplr = comfy.sd.load_bypass_lora_for_models(
                model,
                clip,
                loraw,
                model_strength_value,
                clip_strength_value,
            )
            model_lora.append(modellr)
            clip_lora.append(cliplr)
        return (model_lora, clip_lora, stack)
