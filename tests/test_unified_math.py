import sys
import os
import torch
import math

# Ensure we can import the module
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# Placeholder import - we will create this file next
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.MathExprLexer import MathExprLexer
from more_math.Parser.MathExprParser import MathExprParser
from antlr4 import InputStream, CommonTokenStream


def parse_and_visit(expr_str, variables):
    lexer = MathExprLexer(InputStream(expr_str))
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    tree = parser.expr()

    # We might need to pass shape/device if UnifiedMathVisitor requires it for tensor creation
    # For now assuming it can infer or defaults.
    # The original TensorEvalVisitor required shape. Unified might need it for "1.0" -> Tensor promotion cases?
    # Or maybe "1.0" stays scalar till needed?
    # Let's assume we pass a default shape/device if needed, but for scalar tests we might not need it.

    shape = (1, 1, 1, 1)  # Dummy shape
    visitor = UnifiedMathVisitor(variables, shape)
    return visitor.visit(tree)


def test_scalar_ops():
    vars = {"a": 2.0, "b": 3.0}

    assert parse_and_visit("a + b", vars) == 5.0
    assert parse_and_visit("a * b", vars) == 6.0
    assert parse_and_visit("sin(0)", vars) == 0.0
    assert parse_and_visit("smax(a, b)", vars) == 3.0
    assert parse_and_visit("step(2, 1)", vars) == 1.0
    assert parse_and_visit("step(0, 1)", vars) == 0.0
    assert parse_and_visit("clamp(5, 0, 10)", vars) == 5.0
    assert parse_and_visit("clamp(-5, 0, 10)", vars) == 0.0
    assert parse_and_visit("lerp(0, 10, 0.5)", vars) == 5.0
    assert parse_and_visit("fract(1.25)", vars) == 0.25

    # Type check - ensure they are python float/int, not tensor
    res = parse_and_visit("a + b", vars)
    assert isinstance(res, (float, int))


def test_tensor_ops():
    t1 = torch.tensor([1.0, 2.0])
    t2 = torch.tensor([3.0, 4.0])
    vars = {"t1": t1, "t2": t2, "s": 2.0}

    # Tensor + Tensor
    res = parse_and_visit("t1 + t2", vars)
    assert isinstance(res, torch.Tensor)
    assert torch.allclose(res, torch.tensor([4.0, 6.0]))

    # Tensor + Scalar
    res2 = parse_and_visit("t1 * s", vars)
    assert isinstance(res2, torch.Tensor)
    assert torch.allclose(res2, torch.tensor([2.0, 4.0]))

    # Scalar + Tensor
    res3 = parse_and_visit("s + t2", vars)
    assert isinstance(res3, torch.Tensor)
    assert torch.allclose(res3, torch.tensor([5.0, 6.0]))


def test_list_broadcasting():
    # Feature: List * Tensor -> Stack of Tensors
    t = torch.ones((2, 2))  # 2x2 ones
    l = [1.0, 2.0, 3.0]
    vars = {"t": t, "l": l}

    # l * t should produce a concatenation of 3 tensors: 1*t, 2*t, 3*t
    # Expected shape with torch.cat: (6, 2) - concatenates along existing dim
    res = parse_and_visit("l * t", vars)

    assert isinstance(res, torch.Tensor)
    assert res.shape == (6, 2)
    # With torch.cat along dim=0, the result is flattened:
    # [1*t[0], 1*t[1], 2*t[0], 2*t[1], 3*t[0], 3*t[1]]
    assert torch.allclose(res[0:2], t * 1.0)
    assert torch.allclose(res[2:4], t * 2.0)
    assert torch.allclose(res[4:6], t * 3.0)


def test_list_scalar_mapping():
    # Feature: List * Scalar -> List of results
    l = [1.0, 2.0, 3.0]
    vars = {"l": l}

    res = parse_and_visit("l * 2", vars)
    assert isinstance(res, list)
    assert res == [2.0, 4.0, 6.0]


def test_func_dispatch():
    t = torch.tensor([0.0, math.pi / 2])
    vars = {"t": t, "s": 0.0}

    # sin(tensor) -> tensor
    res_t = parse_and_visit("sin(t)", vars)
    assert isinstance(res_t, torch.Tensor)
    assert torch.allclose(res_t, torch.tensor([0.0, 1.0]))

    # sin(scalar) -> scalar
    res_s = parse_and_visit("sin(s)", vars)
    assert isinstance(res_s, float)
    assert abs(res_s) < 1e-6

    # sin(list) -> list
    l = [0.0, math.pi / 2]
    vars["l"] = l
    res_l = parse_and_visit("sin(l)", vars)
    assert isinstance(res_l, list)
    assert abs(res_l[0]) < 1e-6
    assert abs(res_l[1] - 1.0) < 1e-6


def test_power_ops():
    vars = {"a": 2.0, "b": 3.0}
    # Scalar ^ Scalar
    assert parse_and_visit("a ^ b", vars) == 8.0

    # Tensor ^ Scalar
    t = torch.tensor([2.0, 3.0])
    vars["t"] = t
    res = parse_and_visit("t ^ 2", vars)
    assert torch.allclose(res, torch.tensor([4.0, 9.0]))

    # Scalar ^ Tensor
    res2 = parse_and_visit("2 ^ t", vars)
    assert torch.allclose(res2, torch.tensor([4.0, 8.0]))


