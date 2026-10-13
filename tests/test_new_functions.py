import torch
import sys
import os
import math
import pytest

# Ensure test runner usage (Visual Studio) can import the package regardless of working dir.
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

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

if __name__ == "__main__":
    test_logic_functions()
    test_spatial_functions()
    test_stats_functions()
    test_easing_functions()
    test_lerp_fix()
    print("All new function tests passed!")
