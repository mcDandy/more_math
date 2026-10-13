import sys
import os

# Add the parent directory to sys.path so we can import more_math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from more_math.Parser.antlr_router import get_antlr_modules
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from antlr4 import CommonTokenStream, InputStream

MathExprLexer, MathExprParser, _ = get_antlr_modules()

def evaluate(expression, variables=None):
    if variables is None:
        variables = {}
    input_stream = InputStream(expression)
    lexer = MathExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    tree = parser.start()
    visitor = UnifiedMathVisitor(variables)
    return visitor.visit(tree)

def test_if_else():
    expr_if = "a = 1; b = 0; if (a > 0) { b = 10; } else { b = 20; }; b"
    assert evaluate(expr_if) == 10.0


def test_while_loop():
    expr_while = "i = 0; while (i < 5) { i = i + 1; }; i"
    assert evaluate(expr_while) == 5.0


def test_recursive_function():
    expr_fib = "f(n) -> { if(n <= 1) return n; return f(n-1) + f(n-2); }; f(7)"
    assert evaluate(expr_fib) == 13.0


def test_block_scope_removes_new_variables_but_preserves_assignments():
    expr_scope = "x = 1; { x = 2; y = 10; }; x"
    variables = {}
    assert evaluate(expr_scope, variables) == 2.0
    assert "y" not in variables


def test_existing_variable_assignment_persists_after_block():
    expr_scope2 = "x = 1; { x = x + 1; }; x"
    assert evaluate(expr_scope2) == 2.0
