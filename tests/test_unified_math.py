import sys
import os
import torch
import math

# Ensure we can import the module
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)


# Import visitor
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.MathExprLexer import MathExprLexer
from more_math.Parser.MathExprParser import MathExprParser
from antlr4 import InputStream, CommonTokenStream


def parse_and_visit(expr_str, variables):
    lexer = MathExprLexer(InputStream(expr_str))
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    tree = parser.start()

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
    res_sinh = parse_and_visit("sinh(t)", vars)
    if isinstance(res_sinh, float): res_sinh = torch.tensor([res_sinh])
    assert torch.allclose(res_sinh, torch.tensor([0.0]))

    res_cosh = parse_and_visit("cosh(t)", vars)
    if isinstance(res_cosh, float): res_cosh = torch.tensor([res_cosh])
    assert torch.allclose(res_cosh, torch.tensor([1.0]))


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
    p = [2, 0, 1]  # 0->2, 1->0, 2->1
    vars = {"p": p}
    res = parse_and_visit("pinv(p)", vars)
    assert isinstance(res, list)
    # Inverse: if perm[i]=j, then inv[j]=i
    # perm[0]=2 -> inv[2]=0
    # perm[1]=0 -> inv[0]=1
    # perm[2]=1 -> inv[1]=2
    assert res == [1, 2, 0]

    # Tensor permutation inverse
    pt = torch.tensor([2, 0, 1])
    vars["pt"] = pt
    res_t = parse_and_visit("pinv(pt)", vars)
    assert isinstance(res_t, torch.Tensor)
    assert torch.equal(res_t, torch.tensor([1, 2, 0]))

def test_pinv_identity():
    perm = [2,0,1,6,4,3,5]
    tensor = torch.rand([11,14,32,21,4,3,1])
    varbl = {'c':tensor,'a':perm}
    res = parse_and_visit("permute(permute(c,a),pinv(a))",varbl)
    assert torch.equal(tensor,res)


def test_quartil():
    # Test Quartiles (Strict Integer Indices)
    # List: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (11 elements)
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    vars = {"l": l}

    assert parse_and_visit("quartile(l, 0)", vars) == 0.0
    assert parse_and_visit("quartile(l, 1)", vars) == 2.5
    assert parse_and_visit("quartile(l, 2)", vars) == 5.0
    assert parse_and_visit("quartile(l, 3)", vars) == 7.5
    assert parse_and_visit("quartile(l, 4)", vars) == 10.0

    # Tensor
    t = torch.tensor(l, dtype=torch.float32)
    vars["t"] = t

    res_q2 = parse_and_visit("quartile(t, 2)", vars)
    if not isinstance(res_q2, torch.Tensor): res_q2 = torch.tensor(res_q2)
    assert torch.allclose(res_q2, torch.tensor(5.0))

    res_q1 = parse_and_visit("quartile(t, 1)", vars)
    if not isinstance(res_q1, torch.Tensor): res_q1 = torch.tensor(res_q1)
    assert torch.allclose(res_q1, torch.tensor(2.5))

    # Float inputs for quartil should be cast to int, so 0.5 -> 0 -> Min
    # verifying strict behavior or fallback
    assert parse_and_visit("quartile(l, 0.9)", vars) == 0.0


def test_percentile():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    vars = {"l": l}
    t = torch.tensor(l, dtype=torch.float32)
    vars["t"] = t

    # Percentile (0 - 100)
    assert parse_and_visit("percentile(l, 50)", vars) == 5.0 # Median
    assert parse_and_visit("percentile(l, 25)", vars) == 2.5 # Q1

    res_p75 = parse_and_visit("percentile(t, 75)", vars)
    if not isinstance(res_p75, torch.Tensor): res_p75 = torch.tensor(res_p75)
    assert torch.allclose(res_p75, torch.tensor(7.5))

    # Aliases
    assert parse_and_visit("prcnt(l, 50)", vars) == 5.0


