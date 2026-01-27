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

def test_ternary_scalar_truthy():
    expr = "1 ? 10 : 20"
    tree = parse_expr(expr)
    visitor = UnifiedMathVisitor({}, (1,))
    res = visitor.visit(tree)
    assert res == 10

def test_ternary_scalar_falsy():
    expr = "0 ? 10 : 20"
    tree = parse_expr(expr)
    visitor = UnifiedMathVisitor({}, (1,))
    res = visitor.visit(tree)
    assert res == 20

def test_ternary_tensor():
    # cond: [1, 0, 1]
    # T1: [5, 5, 5]
    # T2: [8, 8, 8]
    # Result should be [5, 8, 5]
    cond = torch.tensor([1, 0, 1])
    t1 = torch.tensor([5, 5, 5])
    t2 = torch.tensor([8, 8, 8])

    expr = "C ? T1 : T2"
    tree = parse_expr(expr)
    visitor = UnifiedMathVisitor({"C": cond, "T1": t1, "T2": t2}, (3,))
    res = visitor.visit(tree)

    expected = torch.tensor([5, 8, 5])
    assert torch.allclose(res, expected)

def test_ternary_lazy_evaluation():
    # Test that the branch not taken is not evaluated (no crash)
    # Using a divide by zero in the false branch
    expr = "1 ? 10 : (5/0)"
    tree = parse_expr(expr)
    visitor = UnifiedMathVisitor({}, (1,))
    res = visitor.visit(tree)
    assert res == 10

def test_ternary_complex_condition():
    # 5 > 3 is true -> 100
    expr = "(5 > 3) ? 100 : 200"
    tree = parse_expr(expr)
    visitor = UnifiedMathVisitor({}, (1,))
    res = visitor.visit(tree)
    assert res == 100

if __name__ == "__main__":
    test_ternary_scalar_truthy()
    test_ternary_scalar_falsy()
    test_ternary_tensor()
    test_ternary_lazy_evaluation()
    test_ternary_complex_condition()
    print("All ternary tests passed!")
