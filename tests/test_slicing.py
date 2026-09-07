"""Tests for tensor slicing functionality."""
import sys
import os
import torch
import pytest

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
    """Helper to parse and visit an expression."""
    lexer = MathExprLexer(InputStream(expr_str))
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    tree = parser.start()

    shape = (1, 1, 1, 1)
    visitor = UnifiedMathVisitor(variables, shape)
    return visitor.visit(tree)


class TestTensorSlicing:
    """Test tensor slicing operations."""

    def test_basic_slice_1d(self):
        """Test basic 1D tensor slicing."""
        t = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
        vars = {"t": t}

        # Test [1:3]
        result = parse_and_visit("t[1:3]", vars)
        assert torch.allclose(result, torch.tensor([2.0, 3.0]))

        # Test [0:2]
        result = parse_and_visit("t[0:2]", vars)
        assert torch.allclose(result, torch.tensor([1.0, 2.0]))

        # Test [2:]
        result = parse_and_visit("t[2:]", vars)
        assert torch.allclose(result, torch.tensor([3.0, 4.0, 5.0]))

        # Test [:3]
        result = parse_and_visit("t[:3]", vars)
        assert torch.allclose(result, torch.tensor([1.0, 2.0, 3.0]))

    def test_slice_with_step_1d(self):
        """Test 1D tensor slicing with step."""
        t = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        vars = {"t": t}

        # Test [::2]
        result = parse_and_visit("t[::2]", vars)
        assert torch.allclose(result, torch.tensor([1.0, 3.0, 5.0]))

        # Test [1::2]
        result = parse_and_visit("t[1::2]", vars)
        assert torch.allclose(result, torch.tensor([2.0, 4.0, 6.0]))

        # Test [0:4:2]
        result = parse_and_visit("t[0:4:2]", vars)
        assert torch.allclose(result, torch.tensor([1.0, 3.0]))

    def test_slice_2d(self):
        """Test 2D tensor slicing."""
        t = torch.tensor([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ])
        vars = {"t": t}

        # Test [0:2, 1:3]
        result = parse_and_visit("t[0:2, 1:3]", vars)
        expected = torch.tensor([[2.0, 3.0], [5.0, 6.0]])
        assert torch.allclose(result, expected)

        # Test [1:, :2]
        result = parse_and_visit("t[1:, :2]", vars)
        expected = torch.tensor([[4.0, 5.0], [7.0, 8.0]])
        assert torch.allclose(result, expected)

    def test_negative_indices(self):
        """Test slicing with negative indices."""
        t = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
        vars = {"t": t}

        # Test [-2:]
        result = parse_and_visit("t[-2:]", vars)
        assert torch.allclose(result, torch.tensor([4.0, 5.0]))

        # Test [:-2]
        result = parse_and_visit("t[:-2]", vars)
        assert torch.allclose(result, torch.tensor([1.0, 2.0, 3.0]))

    def test_indexing_still_works(self):
        """Test that regular indexing still works after slicing changes."""
        t = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
        vars = {"t": t}

        # Test [0]
        result = parse_and_visit("t[0]", vars)
        assert result == 1.0

        # Test [2]
        result = parse_and_visit("t[2]", vars)
        assert result == 3.0

        # Test [-1]
        result = parse_and_visit("t[-1]", vars)
        assert result == 5.0

    def test_list_slicing(self):
        """Test list slicing."""
        l = [1.0, 2.0, 3.0, 4.0, 5.0]
        vars = {"l": l}

        # Test [1:3]
        result = parse_and_visit("l[1:3]", vars)
        assert result == [2.0, 3.0]

        # Test [::2]
        result = parse_and_visit("l[::2]", vars)
        assert result == [1.0, 3.0, 5.0]

        # Test [-2:]
        result = parse_and_visit("l[-2:]", vars)
        assert result == [4.0, 5.0]

    def test_string_slicing(self):
        """Test string slicing."""
        s = "hello"
        vars = {"s": s}

        # Test [1:3]
        result = parse_and_visit("s[1:3]", vars)
        assert result == "el"

        # Test [::2]
        result = parse_and_visit("s[::2]", vars)
        assert result == "hlo"

        # Test [2:]
        result = parse_and_visit("s[2:]", vars)
        assert result == "llo"


class TestListAndTensorIndexing:
    """Test that existing indexing functionality still works."""

    def test_tensor_indexing_multi_dim(self):
        """Test multi-dimensional tensor indexing."""
        t = torch.arange(24).reshape(2, 3, 4).float()
        vars = {"t": t}

        # Test [0, 1, 2]
        result = parse_and_visit("t[0, 1, 2]", vars)
        assert result == 6.0

        # Test [1, 2, 3]
        result = parse_and_visit("t[1, 2, 3]", vars)
        assert result == 23.0

    def test_list_indexing(self):
        """Test list indexing."""
        l = [10, 20, 30, 40, 50]
        vars = {"l": l}

        # Test [0]
        result = parse_and_visit("l[0]", vars)
        assert result == 10

        # Test [3]
        result = parse_and_visit("l[3]", vars)
        assert result == 40

        # Test [-1]
        result = parse_and_visit("l[-1]", vars)
        assert result == 50


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
