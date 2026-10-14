import torch
import sys
import os
import math
import pytest

# Ensure test runner usage (Visual Studio) can import the package regardless of working dir.
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
_comfy_root = os.path.abspath(os.path.join(_project_root, os.pardir, os.pardir))
for _path in (_comfy_root, _project_root):
    if _path not in sys.path:
        sys.path.insert(0, _path)

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.inbuilt_symbols import INBUILT_FUNCTIONS
from more_math.helper_functions import parse_expr

def eval_expr(expr, variables={}, shape=(1,)):
    tree = parse_expr(expr)
    visitor = UnifiedMathVisitor(variables, shape)
    return visitor.visit(tree)

def test_logic_functions():
    assert eval_expr("any([0, 0, 1])") == 1.0
    assert eval_expr("any([0, 0, 0])") == 0.0
    assert eval_expr("all([1, 1, 1])") == 1.0
    assert eval_expr("all([1, 0, 1])") == 0.0

    t_any = torch.tensor([0.0, 1.0, 0.0])
    assert eval_expr("any(T)", {"T": t_any}) == 1.0

def test_spatial_functions():
    # Remap
    r = eval_expr("remap(0.5, 0, 1, 10, 20)")
    print(f"DEBUG: remap result: {r} type: {type(r)}")
    assert abs(r - 15.0) < 1e-5

    # Distance
    d = eval_expr("dist(0,0, 3,4)")
    print(f"DEBUG: dist result: {d} type: {type(d)}")
    assert abs(d - 5.0) < 1e-5

    # Edge
    t_img = torch.zeros((1, 32, 32, 1))
    t_img[:, 16:, :, :] = 1.0
    res_edge = eval_expr("edge(I)", {"I": t_img})
    print(f"DEBUG: edge shape: {res_edge.shape} max: {res_edge.max()}")
    assert res_edge.shape == t_img.shape
    assert res_edge.max() > 0

def test_stats_functions():
    # Median
    assert eval_expr("median([1, 10, 2, 5, 3])") == 3

    # Mode
    # Note: list mode uses Counter, returns first most common
    assert eval_expr("mode([1, 2, 2, 3])") == 2

    # Cumsum/Cumprod
    t = torch.tensor([1, 2, 3], dtype=torch.float32)
    assert torch.allclose(eval_expr("cumsum(T)", {"T": t}), torch.tensor([1, 3, 6], dtype=torch.float32))
    assert torch.allclose(eval_expr("cumprod(T)", {"T": t}), torch.tensor([1, 2, 6], dtype=torch.float32))

def test_easing_functions():
    # lerp(0, 10, 0.5) = 5
    # cubic_ease(0, 10, 0.5) = 5 (inflection point)
    assert abs(eval_expr("cubic_ease(0, 10, 0.5)") - 5.0) < 1e-5
    # cubic_ease(0, 10, 0.1) should be less than lerp(0, 10, 0.1) = 1.0
    assert eval_expr("cubic_ease(0, 10, 0.1)") < 1.0

    # Sine ease
    assert abs(eval_expr("sine_ease(0, 10, 0.5)") - 5.0) < 1e-5

    # Smooterstep
    assert abs(eval_expr("smootherstep(0.5, 0, 1)") - 0.5) < 1e-5

def test_lerp_fix():
    # Test w as list
    # lerp(0, 10, [0, 0.5, 1]) -> [0, 5, 10]
    res = eval_expr("lerp(0, 10, [0, 0.5, 1])")
    assert res == [0.0, 5.0, 10.0]

    # Test a, b as lists matching w
    res2 = eval_expr("lerp([0, 10, 20], [10, 20, 30], [0.5, 0.5, 0.5])")
    # Expected: [5, 15, 25]
    assert res2 == [5.0, 15.0, 25.0]