def test_custom_functions():
    vars = {}

    # 1. Simple function definition and call
    # f(x) -> x + 1; f(10)
    expr1 = "f(x) -> x + 1; f(10)"
    assert parse_and_visit(expr1, vars) == 11.0

    # 2. Multi-arg function
    # add(a, b) -> a + b; add(3, 4)
    expr2 = "add(a, b) -> a + b; add(3, 4)"
    assert parse_and_visit(expr2, vars) == 7.0

    # 3. Function reusing other functions (simulated by defining in same block)
    # sq(x) -> x * x; sumsq(a, b) -> sq(a) + sq(b); sumsq(3, 4)
    expr3 = "sq(x) -> x * x; sumsq(a, b) -> sq(a) + sq(b); sumsq(3, 4)"
    assert parse_and_visit(expr3, vars) == 25.0

    # 4. Global variable access & Shadowing
    # x = 10 (global)
    # f(x) -> x * 2; f(5) -> should be 10, not 20
    vars = {"x": 10.0}
    expr4 = "f(x) -> x * 2; f(5)"
    assert parse_and_visit(expr4, vars) == 10.0

    # f(y) -> x + y; f(5) -> global x(10) + param y(5) = 15
    expr5 = "f(y) -> x + y; f(5)"
    assert parse_and_visit(expr5, vars) == 15.0

def test_append():
    vars = {}

    # 1. Append scalar to list
    assert parse_and_visit("append([1, 2], 3)", vars) == [1.0, 2.0, 3.0]

    # 2. Append list to list (concat)
    assert parse_and_visit("append([1], [2, 3])", vars) == [1.0, 2.0, 3.0]

    # 3. Scalar a, list b
    assert parse_and_visit("append(0, [1, 2])", vars) == [0.0, 1.0, 2.0]

    # 4. Tensors
    t1 = torch.tensor([1.0, 2.0])
    t2 = torch.tensor([3.0])
    vars = {"t1": t1, "t2": t2}
    res = parse_and_visit("append(t1, t2)", vars)
    assert torch.equal(res, torch.tensor([1.0, 2.0, 3.0]))

    # 5. Tensor and scalar (promoted)
    res2 = parse_and_visit("append(t1, 4)", vars)
    assert torch.equal(res2, torch.tensor([1.0, 2.0, 4.0]))

def test_random_generators():
    # We pass a shape to have non-scalar results
    vars = {}

    # Use parse_and_visit to test full stack

    # 1. randn / noise (Normal distribution)
    res_n = parse_and_visit("randn(123)", vars)
    assert isinstance(res_n, torch.Tensor)
    assert res_n.shape == (1, 1, 1, 1) # Default shape from parse_and_visit

    res_noise = parse_and_visit("noise(123)", vars)
    assert torch.equal(res_n, res_noise) # Same seed should give same results

    # 2. rand (Uniform distribution [0, 1))
    res_u = parse_and_visit("rand(123)", vars)
    assert res_u.shape == (1, 1, 1, 1)
    assert torch.all(res_u >= 0) and torch.all(res_u < 1)

    # 3. rande / exponential
    res_e = parse_and_visit("rande(123, 1.0)", vars)
    assert res_e.shape == (1, 1, 1, 1)
    assert torch.all(res_e >= 0)

    res_exp = parse_and_visit("random_exponential(123, 1.0)", vars)
    assert torch.equal(res_e, res_exp)

    # 4. randc / cauchy
    res_c = parse_and_visit("randc(123, 0.0, 1.0)", vars)
    assert res_c.shape == (1, 1, 1, 1)

    res_cauchy = parse_and_visit("random_cauchy(123, 0.0, 1.0)", vars)
    assert torch.equal(res_c, res_cauchy)

    # 5. randln / log_normal
    res_ln = parse_and_visit("randln(123, 0.0, 1.0)", vars)
    assert res_ln.shape == (1, 1, 1, 1)
    assert torch.all(res_ln > 0)

    res_lognorm = parse_and_visit("random_log_normal(123, 0.0, 1.0)", vars)
    assert torch.equal(res_ln, res_lognorm)

    # 6. randb / bernoulli
    res_b = parse_and_visit("randb(123, 0.5)", vars)
    assert res_b.shape == (1, 1, 1, 1)
    assert torch.all((res_b == 0) | (res_b == 1))

    # 7. randp / poisson
    res_p = parse_and_visit("randp(123, 5.0)", vars)
    assert res_p.shape == (1, 1, 1, 1)
    assert torch.all(res_p >= 0)

