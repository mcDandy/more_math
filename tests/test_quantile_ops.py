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
    shape = (1, 1, 1, 1)
    visitor = UnifiedMathVisitor(variables, shape)
    return visitor.visit(tree)

def test_quantile_basic():
    vars = {"t": torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0]), "l": [0, 1, 2, 3, 4]}
    
    # Quantile (0-1)
    assert parse_and_visit("quantile(t, 0.5)", vars) == 2.0
    assert parse_and_visit("quantile(l, 0.25)", vars) == 1.0
    assert parse_and_visit("quantile(t, 1.0)", vars) == 4.0
    assert parse_and_visit("quantile(l, 0)", vars) == 0.0

def test_percentile_basic():
    vars = {"t": torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0]), "l": [0, 1, 2, 3, 4]}
    
    # Percentile (0-100)
    assert parse_and_visit("percentile(t, 50)", vars) == 2.0
    assert parse_and_visit("percentile(l, 25)", vars) == 1.0
    assert parse_and_visit("percentile(t, 100)", vars) == 4.0
    assert parse_and_visit("percentile(l, 0)", vars) == 0.0

def test_quartile_basic():
    vars = {"t": torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0]), "l": [0, 1, 2, 3, 4]}
    
    # Quartile (0-4)
    assert parse_and_visit("quartile(t, 2)", vars) == 2.0
    assert parse_and_visit("quartile(l, 1)", vars) == 1.0
    assert parse_and_visit("quartile(t, 4)", vars) == 4.0
    assert parse_and_visit("quartile(l, 0)", vars) == 0.0
    
    # Alias
    assert parse_and_visit("quartil(t, 2)", vars) == 2.0

def test_tensor_queries():
    t = torch.tensor([0.0, 10.0, 20.0, 30.0, 40.0])
    q_tensor = torch.tensor([0.0, 0.5, 1.0])
    vars = {"t": t, "q": q_tensor}
    
    # Quantile with tensor q
    res = parse_and_visit("quantile(t, q)", vars)
    assert isinstance(res, torch.Tensor)
    assert torch.allclose(res, torch.tensor([0.0, 20.0, 40.0]))

    # Percentile with tensor p
    p_tensor = torch.tensor([0.0, 50.0, 100.0])
    vars["p"] = p_tensor
    res_p = parse_and_visit("percentile(t, p)", vars)
    assert torch.allclose(res_p, torch.tensor([0.0, 20.0, 40.0]))

def test_list_with_tensor_query():
    # Optimization: list input promoted to tensor for tensor query
    l = [0, 10, 20, 30, 40]
    q = torch.tensor([0.25, 0.75])
    vars = {"l": l, "q": q}
    
    res = parse_and_visit("quantile(l, q)", vars)
    assert isinstance(res, torch.Tensor)
    assert torch.allclose(res, torch.tensor([10.0, 30.0]))

def test_nd_tensor_query():
    # N-D tensor as query should reshape result
    t = torch.tensor([0.0, 100.0])
    q_nd = torch.zeros((2, 2, 2))
    q_nd[0, 0, 1] = 1.0 # Max
    q_nd[1, 1, 1] = 0.5 # Mid
    vars = {"t": t, "q": q_nd}
    
    res = parse_and_visit("quantile(t, q)", vars)
    assert res.shape == (2, 2, 2)
    assert res[0, 0, 0] == 0.0
    assert res[0, 0, 1] == 100.0
    assert res[1, 1, 1] == 50.0

def test_large_tensor_fallback():
    # Test that the fallback doesn't crash (we can't easily verify it *fell back* 
    # but we can verify it works on larger ones)
    # Using 1M for speed in regular tests, but enough to trust the logic
    size = 1_000_000
    t = torch.rand(size)
    vars = {"t": t}
    
    # Simple median
    res = parse_and_visit("quantile(t, 0.5)", vars)
    # torch.quantile(t, 0.5) should be very close to t.median()
    assert math.isclose(res.item(), t.median().item(), abs_tol=1e-3)

def test_list_query():
    # percentile(t, [0, 10, 20]) -> returns a list of results
    t = torch.tensor([0.0, 10.0, 20.0, 30.0, 40.0])
    vars = {"t": t}
    
    res = parse_and_visit("percentile(t, [0, 50, 100])", vars)
    assert isinstance(res, list)
    assert len(res) == 3
    assert res[0] == 0.0
    assert res[1] == 20.0
    assert res[2] == 40.0

if __name__ == "__main__":
    # If run as script
    try:
        test_quantile_basic()
        test_percentile_basic()
        test_quartile_basic()
        test_tensor_queries()
        test_list_with_tensor_query()
        test_nd_tensor_query()
        test_large_tensor_fallback()
        test_list_query()
        print("All quantile_ops tests passed!")
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)
