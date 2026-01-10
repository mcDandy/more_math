
import torch
import sys
import os
import math

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

def test_sum():
    vars = {"t": torch.tensor([1.0, 2.0, 3.0]), "l": [1.0, 2.0, 3.0], "s": 5.0}
    assert parse_and_visit("sum(t)", vars) == 6.0
    assert parse_and_visit("sum(l)", vars) == 6.0
    assert parse_and_visit("sum(s)", vars) == 5.0

def test_mean():
    vars = {"t": torch.tensor([1.0, 2.0, 3.0]), "l": [1.0, 2.0, 3.0], "s": 5.0}
    assert parse_and_visit("mean(t)", vars) == 2.0
    assert parse_and_visit("mean(l)", vars) == 2.0
    assert parse_and_visit("mean(s)", vars) == 5.0

def test_std():
    t = torch.tensor([1.0, 5.0]) # mean=3, var=((2^2 + 2^2)/1) = 8. std = sqrt(8)=2.828...
    vars = {"t": t, "l": [1.0, 5.0]}

    assert math.isclose(parse_and_visit("std(t)", vars).item(), math.sqrt(8), rel_tol=1e-5)
    assert math.isclose(parse_and_visit("std(l)", vars), math.sqrt(8), rel_tol=1e-5)

def test_var():
    t = torch.tensor([1.0, 5.0]) 
    vars = {"t": t, "l": [1.0, 5.0]}
    assert math.isclose(parse_and_visit("var(t)", vars).item(), 8.0, rel_tol=1e-5)
    assert math.isclose(parse_and_visit("var(l)", vars), 8.0, rel_tol=1e-5)

def test_dot():
    a = torch.tensor([1.0, 2.0])
    b = torch.tensor([3.0, 4.0])
    vars = {"a": a, "b": b}
    # dot = 1*3 + 2*4 = 3 + 8 = 11
    assert parse_and_visit("dot(a, b)", vars) == 11.0

    # Check flattening behavior (2D tensor)
    a2 = torch.tensor([[1.0, 2.0]])
    b2 = torch.tensor([[3.0], [4.0]]) # 2x1
    vars = {"a2": a2, "b2": b2}
    # a2 flat = [1, 2], b2 flat = [3, 4] -> dot=11
    assert parse_and_visit("dot(a2, b2)", vars) == 11.0