def test_recursion_and_depth():
    vars = {}
    # 1. Test recursion depth (100 levels)
    # f(i) -> i == 0 ? 0 : f(i-1) + 1; f(100)
    expr_rec = "f(i) -> i == 0 ? 0 : f(i-1) + 1; f(100)"
    assert parse_and_visit(expr_rec, vars) == 100.0

    # 2. Test 'depth' variable
    # g(i) -> i == 0 ? depth : g(i-1); g(10)
    # g(10) is depth 1, g(0) is depth 11
    expr_depth = "g(i) -> i == 0 ? depth : g(i-1); g(10)"
    assert parse_and_visit(expr_depth, vars) == 11.0

    # 3. Test scope stack (shadowing with recursion)
    # x = 100
    # h(x, i) -> i == 0 ? x : h(x + 1, i - 1); h(0, 5)
    # Should result in 5, not affected by global x=100 or previous levels' x in a broken way
    vars = {"x": 100.0}
    expr_scope = "h(x, i) -> i == 0 ? x : h(x + 1, i - 1); h(0, 5)"
    assert parse_and_visit(expr_scope, vars) == 5.0

def test_new_loop_features():
    vars = {}

    # 1. Test FOR loop with range() (list)
    # x = 0; for(i in range(0, 5, 1)) x = x + i; x
    expr1 = "x = 0; for(i in range(0, 5, 1)) x = x + i; x"
    assert parse_and_visit(expr1, vars) == 10.0

    # 2. Test FOR loop with list
    # x = 1; for(i in [1, 2, 3]) x = x * i; x
    expr2 = "x = 1; for(i in [1, 2, 3]) x = x * i; x"
    assert parse_and_visit(expr2, vars) == 6.0

    # 3. Test get_value (2D tensor)
    # T = [[1, 2], [3, 4]] -> pos=[1, 0] -> 3
    t = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    vars = {"T": t}
    # get_value(T, [1, 0])
    expr3 = "get_value(T, [1, 0])"
    res3 = parse_and_visit(expr3, vars)
    assert res3 == 3.0

    # get_value(T, [0, 1]) -> 2
    assert parse_and_visit("get_value(T, [0, 1])", vars) == 2.0

    # 4. Test crop
    # crop(T, [0, 0], [1, 1]) -> [[1]]
    res4 = parse_and_visit("crop(T, [0, 0], [1, 1])", vars)
    assert torch.equal(res4, torch.tensor([[1.0]]))

    # crop(T, [0, 0], [2, 2]) -> T
    res5 = parse_and_visit("crop(T, [0, 0], [2, 2])", vars)
    assert torch.equal(res5, t)

    # 5. Test crop with padding (zeros)
    # crop(T, [1, 1], [2, 2]) -> [[4, 0], [0, 0]]
    # T at [1,1] is 4. Size [2,2].
    # Row 1 (from T[1]): [4, T[1,2](out)] -> [4, 0]
    # Row 2 (from T[2]): [0, 0]
    expected_pad = torch.tensor([[4.0, 0.0], [0.0, 0.0]])
    res6 = parse_and_visit("crop(T, [1, 1], [2, 2])", vars)
    assert torch.equal(res6, expected_pad)

def test_entropy():
    """Test entropy function for information entropy calculation."""
    vars = {}
    
    # 1. Test uniform distribution (maximum entropy)
    # Uniform probabilities should have high entropy
    uniform = torch.ones(4) / 4.0  # [0.25, 0.25, 0.25, 0.25]
    vars["uniform"] = uniform
    entropy_uniform = parse_and_visit("entropy(uniform)", vars)
    assert isinstance(entropy_uniform, float)
    # For uniform distribution of 4 elements: H = -sum(0.25 * log(0.25)) = log(4) ≈ 1.386
    assert 1.3 < entropy_uniform < 1.5
    
    # 2. Test deterministic distribution (minimum entropy)
    # One probability is 1, others are 0 -> entropy should be near 0
    deterministic = torch.tensor([1000.0, -1000.0, -1000.0, -1000.0])  # After softmax: ~[1, 0, 0, 0]
    vars["deterministic"] = deterministic
    entropy_det = parse_and_visit("entropy(deterministic)", vars)
    assert isinstance(entropy_det, float)
    assert entropy_det < 0.1  # Near zero entropy
    
    # 3. Test with different tensor sizes
    small = torch.randn(8)
    vars["small"] = small
    entropy_small = parse_and_visit("entropy(small)", vars)
    assert isinstance(entropy_small, float)
    assert entropy_small > 0  # Should be positive
    
    # 4. Test that entropy is always non-negative
    random_vals = torch.randn(100)
    vars["random_vals"] = random_vals
    entropy_random = parse_and_visit("entropy(random_vals)", vars)
    assert entropy_random >= 0

