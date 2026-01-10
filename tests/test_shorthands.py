
import torch
import sys
import os

# Ensure we can import the module
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.MathExprLexer import MathExprLexer
from more_math.Parser.MathExprParser import MathExprParser
from antlr4 import InputStream, CommonTokenStream

def parse_and_visit(expr_str, variables):
    lexer = MathExprLexer(InputStream(expr_str))
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    tree = parser.expr()
    shape = (1, 1, 1, 1)  # Dummy shape
    visitor = UnifiedMathVisitor(variables, shape)
    return visitor.visit(tree)

def test_shorthamd_ezconv():
    t = torch.zeros((1, 10, 10, 3))
    t[:, 5, 5, :] = 1.0 
    vars = {"t": t}

    # ezconv should work exactly like ezconvolution
    expr = "ezconv(t, 3, 3, 1.0)"
    res = parse_and_visit(expr, vars)
    assert isinstance(res, torch.Tensor)
    assert res.shape == (1, 10, 10, 3)

def test_shorthand_conv():
    t = torch.zeros((1, 3, 10, 10))
    t[:, :, 5, 5] = 1.0
    vars = {"t": t}

    # conv should work exactly like convolution (strictly)
    expr = "conv(t, 3, 3, 1.0)"
    res = parse_and_visit(expr, vars)
    assert isinstance(res, torch.Tensor)
    assert res.shape == (1, 3, 10, 10)

def test_shorthand_print_shape():
    t = torch.zeros((1, 3))
    vars = {"t": t}

    # Test print_shape
    # visitor prints to stdout, we just check it runs and returns t
    res1 = parse_and_visit("print_shape(t)", vars)
    assert torch.equal(res1, t)

    # Test pshp
    res2 = parse_and_visit("pshp(t)", vars)
    assert torch.equal(res2, t)

def test_shorthand_perm():
    t = torch.randn((2, 3, 4))
    vars = {"t": t}
    # permute(t, [2, 0, 1])
    res_full = parse_and_visit("permute(t, [2, 0, 1])", vars)
    res_short = parse_and_visit("perm(t, [2, 0, 1])", vars)

    assert res_short.shape == (4, 2, 3)
    assert torch.equal(res_full, res_short)

def test_shorthand_rshp():
    t = torch.randn((2, 3, 4)) # 24 elements
    vars = {"t": t}
    # reshape(t, [24])
    res_full = parse_and_visit("reshape(t, [24])", vars)
    res_short = parse_and_visit("rshp(t, [24])", vars)

    assert res_short.shape == (24,)
    assert torch.equal(res_full, res_short)