def test_hyperbolic_trig():
    vars = {"s": 0.0}
    assert parse_and_visit("sinh(s)", vars) == 0.0
    assert parse_and_visit("cosh(s)", vars) == 1.0
    assert parse_and_visit("tanh(s)", vars) == 0.0

    t = torch.tensor([0.0])
    vars["t"] = t
    assert torch.allclose(parse_and_visit("sinh(t)", vars), torch.tensor([0.0]))
    assert torch.allclose(parse_and_visit("cosh(t)", vars), torch.tensor([1.0]))


def test_kernel_coords():
    # Simulate visitConvFunc context
    # Usually grid variables are provided by the visitor during visitConvFunc
    # We can test if they are correctly handled if present in variables
    grid = torch.linspace(-1, 1, 3)
    vars = {"kx": grid, "ky": grid}

    # Test if expression using coordinates works
    res = parse_and_visit("kx^2 + ky^2", vars)
    assert isinstance(res, torch.Tensor)
    assert res.shape == grid.shape
    assert torch.allclose(res, grid**2 + grid**2)


def test_bool_ops():
    vars = {"a": 1, "b": 0}
    # Scalar bool
    assert parse_and_visit("a > b", vars) == 1
    assert parse_and_visit("a < b", vars) == 0

    # Tensor bool
    t1 = torch.tensor([1.0, 0.0])
    t2 = torch.tensor([0.0, 1.0])
    vars = {"t1": t1, "t2": t2}
    res = parse_and_visit("t1 > t2", vars)
    assert isinstance(res, torch.Tensor)
    assert torch.all(res == torch.tensor([1.0, 0.0]))


def test_topk():
    # Tensor topk
    t = torch.tensor([1.0, 5.0, 2.0, 8.0, 3.0])
    vars = {"t": t}
    # Tensor topk masking
    t = torch.tensor([1.0, 5.0, 2.0, 8.0, 3.0])
    vars = {"t": t}
    res = parse_and_visit("topk(t, 3)", vars)
    assert isinstance(res, torch.Tensor)
    assert res.shape == t.shape
    # Top 3 are 8, 5, 3. Masked result should be [0, 5, 0, 8, 3]
    expected = torch.tensor([0.0, 5.0, 0.0, 8.0, 3.0])
    assert torch.allclose(res, expected)
    assert res.is_contiguous()

    # Complex topk masking
    tc = torch.tensor([1.0+1j, 5.0+5j, 2.0+2j])
    vars["tc"] = tc
    res_c = parse_and_visit("topk(tc, 1)", vars)
    assert res_c.shape == tc.shape
    # Top 1 is 5+5j. Masked should be [0, 5+5j, 0]
    expected_c = torch.tensor([0.0+0j, 5.0+5j, 0.0+0j])
    assert torch.allclose(res_c, expected_c)


def test_botk():
    # Tensor botk masking (bottom k smallest values)
    t = torch.tensor([1.0, 5.0, 2.0, 8.0, 3.0])
    vars = {"t": t}
    res = parse_and_visit("botk(t, 3)", vars)
    assert isinstance(res, torch.Tensor)
    assert res.shape == t.shape
    # Bottom 3 are 1, 2, 3. Masked result should be [1, 0, 2, 0, 3]
    expected = torch.tensor([1.0, 0.0, 2.0, 0.0, 3.0])
    assert torch.allclose(res, expected)
    assert res.is_contiguous()

    # List botk
    l = [1.0, 5.0, 2.0, 8.0, 3.0]
    vars = {"l": l}
    res_l = parse_and_visit("botk(l, 2)", vars)
    assert isinstance(res_l, list)
    assert res_l == [1.0, 2.0]


def test_pinv():
    # List permutation inverse
    perm = [2, 0, 1]  # 0->2, 1->0, 2->1
    vars = {"perm": perm}
    res = parse_and_visit("pinv(perm)", vars)
    assert isinstance(res, list)
    # Inverse: if perm[i]=j, then inv[j]=i
    # perm[0]=2 -> inv[2]=0
    # perm[1]=0 -> inv[0]=1
    # perm[2]=1 -> inv[1]=2
    assert res == [1, 2, 0]

    # Tensor permutation inverse
    perm_t = torch.tensor([2, 0, 1])
    vars["perm_t"] = perm_t
    res_t = parse_and_visit("pinv(perm_t)", vars)
    assert isinstance(res_t, torch.Tensor)
    assert torch.equal(res_t, torch.tensor([1, 2, 0]))

def test_pinv_identity():
    perm = [2,0,1,6,4,3,5]
    tensor = torch.rand([11,14,32,21,4,3,1])
    varbl = {'c':tensor,'a':perm}
    res = parse_and_visit("permute(permute(c,a),pinv(a))",varbl)
    assert torch.equal(tensor,res)

if __name__ == "__main__":
    try:
        test_scalar_ops()
        test_tensor_ops()
        test_list_broadcasting()
        test_list_scalar_mapping()
        test_func_dispatch()
        test_power_ops()
        test_hyperbolic_trig()
        test_kernel_coords()
        test_bool_ops()
        test_topk()
        test_botk()
        test_pinv()
        print("All UnifiedMathVisitor tests passed!")
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