def test_correlation():
    """Test correlation (Pearson correlation coefficient) function."""
    vars = {}
    
    # 1. Perfect positive correlation
    x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
    y = torch.tensor([2.0, 4.0, 6.0, 8.0, 10.0])  # y = 2*x
    vars["x"] = x
    vars["y"] = y
    corr_perfect = parse_and_visit("corr(x, y)", vars)
    assert isinstance(corr_perfect, float)
    assert abs(corr_perfect - 1.0) < 1e-5  # Should be very close to 1
    
    # Test with alias
    corr_alias = parse_and_visit("correlation(x, y)", vars)
    assert abs(corr_alias - 1.0) < 1e-5
    
    # 2. Perfect negative correlation
    z = torch.tensor([10.0, 8.0, 6.0, 4.0, 2.0])  # Decreasing
    vars["z"] = z
    corr_negative = parse_and_visit("corr(x, z)", vars)
    assert isinstance(corr_negative, float)
    assert abs(corr_negative - (-1.0)) < 1e-5  # Should be very close to -1
    
    # 3. No correlation (orthogonal)
    a = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
    b = torch.tensor([1.0, -1.0, 1.0, -1.0, 1.0])  # Oscillating
    vars["a"] = a
    vars["b"] = b
    corr_none = parse_and_visit("corr(a, b)", vars)
    assert isinstance(corr_none, float)
    assert abs(corr_none) < 0.5  # Low correlation
    
    # 4. Test with same tensor (should be 1.0)
    corr_self = parse_and_visit("corr(x, x)", vars)
    assert abs(corr_self - 1.0) < 1e-5
    
    # 5. Test with flattened 2D tensors
    t1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    t2 = torch.tensor([[1.5, 3.0], [4.5, 6.0]])  # Scaled version
    vars["t1"] = t1
    vars["t2"] = t2
    corr_2d = parse_and_visit("corr(t1, t2)", vars)
    assert isinstance(corr_2d, float)
    assert abs(corr_2d - 1.0) < 1e-5  # Linear relationship
    
    # 6. Test correlation is symmetric
    corr_xy = parse_and_visit("corr(x, y)", vars)
    corr_yx = parse_and_visit("corr(y, x)", vars)
    assert abs(corr_xy - corr_yx) < 1e-10  # Should be identical

def test_entropy_and_correlation_edge_cases():
    """Test edge cases for entropy and correlation."""
    vars = {}
    
    # 1. Entropy with constant values (after softmax becomes uniform)
    constant = torch.ones(10)
    vars["constant"] = constant
    entropy_const = parse_and_visit("entropy(constant)", vars)
    # All equal logits -> uniform distribution after softmax -> log(10) ≈ 2.302
    assert 2.2 < entropy_const < 2.4
    
    # 2. Correlation with constant values (undefined, but should handle gracefully)
    const_a = torch.ones(5) * 3.0
    const_b = torch.ones(5) * 5.0
    vars["const_a"] = const_a
    vars["const_b"] = const_b
    # Both have zero variance, correlation is undefined (0/0)
    # Implementation returns nan or 0
    corr_const = parse_and_visit("corr(const_a, const_b)", vars)
    # Check that it doesn't crash and returns a float
    assert isinstance(corr_const, float)
    
    # 3. Small tensors
    tiny_x = torch.tensor([1.0, 2.0])
    tiny_y = torch.tensor([2.0, 4.0])
    vars["tiny_x"] = tiny_x
    vars["tiny_y"] = tiny_y
    corr_tiny = parse_and_visit("corr(tiny_x, tiny_y)", vars)
    assert abs(corr_tiny - 1.0) < 1e-5

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
        test_pinv()
        test_quartil()
        test_percentile()
        test_custom_functions()
        test_append()
        test_random_generators()
        test_recursion_and_depth()
        test_new_loop_features()
        test_entropy()
        test_correlation()
        test_entropy_and_correlation_edge_cases()
        print("All UnifiedMathVisitor tests passed!")


    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
