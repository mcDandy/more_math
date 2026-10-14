import torch
import sys
import os
import math
import pytest

# Ensure we can import the module
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.antlr_router import get_antlr_modules
from more_math.Parser.inbuilt_symbols import INBUILT_FUNCTIONS, INBUILT_KEYWORDS
from antlr4 import InputStream, CommonTokenStream

MathExprLexer, MathExprParser, _ = get_antlr_modules()

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

@pytest.mark.parametrize("function", ("mean", "std", "var"))
@pytest.mark.parametrize("dimension", ("0", "-1", "[0, 1]"))
def test_statistic_uses_requested_dimensions(function, dimension):
    values = torch.tensor([[1.0, 3.0, 5.0], [2.0, 4.0, 8.0]])
    if dimension == "[0, 1]":
        expected = getattr(torch, function)(values.float(), dim=(0, 1))
    else:
        expected = getattr(torch, function)(values.float(), dim=int(dimension))

    result = parse_and_visit(f"{function}(t, {dimension})", {"t": values})

    if isinstance(expected, torch.Tensor) and expected.numel() == 1:
        expected = expected.item()
    if isinstance(result, torch.Tensor):
        torch.testing.assert_close(result, expected)
    else:
        assert math.isclose(result, expected, rel_tol=1e-5)

def test_std():
    t = torch.tensor([1.0, 5.0]) # mean=3, var=((2^2 + 2^2)/1) = 8. std = sqrt(8)=2.828...
    vars = {"t": t, "l": [1.0, 5.0]}

    res_t = parse_and_visit("std(t)", vars)
    # Result might be float or tensor with .item()
    val_t = res_t.item() if hasattr(res_t, 'item') else res_t
    assert math.isclose(val_t, math.sqrt(8), rel_tol=1e-5)
    assert math.isclose(parse_and_visit("std(l)", vars), math.sqrt(8), rel_tol=1e-5)

def test_var():
    t = torch.tensor([1.0, 5.0]) 
    vars = {"t": t, "l": [1.0, 5.0]}
    res_t = parse_and_visit("var(t)", vars)
    # Result might be float or tensor with .item()
    val_t = res_t.item() if hasattr(res_t, 'item') else res_t
    assert math.isclose(val_t, 8.0, rel_tol=1e-5)
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

def test_isclose_and_allclose_are_functions():
    a = torch.tensor([1.0, 2.0])
    b = torch.tensor([1.0, 2.000001])

    assert "isclose" in INBUILT_FUNCTIONS
    assert "allclose" in INBUILT_FUNCTIONS
    assert "isclose" not in INBUILT_KEYWORDS
    assert "allclose" not in INBUILT_KEYWORDS
    torch.testing.assert_close(parse_and_visit("isclose(a, b)", {"a": a, "b": b}), torch.tensor([1.0, 1.0]))
    assert parse_and_visit("allclose(a, b)", {"a": a, "b": b}) == 1.0

def test_order_statistics_support_dimensions():
    values = torch.tensor([[1.0, 3.0, 3.0], [2.0, 2.0, 8.0]])
    variables = {"t": values}

    torch.testing.assert_close(parse_and_visit("median(t, 0)", variables), torch.tensor([1.0, 2.0, 3.0]))
    torch.testing.assert_close(parse_and_visit("mode(t, 1)", variables), torch.tensor([3.0, 2.0]))
    torch.testing.assert_close(parse_and_visit("quantile(t, 0.5, 0)", variables), torch.tensor([1.5, 2.5, 5.5]))
    torch.testing.assert_close(parse_and_visit("percentile(t, 50, 1)", variables), torch.tensor([3.0, 2.0]))
    torch.testing.assert_close(parse_and_visit("quartile(t, 2, 1)", variables), torch.tensor([3.0, 2.0]))

    torch.testing.assert_close(parse_and_visit("argmin(t, 0, 1)", variables), torch.tensor([0, 0]))
    torch.testing.assert_close(parse_and_visit("argmax(t, 0, 1)", variables), torch.tensor([1, 2]))
    torch.testing.assert_close(parse_and_visit("topk_ind(t, 1, 1)", variables), torch.tensor([[1], [2]]))
    torch.testing.assert_close(parse_and_visit("botk_ind(t, 1, 1)", variables), torch.tensor([[0], [0]]))
    torch.testing.assert_close(
        parse_and_visit("topk(t, 1, 1)", variables),
        torch.tensor([[0.0, 3.0, 0.0], [0.0, 0.0, 8.0]]),
    )

def test_weighted_mean_and_losses():
    values = torch.tensor([[1.0, 3.0], [2.0, 4.0]])
    weights = torch.tensor([[1.0, 3.0], [3.0, 1.0]])
    variables = {"x": values, "w": weights}
    torch.testing.assert_close(parse_and_visit("weighted_mean(x, w)", variables), torch.tensor(2.5))
    torch.testing.assert_close(parse_and_visit("weighted_mean(x, w, 1)", variables), torch.tensor([2.5, 2.5]))
    torch.testing.assert_close(parse_and_visit("weighted_mean(x, w, 0)", variables), torch.tensor([1.75, 3.25]))

    prediction = torch.tensor([0.0, 2.0])
    target = torch.tensor([1.0, 0.0])
    torch.testing.assert_close(
        parse_and_visit("huber_loss(prediction, target)", {"prediction": prediction, "target": target}),
        torch.tensor(1.0),
    )
    assert parse_and_visit("huber_loss(0, 2, 0.5, 'sum')", {}) == 0.875
    with pytest.raises(ValueError, match="delta must be a positive"):
        parse_and_visit("huber_loss(0, 1, 0)", {})
    with pytest.raises(ValueError, match="weights must have a non-zero sum"):
        parse_and_visit("weighted_mean([1, 2], [1, -1])", {})

    logits = torch.tensor([[2.0, 0.0], [0.0, 2.0]])
    labels = torch.tensor([0, 1])
    expected = torch.nn.functional.cross_entropy(logits, labels)
    torch.testing.assert_close(
        parse_and_visit("cross_entropy(logits, labels)", {"logits": logits, "labels": labels}),
        expected,
    )
    probabilities = torch.nn.functional.one_hot(labels, num_classes=2).float()
    torch.testing.assert_close(
        parse_and_visit("cross_entropy(logits, probabilities, 1, 'sum')", {"logits": logits, "probabilities": probabilities}),
        torch.nn.functional.cross_entropy(logits, probabilities, reduction="sum"),
    )

