import importlib
import math
import os

import pytest
import torch
from PIL import ImageFont

from more_math.Parser.UnifiedMathVisitor import ChangeTrackingDict, MathDict, UnifiedMathVisitor
from more_math.helper_functions import parse_expr


def _visit(expression, variables):
    return UnifiedMathVisitor(variables).visit(parse_expr(expression))


def test_tracked_dict_arithmetic_preserves_original_baseline():
    values = {
        "changed": torch.tensor([1.0, 2.0]),
        "unchanged": torch.tensor([3.0, 4.0]),
    }
    result = _visit("V0 * 2", {"V0": ChangeTrackingDict(values)})

    assert isinstance(result, ChangeTrackingDict)
    assert result.get_changed_keys() == {"changed", "unchanged"}
    assert torch.equal(result._initial_values["changed"], values["changed"])
    assert torch.equal(result["changed"], torch.tensor([2.0, 4.0]))


def test_tracked_dict_mapping_uses_v0_baseline_and_untracked_v1():
    v0 = ChangeTrackingDict({"weight": torch.tensor([1.0, 2.0])})
    v1 = MathDict({"weight": torch.tensor([3.0, 4.0])})

    result = _visit("V0 + V1", {"V0": v0, "V1": v1})
    v1_result = _visit("V1", {"V0": v0, "V1": v1})

    assert result.get_changed_keys() == {"weight"}
    assert isinstance(v1_result, MathDict)
    assert not isinstance(v1_result, ChangeTrackingDict)


@pytest.mark.parametrize(
    "dtype_name",
    ("float8_e4m3fn", "float8_e4m3fnuz", "float8_e5m2", "float8_e5m2fnuz"),
)
def test_float8_operations_preserve_dtype(dtype_name):
    dtype = getattr(torch, dtype_name, None)
    if dtype is None:
        pytest.skip(f"{dtype_name} is unavailable in this PyTorch build")

    values = torch.tensor([1.0, 2.0], dtype=dtype)
    tensor_result = _visit("x * 2", {"x": values})
    unary_result = _visit("-x", {"x": values})
    math_result = _visit("log2(x)", {"x": values})
    hypot_result = _visit("hypot(3*x, 4*x)", {"x": values})
    logical_result = _visit("logical_and(x, 1)", {"x": values})
    dict_result = _visit("V0 * 2", {"V0": ChangeTrackingDict({"weight": values})})

    assert tensor_result.dtype == dtype
    assert unary_result.dtype == dtype
    assert math_result.dtype == dtype
    assert hypot_result.dtype == dtype
    assert logical_result.dtype == dtype
    assert dict_result["weight"].dtype == dtype
    assert torch.equal(tensor_result.float(), torch.tensor([2.0, 4.0]))
    assert torch.equal(unary_result.float(), torch.tensor([-1.0, -2.0]))
    assert torch.equal(math_result.float(), torch.tensor([0.0, 1.0]))
    assert torch.equal(hypot_result.float(), torch.tensor([5.0, 10.0]))
    assert torch.equal(logical_result.float(), torch.tensor([1.0, 1.0]))
    assert torch.equal(dict_result["weight"].float(), torch.tensor([2.0, 4.0]))


@pytest.mark.parametrize("call", ("f()", "f(1, 2)"))
def test_lambda_calls_require_exact_argument_count(call):
    with pytest.raises(ValueError, match="Lambda expects 1 arguments"):
        _visit(f"f = (x) -> x; {call}", {})


def test_text_image_size_expression_is_evaluated_once(monkeypatch):
    visitor_module = importlib.import_module("more_math.Parser.UnifiedMathVisitor")
    default_font = ImageFont.load_default()
    original_exists = os.path.exists
    monkeypatch.setattr(
        visitor_module.ImageFont,
        "truetype",
        lambda *args, **kwargs: default_font,
    )
    monkeypatch.setattr(
        visitor_module.os.path,
        "exists",
        lambda path: path == "mock-font" or original_exists(path),
    )

    values = MathDict()
    _visit(
        'text_image("x", "mock-font", count(add_key(d, count(d), 1)))',
        {"d": values},
    )

    assert len(values) == 1


def test_stack_list_of_tensors_with_negative_dimension():
    first = torch.tensor([1.0, 2.0])
    second = torch.tensor([3.0, 4.0])

    result = _visit("stack([a, b], -1)", {"a": first, "b": second})

    assert result.shape == (2, 2)
    assert torch.equal(result, torch.tensor([[1.0, 3.0], [2.0, 4.0]]))


