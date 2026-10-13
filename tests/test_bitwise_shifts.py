#!/usr/bin/env python3
"""
Test bitwise shift operators and bit count function
"""
import torch
import sys
sys.path.insert(0, 'custom_nodes/more_math')

from more_math.Parser.antlr_router import get_antlr_modules
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from antlr4 import InputStream, CommonTokenStream

MathExprLexer, MathExprParser, _ = get_antlr_modules()

def parse_and_evaluate(expression, variables=None):
    """Parse and evaluate a math expression"""
    if variables is None:
        variables = {}

    input_stream = InputStream(expression)
    lexer = MathExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    tree = parser.start()

    visitor = UnifiedMathVisitor(variables, device='cpu')
    result = visitor.visit(tree)
    return result

def test_bit_shifts():
    """Test scalar and chained integer shifts."""
    test_cases = [
        ("a << b", {"a": 5, "b": 2}, 20),
        ("a >> b", {"a": 20, "b": 2}, 5),
        ("x << 3", {"x": 4}, 32),  # 4 << 3 = 32
        ("x >> 2", {"x": 16}, 4),  # 16 >> 2 = 4
        ("(a << b) >> c", {"a": 8, "b": 2, "c": 3}, 4),
    ]

    for expr, vars, expected in test_cases:
        assert parse_and_evaluate(expr, vars) == expected

def test_bit_count():
    """Test scalar bit counts."""
    test_cases = [
        ("bitcount(5)", {}, 2),
        ("bitcount(15)", {}, 4),
        ("bitcount(7)", {}, 3),
        ("bitcount(255)", {}, 8),
        ("bitcount(0)", {}, 0),
        ("bitcount(x)", {"x": 31}, 5),  # 31 = 11111 = 5 bits set
    ]

    for expr, vars, expected in test_cases:
        assert parse_and_evaluate(expr, vars) == expected

def test_bit_shifts_with_tensors():
    """Test bitwise shifts with integer tensors."""
    vars = {
        "a": torch.tensor([1, 2, 4, 8], dtype=torch.int32),
        "shift": 2,
    }

    result = parse_and_evaluate("a << shift", vars)
    expected = torch.tensor([4, 8, 16, 32], dtype=torch.int32)
    assert torch.equal(result, expected)

    result = parse_and_evaluate("a >> shift", vars)
    expected = torch.tensor([0, 0, 1, 2], dtype=torch.int32)
    assert torch.equal(result, expected)

def test_bit_count_with_tensors():
    """Test bit counts with integer tensors."""
    vars = {
        "nums": torch.tensor([5, 15, 7, 255], dtype=torch.int32),
    }

    result = parse_and_evaluate("bitcount(nums)", vars)
    expected = torch.tensor([2, 4, 3, 8], dtype=torch.float32)
    assert torch.equal(result, expected)

def test_combinations():
    """Test combined shifts and bitwise functions."""
    test_cases = [
        ("bitcount(a << b)", {"a": 5, "b": 2}, 2),
        ("bor(a << b, c << d)", {"a": 5, "b": 2, "c": 3, "d": 4}, 52),
    ]

    for expr, vars, expected in test_cases:
        assert parse_and_evaluate(expr, vars) == expected

if __name__ == "__main__":
    test_bit_shifts()
    test_bit_count()
    test_bit_shifts_with_tensors()
    test_bit_count_with_tensors()
    test_combinations()