def test_added_math_and_logical_functions():
    added_functions = {
        "logical_not", "logical_and", "logical_or", "degrees", "radians", "log2", "hypot"
    }
    assert added_functions <= INBUILT_FUNCTIONS

    assert eval_expr("logical_not(0)") == 1.0
    assert eval_expr("logical_not(-2)") == 0.0
    assert eval_expr("logical_and(2, 1)") == 1.0
    assert eval_expr("logical_and(2, 0)") == 0.0
    assert eval_expr("logical_or(0, -1)") == 1.0
    assert eval_expr("logical_or(0, 0)") == 0.0

    assert math.isclose(eval_expr("degrees(pi)"), 180.0, rel_tol=1e-6)
    assert math.isclose(eval_expr("radians(180)"), math.pi, rel_tol=1e-6)
    assert eval_expr("log2(8)") == 3.0
    assert eval_expr("hypot(3, 4)") == 5.0

    assert eval_expr("logical_and([1, 0], [1, 1])") == [1.0, 0.0]
    assert eval_expr("logical_or([0, 0], [1, 0])") == [1.0, 0.0]
    assert eval_expr("logical_not([0, 1])") == [1.0, 0.0]
    assert torch.allclose(eval_expr("log2(T)", {"T": torch.tensor([1.0, 2.0, 8.0])}), torch.tensor([0.0, 1.0, 3.0]))
    assert torch.allclose(eval_expr("hypot(A, B)", {"A": torch.tensor([3.0, 5.0]), "B": torch.tensor([4.0, 12.0])}), torch.tensor([5.0, 13.0]))
    assert torch.allclose(eval_expr("logical_or(A, B)", {"A": torch.tensor([0.0, 1.0]), "B": torch.tensor([0.0, 0.0])}), torch.tensor([0.0, 1.0]))
    assert torch.allclose(eval_expr("degrees(T)", {"T": torch.tensor([0.0, math.pi])}), torch.tensor([0.0, 180.0]))

def test_tensor_constructors_and_one_hot():
    template = torch.empty((), dtype=torch.float64)
    zeros = eval_expr("zeros([2, 3], T)", {"T": template})
    assert zeros.shape == (2, 3)
    assert zeros.dtype == torch.float64
    assert torch.count_nonzero(zeros) == 0
    assert torch.equal(eval_expr("ones([2])"), torch.ones(2))
    assert torch.equal(eval_expr("eye(3)"), torch.eye(3))
    assert torch.equal(eval_expr("eye(2, T)", {"T": template}), torch.eye(2, dtype=torch.float64))
    assert torch.equal(
        eval_expr("one_hot([0, 2], 3)"),
        torch.tensor([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]),
    )
    assert "one_hot" in INBUILT_FUNCTIONS
    with pytest.raises(ValueError, match="outside the class range"):
        eval_expr("one_hot([3], 3)")
    with pytest.raises(ValueError, match="must be integers"):
        eval_expr("one_hot([0.5], 3)")

def test_loss_metrics_and_psnr():
    a = torch.tensor([1.0, 3.0])
    b = torch.tensor([2.0, 1.0])
    variables = {"a": a, "b": b}
    assert math.isclose(eval_expr("mse(a, b)", variables).item(), 2.5)
    assert math.isclose(eval_expr("mse(a, b, 'sum')", variables).item(), 5.0)
    assert torch.equal(eval_expr("mse(a, b, 'none')", variables), torch.tensor([1.0, 4.0]))
    assert math.isclose(eval_expr("mae(a, b)", variables).item(), 1.5)
    assert math.isclose(eval_expr("mae(a, b, 'sum')", variables).item(), 3.0)
    assert math.isclose(eval_expr("psnr(a, b)", variables).item(), 10.0 * math.log10(0.4), rel_tol=1e-6)
    assert math.isinf(eval_expr("psnr(a, a)", variables).item())
    assert "mse" in INBUILT_FUNCTIONS and "mae" in INBUILT_FUNCTIONS and "psnr" in INBUILT_FUNCTIONS
    with pytest.raises(ValueError, match="reduction must be"):
        eval_expr("mse(a, b, 'median')", variables)
    with pytest.raises(ValueError, match="data_range must be positive"):
        eval_expr("psnr(a, b, 0)", variables)

