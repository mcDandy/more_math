import torch
import sys
import os

# Ensure test runner usage (Visual Studio) can import the package regardless of working dir.
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
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

if __name__ == "__main__":
    test_logic_functions()
    test_spatial_functions()
    test_stats_functions()
    test_easing_functions()
    test_lerp_fix()
    print("All new function tests passed!")
