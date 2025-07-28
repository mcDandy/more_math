#!/usr/bin/env python

"""Tests for `more_math` package."""

import pytest
from src.more_math.ConditioningMathNode import ConditioningMathNode
from src.more_math.LatentMathNode import LatentMathNode
from src.more_math.ImageMathNode import ImageMathNode
import tokenize
from io import StringIO

def tokenize_expression(expr):
    if not expr.endswith('\n'):
        expr = expr + '\n'
    f = StringIO(expr)
    tokens = tokenize.generate_tokens(f.readline)
    filtered_tokens = []
    for toktype, tokval, _, _, _ in tokens:
        token_name = tokenize.tok_name[toktype]
        # Opravíme ERRORTOKEN na OP pro !, &, |, ^
        if token_name == 'ERRORTOKEN' and tokval in {'!', '&', '|', '^'}:
            token_name = 'OP'
        if token_name in {'COMMENT', 'NL', 'NEWLINE', 'INDENT', 'DEDENT'}:
            continue
        filtered_tokens.append((token_name, tokval.strip()))
    return filtered_tokens

def test_conditioning_math_node_initialization():
    node = ConditioningMathNode()
    assert isinstance(node, ConditioningMathNode)

def test_conditioning_math_node_metadata():
    assert ConditioningMathNode.RETURN_TYPES == ("CONDITIONING",)
    assert ConditioningMathNode.FUNCTION == "condMathNode"
    assert ConditioningMathNode.CATEGORY == "More math"

def test_latent_math_node_initialization():
    node = LatentMathNode()
    assert isinstance(node, LatentMathNode)

def test_latent_math_node_metadata():
    assert LatentMathNode.RETURN_TYPES == ("LATENT",)
    assert LatentMathNode.FUNCTION == "latMathNode"
    assert LatentMathNode.CATEGORY == "More math"

def test_image_math_node_initialization():
    node = ImageMathNode()
    assert isinstance(node, ImageMathNode)

def test_image_math_node_metadata():
    assert ImageMathNode.RETURN_TYPES == ("IMAGE",)
    assert ImageMathNode.FUNCTION == "imgMathNode"
    assert ImageMathNode.CATEGORY == "More math"


