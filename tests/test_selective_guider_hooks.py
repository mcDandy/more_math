from types import SimpleNamespace

import torch

from more_math.SelectiveGuiderMathNode import SelectiveGuiderMathNode


def make_guider(hook_target, layer_x=0):
    guider = SimpleNamespace(model_options={})
    SelectiveGuiderMathNode.execute(
        V=guider,
        F={},
        Expression="inp + 1",
        hook_target=hook_target,
        layer_x=layer_x,
    )
    return guider


def test_attention_input_hook_transforms_projected_qkv():
    guider = make_guider("attn_input")
    options = guider.model_options["transformer_options"]
    q = torch.zeros(1, 2, 3, 4)
    seen = []

    def original(q, k, v, heads, **kwargs):
        seen.extend((q, k, v))
        return q

    result = options["optimized_attention_override"](
        original,
        q,
        q,
        q,
        2,
        transformer_options={"block": ("middle", 0), "block_type": "double", "block_index": 0},
    )

    assert torch.equal(result, torch.ones_like(q))
    assert all(torch.equal(tensor, torch.ones_like(q)) for tensor in seen)


def test_attention_qkv_targets_transform_only_the_selected_tensor():
    q, k, v = (torch.zeros(1, 2, 3, 4) for _ in range(3))
    for target, selected in (("attn_q", "q"), ("attn_k", "k"), ("attn_v", "v")):
        options = make_guider(target).model_options["transformer_options"]
        seen = {}

        def original(q, k, v, heads, **kwargs):
            seen.update(q=q, k=k, v=v)
            return q

        options["optimized_attention_override"](
            original,
            q,
            k,
            v,
            2,
            transformer_options={"block": ("middle", 0), "block_type": "double", "block_index": 0},
        )

        for name, tensor in seen.items():
            expected = torch.ones_like(tensor) if name == selected else torch.zeros_like(tensor)
            assert torch.equal(tensor, expected)


def test_post_input_hook_transforms_available_image_and_text_streams():
    guider = make_guider("post_input")
    patch = guider.model_options["transformer_options"]["patches"]["post_input"][0]
    img, txt, img_ids = torch.zeros(1, 2, 3), torch.zeros(1, 4, 3), torch.zeros(1, 2, 3)

    result = patch({"img": img, "txt": txt, "img_ids": img_ids, "transformer_options": {}})

    assert torch.equal(result["img"], torch.ones_like(img))
    assert torch.equal(result["txt"], torch.ones_like(txt))
    assert result["img_ids"] is img_ids
    assert result["transformer_options"] == {}


def test_post_input_hook_supports_models_with_only_image_stream():
    guider = make_guider("post_input")
    patch = guider.model_options["transformer_options"]["patches"]["post_input"][0]
    img = torch.zeros(1, 2, 3)
    result = patch({"img": img, "transformer_options": {}})
    assert torch.equal(result["img"], torch.ones_like(img))


def test_post_input_hook_skips_out_of_range_layer_index():
    guider = make_guider("post_input", layer_x=1)
    patch = guider.model_options["transformer_options"]["patches"]["post_input"][0]
    img = torch.zeros(1, 2, 3)

    result = patch({"img": img, "transformer_options": {}})

    assert result["img"] is img


def test_unet_hook_skips_out_of_range_positive_layer_index():
    guider = make_guider("input_block", layer_x=4)
    patch = guider.model_options["transformer_options"]["patches"]["input_block_patch"][0]
    hidden = torch.zeros(1, 2, 3, 4)

    result = patch(hidden, {"block": ("input", 1)})

    assert result is hidden


def test_granular_unet_targets_register_the_expected_patch():
    expected = {
        "input_block": "input_block_patch",
        "input_block_after_skip": "input_block_patch_after_skip",
        "output_block": "output_block_patch",
        "middle_patch": "middle_patch",
        "middle_block": "middle_block_after_patch",
    }

    for target, patch_name in expected.items():
        options = make_guider(target).model_options["transformer_options"]
        assert len(options["patches"][patch_name]) == 1


def test_granular_unet_hooks_transform_their_activation():
    hidden = torch.zeros(1, 2, 3, 4)
    for target, patch_name in (
        ("input_block", "input_block_patch"),
        ("input_block_after_skip", "input_block_patch_after_skip"),
        ("middle_patch", "middle_patch"),
    ):
        patch = make_guider(target).model_options["transformer_options"]["patches"][patch_name][0]
        assert torch.equal(patch(hidden, {"block": ("input", 0)}), torch.ones_like(hidden))

    options = {"block": ("output", 0)}
    patch = make_guider("output_block").model_options["transformer_options"]["patches"]["output_block_patch"][0]
    h, hsp = patch(hidden, hidden, options)
    assert torch.equal(h, torch.ones_like(hidden))
    assert hsp is hidden

    patch = make_guider("middle_block").model_options["transformer_options"]["patches"]["middle_block_after_patch"][0]
    result = patch({"h": hidden, "transformer_options": {"block": ("middle", 0)}})
    assert torch.equal(result["h"], torch.ones_like(hidden))


def test_noise_refiner_hook_transforms_layer_output():
    guider = make_guider("noise_refiner")
    patch = guider.model_options["transformer_options"]["patches"]["noise_refiner"][0]
    img = torch.zeros(1, 2, 3)
    patch_args = {
        "img": img,
        "img_input": img,
        "txt": img,
        "pe": img,
        "vec": img,
        "x": img,
        "block_index": 0,
        "transformer_options": {},
    }

    result = patch(patch_args)

    assert torch.equal(result["img"], torch.ones_like(img))
    assert result["img_input"] is img
