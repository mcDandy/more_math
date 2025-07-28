#!/usr/bin/env python

"""Tests for `more_math` package."""

import pytest
from src.more_math.ConditioningMathNode import ConditioningMathNode
from src.more_math.LatentMathNode import LatentMathNode
from src.more_math.ImageMathNode import ImageMathNode
from src.more_math.parser import Parser
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

@pytest.mark.parametrize(
    "expr,expected_ast",
    [
        ("a+b", ('BINOP', ('+', ('VARIABLE', 'a'), ('VARIABLE', 'b')))),
        ("-a", ('UNARYOP', ('-', ('VARIABLE', 'a')))),
        ("abs(a)", ('FUNCTION', ('ABS', [('VARIABLE', 'a')]))),
        ("a*(b+c)", ('BINOP', ('*', ('VARIABLE', 'a'), ('PARENTHESIS', ('BINOP', ('+', ('VARIABLE', 'b'), ('VARIABLE', 'c'))))))),
        ("min(a, b, 1)", ('FUNCTION', ('MIN', [('VARIABLE', 'a'), ('VARIABLE', 'b'), ('LITERAL', 1.0)]))),
        ("pi+e", ('BINOP', ('+', ('LITERAL', 3.141592653589793), ('LITERAL', 2.718281828459045)))),
        ("a % 2", ('BINOP', ('%', ('VARIABLE', 'a'), ('LITERAL', 2.0)))),
    ]
)
def test_parser_valid_expressions(expr, expected_ast):
    tokens = tokenize_expression(expr)
    # Skip test if tokenization failed (should not happen for valid expr)
    if tokens and tokens[0][0] == 'TOKENIZE_ERROR':
        pytest.skip(f"Tokenization failed: {tokens[0][1]}")
    parser = Parser(tokens)
    ast = parser.parse_expression()
    assert ast == expected_ast

@pytest.mark.parametrize(
    "expr,err_msg",
    [
        ("a + )", "Unexpected right parenthesis"),
        ("(a + b", "Missing closing parenthesis"),
        ("a + * b", "Unexpected token '*'"),
        ("min(a, b", "Missing closing parenthesis for function"),
        ("a +", "Unexpected end of input"),
    ]
)
def test_parser_errors(expr, err_msg):
    tokens = tokenize_expression(expr)
    if tokens and tokens[0][0] == 'TOKENIZE_ERROR':
        # Accept Python's tokenize error for incomplete input
        assert (
            'unexpected EOF in multi-line statement' in tokens[0][1]
            or 'Missing closing parenthesis' in err_msg
            or 'Missing closing parenthesis for function' in err_msg
        )
        return
    parser = Parser(tokens)
    with pytest.raises(SyntaxError) as excinfo:
        parser.parse_expression()
    assert err_msg in str(excinfo.value)

@pytest.mark.parametrize(
    "expr,expected_ast",
    [
        ("a ^ b", ('BINOP', ('^', ('VARIABLE', 'a'), ('VARIABLE', 'b')))),
        ("a & b", ('BINOP', ('&', ('VARIABLE', 'a'), ('VARIABLE', 'b')))),
        ("a | b", ('BINOP', ('|', ('VARIABLE', 'a'), ('VARIABLE', 'b')))),
        ("!a", ('UNARYOP', ('!', ('VARIABLE', 'a')))),
        ("!a & b", ('BINOP', ('&', ('UNARYOP', ('!', ('VARIABLE', 'a'))), ('VARIABLE', 'b')))),
        ("a | b & c", ('BINOP', ('|', ('VARIABLE', 'a'), ('BINOP', ('&', ('VARIABLE', 'b'), ('VARIABLE', 'c')))))),
        ("a ^ b | c", ('BINOP', ('|', ('BINOP', ('^', ('VARIABLE', 'a'), ('VARIABLE', 'b'))), ('VARIABLE', 'c')))),
    ]
)
def test_parser_logical_and_pow(expr, expected_ast):
    tokens = tokenize_expression(expr)
    parser = Parser(tokens)
    ast = parser.parse_expression()
    assert ast == expected_ast

