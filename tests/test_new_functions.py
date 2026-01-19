import torch
import pytest
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.MathExprLexer import MathExprLexer
from more_math.Parser.MathExprParser import MathExprParser
from antlr4 import InputStream, CommonTokenStream

def eval_math(expression, variables={}):
    lexer = MathExprLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    tree = parser.expr()
    visitor = UnifiedMathVisitor(variables)
    return visitor.visit(tree)

def test_cossim():
    a = torch.tensor([1.0, 0.0])
    b = torch.tensor([1.0, 0.0])
    # cossim([1,0], [1,0]) should be 1.0
    res = eval_math("cossim(a, b)", {'a': a, 'b': b})
    assert torch.isclose(res, torch.tensor(1.0))

    c = torch.tensor([0.0, 1.0])
    # cossim([1,0], [0,1]) should be 0.0
    res2 = eval_math("cossim(a, c)", {'a': a, 'c': c})
    assert torch.isclose(res2, torch.tensor(0.0), atol=1e-6)

    # Test list support
    res3 = eval_math("cossim([1,0], [0,1])")
    assert torch.isclose(res3, torch.tensor(0.0), atol=1e-6)

def test_flip():
    a = torch.tensor([[1, 2], [3, 4]])
    # flip(a, 0) -> [[3, 4], [1, 2]]
    res = eval_math("flip(a, 0)", {'a': a})
    expected = torch.tensor([[3, 4], [1, 2]])
    assert torch.equal(res, expected)

    # flip(a, 1) -> [[2, 1], [4, 3]]
    res2 = eval_math("flip(a, 1)", {'a': a})
    expected2 = torch.tensor([[2, 1], [4, 3]])
    assert torch.equal(res2, expected2)

    # Test list support for dims
    # flip(a, [0, 1]) -> [[4, 3], [2, 1]]
    res3 = eval_math("flip(a, [0, 1])", {'a': a})
    expected3 = torch.tensor([[4, 3], [2, 1]])
    assert torch.equal(res3, expected3)

def test_cov():
    # Covariance of identical vectors should be variance
    a = torch.tensor([1.0, 2.0, 3.0])
    res = eval_math("cov(a, a)", {'a': a})
    expected = torch.var(a, correction=1).item()  # sample variance
    assert abs(res - expected)<1e-6

    # Covariance of roughly inverse
    b = torch.tensor([3.0, 2.0, 1.0])
    res2 = eval_math("cov(a, b)", {'a': a, 'b': b})
    # Cov(a,b) for a=[1,2,3], b=[3,2,1]:
    # means=2. sum((a-2)*(b-2)) = (-1*1 + 0*0 + 1*-1) = -2.
    # div by N-1=2 -> -1.0
    assert abs(res2 - -1.0)<1e-6

    # Test list
    res3 = eval_math("cov([1,2,3], [3,2,1])")
    assert abs(res3 - -1.0)<1e-6

    # Test mismatch error
    with pytest.raises(ValueError, match="same number of elements"):
        eval_math("cov([1,2], [1,2,3])")


def test_sort():
    a = torch.tensor([3.0, 1.0, 2.0])
    res = eval_math("sort(a)", {'a': a})
    expected = torch.tensor([1.0, 2.0, 3.0])
    assert torch.equal(res, expected)

    # Test list support
    res2 = eval_math("sort([3, 1, 2])")
    # Output of sort on list promoted to tensor is tensor
    assert torch.equal(res2, torch.tensor([1.0, 2.0, 3.0], device=res2.device))
