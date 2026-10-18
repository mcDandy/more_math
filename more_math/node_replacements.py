from comfy_api.latest import ComfyAPI, io

api = ComfyAPI()

# old node id, new node id, old widgets in saved order mapped to the new input ids
REPLACEMENTS = [
    ("mrmth_AudioMathNode", "mrmth_ag_AudioMathNode", {"Audio": "Expression", "length_mismatch": "length_mismatch"}),
    ("mrmth_CLIPMathNode", "mrmth_ag_CLIPMathNode", {"Model": "Expression", "length_mismatch": "length_mismatch"}),
    ("mrmth_ConditioningMathNode", "mrmth_ag_ConditioningMathNode", {"Tensor": "Expression", "pooled_output": "Expression_pi", "length_mismatch": "length_mismatch"}),
    ("mrmth_FloatMathNode", "mrmth_ag_FloatMathNode", {"FloatFunc": "FloatFunc"}),
    ("mrmth_ImageMathNode", "mrmth_ag_ImageMathNode", {"Image": "Expression", "length_mismatch": "length_mismatch"}),
    ("mrmth_LatentMathNode", "mrmth_ag_LatentMathNode", {"Latent": "Expression", "length_mismatch": "length_mismatch"}),
    ("mrmth_MaskMathNode", "mrmth_ag_MaskMathNode", {"Mask": "Expression", "length_mismatch": "length_mismatch"}),
    ("mrmth_ModelMathNode", "mrmth_ag_ModelMathNode", {"Model": "Expression", "length_mismatch": "length_mismatch"}),
    ("mrmth_NoiseMathNode", "mrmth_ag_NoiseMathNode", {"Noise": "Noise"}),
    ("mrmth_VAEMathNode", "mrmth_ag_VAEMathNode", {"Model": "Expression", "length_mismatch": "length_mismatch"}),
    ("mrmth_VideoMathNode", "mrmth_ag_VideoMathNode", {"Images": "Expression", "Audio": "Expression_pi", "length_mismatch": "length_mismatch"}),
]


def make_replacement(old_id, new_id, widgets):
    # a-d become V0-V3 and w-z become F0-F3; the float node has no F inputs and reads w-z from V4-V7
    float_inputs = [f"V.V{i}" for i in range(4, 8)] if new_id == "mrmth_ag_FloatMathNode" else [f"F.F{i}" for i in range(4)]
    inputs = [{"new_id": f"V.V{i}", "old_id": name} for i, name in enumerate("abcd")]
    inputs += [{"new_id": new, "old_id": name} for new, name in zip(float_inputs, "wxyz")]
    inputs += [{"new_id": new, "old_id": old} for old, new in widgets.items()]
    return io.NodeReplace(
        new_node_id=new_id,
        old_node_id=old_id,
        old_widget_ids=list(widgets),
        input_mapping=inputs,
        output_mapping=[{"new_idx": 0, "old_idx": 0}],
    )


async def register_replacements():
    for replacement in REPLACEMENTS:
        await api.node_replacement.register(make_replacement(*replacement))
