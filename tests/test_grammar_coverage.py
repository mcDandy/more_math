import torch
import math
import sys
import os

# Add parent dir to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from more_math.helper_functions import eval_tensor_expr, eval_float_expr


def test_all_functions():
    # Setup some test data
    a_val = 2.0
    b_val = 3.0
    tensor_a = torch.tensor([1.0, 2.0, 3.0])
    tensor_b = torch.tensor([0.5, 1.5, 2.5])

    variables = {"a": a_val, "b": b_val, "ta": tensor_a, "tb": tensor_b, "x": 0.5, "y": 1.0, "z": 2.0}

    # helper for assertions
    def check(expr, expected_scalar=None, vars=variables):
        # Test scalar
        res_s = eval_float_expr(expr, vars)
        if expected_scalar is not None:
            if isinstance(res_s, (int, float)):
                assert abs(res_s - expected_scalar) < 1e-4, f"Scalar {expr} failed: {res_s} != {expected_scalar}"
            # if expected is tensor we check differently

        # Test tensor
        res_t = eval_tensor_expr(expr, vars, (3,))
        assert torch.is_tensor(res_t) or isinstance(res_t, (list, int, float))
        return res_s, res_t

    print("--- Testing Basic Unary Functions ---")
    check("sin(0)", 0.0)
    check("cos(0)", 1.0)
    check("tan(0)", 0.0)
    check("asin(0)", 0.0)
    check("acos(1)", 0.0)
    check("atan(0)", 0.0)
    check("sinh(0)", 0.0)
    check("cosh(0)", 1.0)
    check("tanh(0)", 0.0)
    check("asinh(0)", 0.0)
    # acosh(1) = 0
    check("acosh(1)", 0.0)
    check("atanh(0)", 0.0)

    check("abs(-5)", 5.0)
    check("| -10 |", 10.0)  # AbsExp
    check("sqrt(16)", 4.0)
    check("ln(e)", 1.0)
    check("log(100)", 2.0)
    check("exp(1)", math.e)

    check("floor(1.9)", 1.0)
    check("ceil(1.1)", 2.0)
    check("round(1.5)", 2.0)
    check("gamma(3)", 2.0)  # gamma(n) = (n-1)!
    check("sigm(0)", 0.5)

    check("fract(1.25)", 0.25)
    check("relu(-5)", 0.0)
    check("relu(5)", 5.0)
    check("softplus(0)", math.log(2.0))
    # gelu(0) = 0
    check("gelu(0)", 0.0)
    check("sign(-10)", -1.0)
    check("sign(10)", 1.0)
    check("angle(ta)")  # test complex angle? no, just ensuring it runs

    print("--- Testing Two-Arg Functions ---")
    check("pow(2, 3)", 8.0)
    check("atan2(1, 1)", math.pi / 4)
    check("tmin(5, 10)", 5.0)
    check("tmax(5, 10)", 10.0)
    check("step(0.5, 0.2)", 1.0)  # step(x, edge) = 1 if x>=edge
    check("step(0.1, 0.2)", 0.0)

    print("--- Testing Operators ---")
    check("1 + 2", 3.0)
    check("5 - 3", 2.0)
    check("2 * 4", 8.0)
    check("10 / 2", 5.0)
    check("7 % 3", 1.0)
    check("2 ^ 3", 8.0)

    print("--- Testing Boolean/Comparison ---")
    check("5 > 3", 1.0)
    check("5 < 3", 0.0)
    check("5 >= 5", 1.0)
    check("5 <= 4", 0.0)
    check("2 == 2", 1.0)
    check("2 != 3", 1.0)

    print("--- Testing Ternary/N-ary ---")
    check("clamp(5, 0, 10)", 5.0)
    check("clamp(-5, 0, 10)", 0.0)
    check("lerp(0, 10, 0.5)", 5.0)
    check("smoothstep(0.5, 0, 1)", 0.5)  # smoothstep(x, edge0, edge1)

    check("smin(1, 2, 3, 0)", 0.0)
    check("smax(1, 5, 2)", 5.0)

    print("--- Testing Tensor Specifics (Norm, Map, Conv, FFT) ---")
    # Verify abs(x) vs |x|
    res_abs_func = eval_tensor_expr("abs(ta)", variables, (3,))
    assert torch.equal(res_abs_func, torch.abs(tensor_a))

    res_abs_exp = eval_tensor_expr("|ta|", variables, (3,))
    assert torch.is_tensor(res_abs_exp) and res_abs_exp.numel() == 1
    assert torch.allclose(res_abs_exp, torch.linalg.norm(tensor_a))

    check("tnorm(ta)")
    check("snorm(ta)")
    check("map(ta, x)")  # 1D map
    # Verify conv with kernel variables kW
    check("conv(reshape(ta, [1, 3]), 3, kW)")  # 1D conv, Input [1, 3] (Channels=1, Width=3)
    check("permute(ta, [0])")
    check("reshape(ta, [3, 1])")

    # FFT/IFFT
    # We need a shape for FFT usually
    eval_tensor_expr("fft(ta)", variables, (3,))
    res_ifft = eval_tensor_expr("ifft(fft(ta))", variables, (3,))
    assert torch.allclose(res_ifft, tensor_a, atol=1e-4)

    # Multi-dim Permute
    tensor_2d = torch.randn(2, 3)
    vars_2d = {"t2": tensor_2d}
    res_perm = eval_tensor_expr("permute(t2, [1, 0])", vars_2d, (3, 2))
    assert res_perm.shape == (3, 2)

    print("--- Testing List and Constants ---")
    check("[1, 2, 3] + 1")
    check("pi", math.pi)
    check("e", math.e)
    check("print(1)", 1.0)
    check("pshp(ta)")

    print("--- Testing Swap ---")
    # swap(tensor, dim, i, j)
    # ta = [1, 2, 3]
    # swap(ta, 0, 0, 2) -> [3, 2, 1]
    res_swap = eval_tensor_expr("swap(ta, 0, 0, 2)", variables, (3,))
    assert torch.equal(res_swap, torch.tensor([3.0, 2.0, 1.0]))

    print("All coverage tests passed!")


if __name__ == "__main__":
    test_all_functions()