def test_leaky_relu_and_softsign():
    assert eval_expr("leaky_relu([-2, 0, 2])") == [-0.02, 0.0, 2.0]
    assert eval_expr("leaky_relu(-2, 0.2)") == -0.4
    assert eval_expr("softsign([-2, 0, 2])") == [-2.0 / 3.0, 0.0, 2.0 / 3.0]
    assert "leaky_relu" in INBUILT_FUNCTIONS and "softsign" in INBUILT_FUNCTIONS

def test_tnorm_normalizes_lists():
    torch.testing.assert_close(torch.tensor(eval_expr("tnorm([3, 4])")), torch.tensor([0.6, 0.8]))
    torch.testing.assert_close(torch.tensor(eval_expr("tnorm([[3, 4], [0, 0]])")), torch.tensor([[0.6, 0.8], [0.0, 0.0]]))
    torch.testing.assert_close(torch.tensor(eval_expr("tnorm([[3, 0], [0, 4]], 0)")), torch.tensor([[1.0, 0.0], [0.0, 1.0]]))

def test_silu_activation():
    expected = torch.nn.functional.silu(torch.tensor([-2.0, 0.0, 2.0])).tolist()
    assert eval_expr("silu([-2, 0, 2])") == pytest.approx(expected)
    assert eval_expr("silu(1000)") == pytest.approx(1000.0)

    values = torch.tensor([-3.0, 0.0, 2.0])
    torch.testing.assert_close(eval_expr("silu(x)", {"x": values}), torch.nn.functional.silu(values))
    assert "silu" in INBUILT_FUNCTIONS

def test_group_norm_matches_pytorch():
    values = torch.arange(24, dtype=torch.float32).reshape(2, 4, 3)
    weight = torch.tensor([1.0, 0.5, 2.0, 3.0])
    bias = torch.tensor([0.0, 1.0, -1.0, 2.0])
    variables = {"x": values, "weight": weight, "bias": bias}

    torch.testing.assert_close(
        eval_expr("group_norm(x, 2)", variables),
        torch.nn.functional.group_norm(values, 2),
    )
    torch.testing.assert_close(
        eval_expr("group_norm(x, 2, weight, bias, 0.01)", variables),
        torch.nn.functional.group_norm(values, 2, weight, bias, eps=0.01),
    )
    assert "group_norm" in INBUILT_FUNCTIONS

    with pytest.raises(ValueError, match="divide the channel count"):
        eval_expr("group_norm(x, 3)", variables)
    with pytest.raises(ValueError, match="weight must have shape"):
        eval_expr("group_norm(x, 2, [1, 2])", variables)
    with pytest.raises(ValueError, match="eps must be a positive finite scalar"):
        eval_expr("group_norm(x, 2, none, none, 0)", variables)

def test_group_norm_preserves_float8_dtype():
    float8_dtypes = [
        getattr(torch, name, None)
        for name in ("float8_e4m3fn", "float8_e4m3fnuz", "float8_e5m2", "float8_e5m2fnuz")
    ]
    for dtype in (dtype for dtype in float8_dtypes if dtype is not None):
        values = torch.randn(2, 4, 3).to(dtype)
        result = eval_expr("group_norm(x, 2)", {"x": values})
        assert result.dtype == dtype

