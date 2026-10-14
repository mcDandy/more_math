import math
import os
import sys

import torch
import pytest

_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.inbuilt_symbols import INBUILT_FUNCTIONS
from more_math.helper_functions import parse_expr


def eval_expr(expr, variables=None, shape=(1,)):
    tree = parse_expr(expr)
    return UnifiedMathVisitor(variables or {}, shape).visit(tree)


def test_numeric_functions_and_float8_support():
    assert math.isclose(eval_expr("cbrt(-27)"), -3.0)
    assert eval_expr("reciprocal([2, 4])") == [0.5, 0.25]
    assert math.isclose(eval_expr("logaddexp(1, 1)"), 1.0 + math.log(2.0))
    assert math.isclose(eval_expr("norm([3, 4])"), 5.0)
    torch.testing.assert_close(torch.tensor(eval_expr("normalize([3, 4])")), torch.tensor([0.6, 0.8]))
    assert math.isclose(eval_expr("logsumexp([0, 0])"), math.log(2.0), rel_tol=1e-6)

    float8_dtype = getattr(torch, "float8_e4m3fn", None)
    if float8_dtype is not None:
        values = torch.tensor([[3.0, 4.0], [5.0, 12.0]], dtype=float8_dtype)
        assert eval_expr("norm(x, 2, 1)", {"x": values}).dtype == float8_dtype
        assert eval_expr("normalize(x)", {"x": values}).dtype == float8_dtype


def test_normalization_and_norm_support_lists_consistently():
    normalized = eval_expr("normalize([3, 4])")
    assert isinstance(normalized, list)
    torch.testing.assert_close(torch.tensor(normalized), torch.tensor([0.6, 0.8]))
    assert math.isclose(eval_expr("snorm([3, 4])"), 5.0)
    torch.testing.assert_close(
        eval_expr("snorm([[3, 4], [0, 0]], 1)"),
        torch.tensor([5.0, 0.0]),
    )


@pytest.mark.parametrize("function", ("std", "var"))
def test_sample_statistics_match_for_small_lists_and_tensors(function):
    for values in ([], [7.0], torch.tensor([]), torch.tensor([7.0])):
        assert eval_expr(f"{function}(x)", {"x": values}) == 0.0

    values_list = [[1.0, 3.0], [5.0, 7.0]]
    values_tensor = torch.tensor(values_list)
    list_result = eval_expr(f"{function}(x, 1)", {"x": values_list})
    tensor_result = eval_expr(f"{function}(x, 1)", {"x": values_tensor})
    torch.testing.assert_close(torch.as_tensor(list_result), torch.as_tensor(tensor_result))

    singleton_slices = torch.tensor([[1.0], [2.0]])
    torch.testing.assert_close(
        eval_expr(f"{function}(x, 1)", {"x": singleton_slices}),
        torch.zeros(2),
    )


def test_linear_algebra_additions():
    torch.testing.assert_close(
        eval_expr("outer(a, b)", {"a": torch.tensor([1.0, 2.0]), "b": torch.tensor([3.0, 4.0])}),
        torch.tensor([[3.0, 4.0], [6.0, 8.0]]),
    )
    assert eval_expr("trace(x)", {"x": torch.tensor([[1.0, 2.0], [3.0, 4.0]])}) == 5.0
    assert eval_expr("det(x)", {"x": torch.tensor([[1.0, 2.0], [3.0, 4.0]])}) == -2.0


def test_matrix_inverse_and_pseudoinverse():
    matrix = torch.tensor([[1.0, 2.0], [3.0, 5.0]])
    inverse = eval_expr("inv(x)", {"x": matrix})
    torch.testing.assert_close(matrix @ inverse, torch.eye(2))

    rectangular = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    pseudoinverse = eval_expr("inv(x, 1)", {"x": rectangular})
    assert pseudoinverse.shape == (3, 2)
    torch.testing.assert_close(rectangular @ pseudoinverse @ rectangular, rectangular)
    assert "inv" in INBUILT_FUNCTIONS
    with pytest.raises(ValueError, match="requires square matrices"):
        eval_expr("inv(x)", {"x": rectangular})

    float8_dtype = getattr(torch, "float8_e4m3fn", None)
    if float8_dtype is not None:
        float8_identity = torch.eye(2, dtype=float8_dtype)
        assert eval_expr("inv(x)", {"x": float8_identity}).dtype == float8_dtype


def test_solve_and_matrix_rank():
    matrix = torch.tensor([[3.0, 1.0], [1.0, 2.0]])
    rhs = torch.tensor([9.0, 8.0])
    result = eval_expr("solve(A, b)", {"A": matrix, "b": rhs})
    torch.testing.assert_close(matrix @ result, rhs)
    assert eval_expr("matrix_rank(A)", {"A": matrix}) == 2

    singular = torch.tensor([[1.0, 2.0], [2.0, 4.0]])
    assert eval_expr("matrix_rank(A)", {"A": singular}) == 1
    assert eval_expr("matrix_rank(A, 1e-5)", {"A": singular}) == 1

    with pytest.raises(ValueError, match="square coefficient matrices"):
        eval_expr("solve(A, b)", {"A": torch.ones(2, 3), "b": rhs})

    float8_dtype = getattr(torch, "float8_e4m3fn", None)
    if float8_dtype is not None:
        float8_identity = torch.eye(2, dtype=float8_dtype)
        assert eval_expr("solve(A, b)", {"A": float8_identity, "b": float8_identity}).dtype == float8_dtype
        assert eval_expr("matrix_rank(A)", {"A": float8_identity}) == 2


def test_real_fft_round_trip():
    values = torch.tensor([0.0, 1.0, 0.5, -1.0, 2.0, 0.25, -0.5, 0.75])
    spectrum = eval_expr("rfft(x)", {"x": values})
    assert spectrum.is_complex()
    torch.testing.assert_close(eval_expr("irfft(f, 8)", {"f": spectrum}), values)


def test_colored_noise_is_seeded_normalized_and_spectrally_shaped():
    pink = eval_expr("pink_noise(123, [4, 512])")
    pink_repeat = eval_expr("pink(123, [4, 512])")
    brown = eval_expr("brown_noise(123, [4, 512])")
    brown_repeat = eval_expr("brown(123, [4, 512])")

    assert pink.shape == (4, 512)
    assert brown.shape == (4, 512)
    torch.testing.assert_close(pink, pink_repeat)
    torch.testing.assert_close(brown, brown_repeat)
    torch.testing.assert_close(pink.mean(dim=-1), torch.zeros(4), atol=1e-6, rtol=0)
    torch.testing.assert_close(brown.mean(dim=-1), torch.zeros(4), atol=1e-6, rtol=0)
    torch.testing.assert_close(pink.std(dim=-1, unbiased=False), torch.ones(4))
    torch.testing.assert_close(brown.std(dim=-1, unbiased=False), torch.ones(4))

    pink_power = torch.fft.rfft(pink).abs().square().mean(dim=0)
    brown_power = torch.fft.rfft(brown).abs().square().mean(dim=0)
    assert pink_power[1:16].mean() > pink_power[64:128].mean()
    assert brown_power[1:16].mean() > brown_power[64:128].mean()


def test_added_symbols_are_registered():
    expected = {
        "cbrt", "reciprocal", "logaddexp", "logsumexp", "norm", "normalize",
        "outer", "trace", "det", "rfft", "irfft", "pink_noise", "pink",
        "brown_noise", "brown",
        "solve", "matrix_rank",
    }
    assert expected <= INBUILT_FUNCTIONS
