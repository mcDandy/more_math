import pytest
import torch

from more_math.LoraMathNode import LoraMathNode


def test_lora_math_uses_v0_as_a_and_supports_scalar_expression():
    lora = {"layer.weight": torch.tensor([1.0, 2.0])}

    result, stack = LoraMathNode.execute(
        V={"V0": lora},
        F={},
        Expression="a * 3",
        use_compute_device=False,
        stack=None,
    )

    assert stack == {}
    torch.testing.assert_close(result["layer.weight"], torch.tensor([3.0, 6.0]))


def test_lora_math_preserves_union_of_sparse_lora_keys():
    first = {
        "only_first": torch.tensor([1.0, 2.0]),
        "shared": torch.tensor([3.0, 4.0]),
    }
    second = {
        "shared": torch.tensor([10.0, 20.0]),
        "only_second": torch.tensor([30.0, 40.0]),
    }

    result, _ = LoraMathNode.execute(
        V={"V0": first, "V1": second},
        F={},
        Expression="V0 + V1",
        use_compute_device=False,
        stack=None,
    )

    assert set(result) == {"only_first", "shared", "only_second"}
    torch.testing.assert_close(result["only_first"], first["only_first"])
    torch.testing.assert_close(result["shared"], torch.tensor([13.0, 24.0]))
    torch.testing.assert_close(result["only_second"], second["only_second"])


def test_lora_math_dictionary_mode_preserves_keys():
    lora = {
        "layer_a": torch.tensor([1.0]),
        "layer_b": torch.tensor([2.0]),
    }

    result, _ = LoraMathNode.execute(
        V={"V0": lora},
        F={},
        Expression="V0 * 2",
        use_compute_device=False,
        stack=None,
        dict_mode=True,
    )

    assert set(result) == set(lora)
    torch.testing.assert_close(result["layer_a"], torch.tensor([2.0]))
    torch.testing.assert_close(result["layer_b"], torch.tensor([4.0]))


def test_lora_math_rejects_empty_inputs():
    with pytest.raises(ValueError, match="At least one input LoRA is required"):
        LoraMathNode.execute(
            V={"V0": None},
            F={},
            Expression="V0",
            use_compute_device=False,
            stack=None,
        )


def test_lora_math_schema_has_expected_contract():
    schema = LoraMathNode.define_schema()

    assert schema.node_id == "mrmth_ag_LoraMathNode"
    assert [input_.id for input_ in schema.inputs] == [
        "V",
        "F",
        "Expression",
        "dict_mode",
        "use_compute_device",
        "stack",
    ]
    assert len(schema.outputs) == 2