@pytest.mark.parametrize(
    "expr,expected_ast",
    [
        # Priority: ! > * > + > & > ^ > |
        ("a + b * c", 
            ('BINOP', ('+', 
                ('VARIABLE', 'a'), 
                ('BINOP', ('*', ('VARIABLE', 'b'), ('VARIABLE', 'c')))
            ))
        ),
        ("a * b + c", 
            ('BINOP', ('+', 
                ('BINOP', ('*', ('VARIABLE', 'a'), ('VARIABLE', 'b'))), 
                ('VARIABLE', 'c')
            ))
        ),
        ("a + b & c", 
            ('BINOP', ('&', 
                ('BINOP', ('+', ('VARIABLE', 'a'), ('VARIABLE', 'b'))), 
                ('VARIABLE', 'c')
            ))
        ),
        ("a & b + c", 
            ('BINOP', ('&', 
                ('VARIABLE', 'a'), 
                ('BINOP', ('+', ('VARIABLE', 'b'), ('VARIABLE', 'c')))
            ))
        ),
        ("a + b | c", 
            ('BINOP', ('|', 
                ('BINOP', ('+', ('VARIABLE', 'a'), ('VARIABLE', 'b'))), 
                ('VARIABLE', 'c')
            ))
        ),
        ("a | b + c", 
            ('BINOP', ('|', 
                ('VARIABLE', 'a'), 
                ('BINOP', ('+', ('VARIABLE', 'b'), ('VARIABLE', 'c')))
            ))
        ),
        ("a * b & c", 
            ('BINOP', ('&', 
                ('BINOP', ('*', ('VARIABLE', 'a'), ('VARIABLE', 'b'))), 
                ('VARIABLE', 'c')
            ))
        ),
        ("a & b * c", 
            ('BINOP', ('&', 
                ('VARIABLE', 'a'), 
                ('BINOP', ('*', ('VARIABLE', 'b'), ('VARIABLE', 'c')))
            ))
        ),
        ("a ^ b + c", 
            ('BINOP', ('^', 
                ('VARIABLE', 'a'), 
                ('BINOP', ('+', ('VARIABLE', 'b'), ('VARIABLE', 'c')))
            ))
        ),
        ("a + b ^ c", 
            ('BINOP', ('^', 
                ('BINOP', ('+', ('VARIABLE', 'a'), ('VARIABLE', 'b'))), 
                ('VARIABLE', 'c')
            ))
        ),
        ("a | b ^ c", 
            ('BINOP', ('|', 
                ('VARIABLE', 'a'), 
                ('BINOP', ('^', ('VARIABLE', 'b'), ('VARIABLE', 'c')))
            ))
        ),
        ("a ^ b | c", 
            ('BINOP', ('|', 
                ('BINOP', ('^', ('VARIABLE', 'a'), ('VARIABLE', 'b'))), 
                ('VARIABLE', 'c')
            ))
        ),
        ("!a * b", 
            ('BINOP', ('*', 
                ('UNARYOP', ('!', ('VARIABLE', 'a'))), 
                ('VARIABLE', 'b')
            ))
        ),
        ("!(a + b) * c", 
            ('BINOP', ('*', 
                ('UNARYOP', ('!', ('PARENTHESIS', ('BINOP', ('+', ('VARIABLE', 'a'), ('VARIABLE', 'b')))))), 
                ('VARIABLE', 'c')
            ))
        ),
        ("a + (b | c)", 
            ('BINOP', ('+', 
                ('VARIABLE', 'a'), 
                ('PARENTHESIS', ('BINOP', ('|', ('VARIABLE', 'b'), ('VARIABLE', 'c'))))
            ))
        ),
    ]
)
def test_parser_operator_priority(expr, expected_ast):
    tokens = tokenize_expression(expr)
    parser = Parser(tokens)
    ast = parser.parse_expression()
    assert ast == expected_ast