def test_slerp_interpolates_direction_and_magnitude():
    a = torch.tensor([2.0, 0.0])
    b = torch.tensor([0.0, 4.0])
    result = eval_expr("slerp(a, b, 0.5)", {"a": a, "b": b})
    torch.testing.assert_close(result, torch.tensor([3.0 / math.sqrt(2.0), 3.0 / math.sqrt(2.0)]))
    torch.testing.assert_close(eval_expr("slerp(a, b, 0)", {"a": a, "b": b}), a)
    torch.testing.assert_close(eval_expr("slerp(a, b, 1)", {"a": a, "b": b}), b)

    batch_a = torch.tensor([[1.0, 0.0], [2.0, 0.0]])
    batch_b = torch.tensor([[0.0, 1.0], [0.0, 2.0]])
    torch.testing.assert_close(
        eval_expr("slerp(a, b, t, 1)", {"a": batch_a, "b": batch_b, "t": torch.tensor([0.0, 1.0])}),
        torch.tensor([[1.0, 0.0], [0.0, 2.0]]),
    )

    whole_a = torch.tensor([[1.0, 0.0], [0.0, 0.0]])
    whole_b = torch.tensor([[0.0, 0.0], [0.0, 1.0]])
    torch.testing.assert_close(
        eval_expr("slerp(a, b, 0.5)", {"a": whole_a, "b": whole_b}),
        torch.tensor([[1.0 / math.sqrt(2.0), 0.0], [0.0, 1.0 / math.sqrt(2.0)]]),
    )

    a_by_column = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
    b_by_column = torch.tensor([[0.0, 2.0], [2.0, 0.0]])
    torch.testing.assert_close(
        eval_expr("slerp(a, b, 0.5, 0)", {"a": a_by_column, "b": b_by_column}),
        torch.full((2, 2), 1.5 / math.sqrt(2.0)),
    )

    antipodal = eval_expr("slerp([1, 0], [-4, 0], 0.5)")
    assert torch.isfinite(antipodal).all()
    torch.testing.assert_close(torch.linalg.vector_norm(antipodal), torch.tensor(2.5))
    torch.testing.assert_close(eval_expr("slerp([0, 0], [0, 4], 0.5)"), torch.tensor([0.0, 2.0]))
    assert "slerp" in INBUILT_FUNCTIONS

def test_slerp_validates_broadcasting_and_preserves_float8_dtype():
    with pytest.raises(ValueError, match="inputs must be broadcastable"):
        eval_expr("slerp([1, 2], [1, 2, 3], 0.5)")
    with pytest.raises(ValueError, match="t must broadcast"):
        eval_expr("slerp([[1, 0], [0, 1]], [[0, 1], [1, 0]], [1, 2, 3])")

    float8_dtypes = [
        getattr(torch, name, None)
        for name in ("float8_e4m3fn", "float8_e4m3fnuz", "float8_e5m2", "float8_e5m2fnuz")
    ]
    for dtype in (dtype for dtype in float8_dtypes if dtype is not None):
        values = torch.randn(2, 3).to(dtype)
        result = eval_expr("slerp(a, b, 0.5)", {"a": values, "b": values})
        assert result.dtype == dtype

def test_sinc_and_erfc():
    assert {"sinc", "erfc"} <= INBUILT_FUNCTIONS
    assert eval_expr("sinc(0)") == 1.0
    assert abs(eval_expr("sinc(0.5)") - 2.0 / math.pi) < 1e-6
    assert abs(eval_expr("sinc(1)")) < 1e-6
    assert eval_expr("erfc(0)") == 1.0
    assert math.isclose(eval_expr("erfc(1)"), math.erfc(1), rel_tol=1e-6)
    torch.testing.assert_close(
        eval_expr("sinc(x)", {"x": torch.tensor([0.0, 0.5, 1.0])}),
        torch.sinc(torch.tensor([0.0, 0.5, 1.0])),
    )
    torch.testing.assert_close(
        eval_expr("erfc(x)", {"x": torch.tensor([-1.0, 0.0, 1.0])}),
        torch.special.erfc(torch.tensor([-1.0, 0.0, 1.0])),
    )
    assert eval_expr("sinc([0, 0.5])") == [1.0, 2.0 / math.pi]
    float8_dtypes = [
        getattr(torch, name, None)
        for name in ("float8_e4m3fn", "float8_e4m3fnuz", "float8_e5m2", "float8_e5m2fnuz")
    ]
    for dtype in (dtype for dtype in float8_dtypes if dtype is not None):
        values = torch.tensor([0.0, 0.5, 1.0]).to(dtype)
        assert eval_expr("sinc(x)", {"x": values}).dtype == dtype
        assert eval_expr("erfc(x)", {"x": values}).dtype == dtype

if __name__ == "__main__":
    test_logic_functions()
    test_spatial_functions()
    test_stats_functions()
    test_easing_functions()
    test_lerp_fix()
    test_sinc_and_erfc()
    print("All new function tests passed!")
