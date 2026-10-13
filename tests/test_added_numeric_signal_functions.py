import math
import os
import sys

import torch

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
    torch.testing.assert_close(eval_expr("normalize([3, 4])"), torch.tensor([0.6, 0.8]))
    assert math.isclose(eval_expr("logsumexp([0, 0])"), math.log(2.0), rel_tol=1e-6)

    float8_dtype = getattr(torch, "float8_e4m3fn", None)
    if float8_dtype is not None:
        values = torch.tensor([[3.0, 4.0], [5.0, 12.0]], dtype=float8_dtype)
        assert eval_expr("norm(x, 2, 1)", {"x": values}).dtype == float8_dtype
        assert eval_expr("normalize(x)", {"x": values}).dtype == float8_dtype


def test_linear_algebra_additions():
    torch.testing.assert_close(
        eval_expr("outer(a, b)", {"a": torch.tensor([1.0, 2.0]), "b": torch.tensor([3.0, 4.0])}),
        torch.tensor([[3.0, 4.0], [6.0, 8.0]]),
    )
    assert eval_expr("trace(x)", {"x": torch.tensor([[1.0, 2.0], [3.0, 4.0]])}) == 5.0
    assert eval_expr("det(x)", {"x": torch.tensor([[1.0, 2.0], [3.0, 4.0]])}) == -2.0


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
    }
    assert expected <= INBUILT_FUNCTIONS