def test_stack_rejects_invalid_dimension_and_non_list_input():
    with pytest.raises(ValueError, match="stack expects a non-empty list"):
        _visit("stack(a)", {"a": torch.tensor([1.0, 2.0])})
    with pytest.raises(ValueError, match="stack dimension"):
        _visit("stack([a], 2)", {"a": torch.tensor([1.0, 2.0])})


@pytest.mark.parametrize("function", ("transpose", "swapaxes"))
def test_axis_swap_functions_support_negative_dimensions(function):
    values = torch.arange(24).reshape(2, 3, 4)

    result = _visit(f"{function}(x, -1, 0)", {"x": values})

    assert result.shape == (4, 3, 2)
    assert torch.equal(result, values.transpose(-1, 0))


def test_axis_swap_rejects_out_of_range_dimension():
    with pytest.raises(ValueError, match="transpose dimension"):
        _visit("transpose(x, 0, 2)", {"x": torch.ones(2, 3)})


def test_nonzero_returns_coordinate_indices():
    values = torch.tensor([[0.0, 2.0], [-1.0, 0.0]])

    result = _visit("nonzero(x)", {"x": values})

    assert result.dtype == torch.int64
    assert result.device == values.device
    assert torch.equal(result, torch.tensor([[0, 1], [1, 0]], dtype=torch.int64))


def test_nonzero_empty_result_preserves_rank():
    result = _visit("nonzero(x)", {"x": torch.zeros(2, 3)})

    assert result.shape == (0, 2)
    assert result.dtype == torch.int64


def test_unique_tensor_and_list():
    assert torch.equal(_visit("unique(x)", {"x": torch.tensor([3.0, 1.0, 2.0, 1.0])}), torch.tensor([1.0, 2.0, 3.0]))
    assert _visit("unique(x)", {"x": [3.0, 1.0, 3.0]}) == [1.0, 3.0]


@pytest.mark.parametrize(
    ("expression", "expected"),
    (("std(5)", 0.0), ("var(5)", 0.0), ("tnorm(-3)", -1.0), ("median(x)", 2.0)),
)
def test_scalar_and_list_statistics(expression, expected):
    assert _visit(expression, {"x": [4.0, 1.0, 3.0, 2.0]}) == expected


def test_gamma_tensor_keeps_sign_for_negative_inputs():
    result = _visit("gamma(x)", {"x": torch.tensor([-0.5, -1.5, 0.5])})

    assert torch.allclose(result, torch.tensor([math.gamma(-0.5), math.gamma(-1.5), math.gamma(0.5)]))


def test_get_value_out_of_bounds_reports_position():
    with pytest.raises(ValueError, match="1:0: Index 5 out of bounds"):
        _visit("get_value(x, [5])", {"x": torch.tensor([1.0, 2.0])})


def test_permute_accepts_negative_dims():
    assert _visit("permute(x, [0, -1, 1])", {"x": torch.zeros(2, 3, 4)}).shape == (2, 4, 3)


def test_blur_kernel_is_centred():
    image = torch.zeros(1, 1, 9, 9)
    image[0, 0, 4, 4] = 1.0

    result = _visit("blur(x, 1)", {"x": image})[0, 0]

    assert torch.allclose(result, result.flip(0)) and torch.allclose(result, result.flip(1))


def test_interpolate_zero_dim_tensor_is_scale_factor():
    assert _visit("interpolate_nearest(x, s)", {"x": torch.zeros(1, 1, 4, 4), "s": torch.tensor(2.0)}).shape == (1, 1, 8, 8)


def test_string_flip_and_concatenate():
    assert _visit('flip("abc", 0)', {}) == "cba"
    assert _visit('cat("a", "b", 0)', {}) == "ab"


def test_coords_uses_dtype_template():
    assert _visit("coords([2, 3], 1, t)", {"t": torch.zeros(1, dtype=torch.int64)}).dtype == torch.int64


@pytest.mark.parametrize(
    "expression",
    (
        "perlin(1, 8, 1, 0, [256, 256])",
        "perlin(1, 8, 4, 0, [16, 16, 16])",
        "plasma(1, 8, 1, 0, [256, 256])",
        "ridged(1, 8, 1, 0, [256, 256])",
        "domain_warp(1, 8, 4, 4, 4, 2, 0, [256, 256])",
        "cellular(1, 8, 1, 0, [256, 256])",
    ),
)
def test_procedural_noise_stays_in_unit_range(expression):
    result = _visit(expression, {})

    assert result.min() >= 0.0 and result.max() <= 1.0


def test_perlin_uses_full_unit_range():
    result = _visit("perlin(1, 8, 1, 0, [4096])", {})

    assert result.min() < 0.05 and result.max() > 0.95
