#!/usr/bin/env python

"""Tests for `more_math` package."""

import pytest
from src.more_math.nodes import ConditioningMathNode

@pytest.fixture
def example_node():
    """Fixture to create an Example node instance."""
    return ConditioningMathNode()

def test_example_node_initialization(example_node):
    """Test that the node can be instantiated."""
    assert isinstance(example_node, ConditioningMathNode)

def test_return_types():
    """Test the node's metadata."""
    assert ConditioningMathNode.RETURN_TYPES == ("IMAGE",)
    assert ConditioningMathNode.FUNCTION == "test"
    assert ConditioningMathNode.CATEGORY == "Example"
