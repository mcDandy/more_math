import torch
import sys
import os

# Add the parent directory to sys.path so we can import more_math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.MathExprLexer import MathExprLexer
from more_math.Parser.MathExprParser import MathExprParser
from antlr4 import CommonTokenStream, InputStream

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

if __name__ == "__main__":
    # 1. Test If-Else
    expr_if = "a = 1; b = 0; if (a > 0) { b = 10; } else { b = 20; }; b"
    res_if = evaluate(expr_if)
    print(f"If-Else Test: b={res_if} (expected 10.0)")

    # 2. Test While Loop
    expr_while = "i = 0; while (i < 5) { i = i + 1; }; i"
    res_while = evaluate(expr_while)
    print(f"While Loop Test: i={res_while} (expected 5.0)")

    # 3. Test Function with Return and Recursion
    # Fibonacci: f(n) -> { if(n <= 1) return n; return f(n-1) + f(n-2); }; f(7)
    # Fib(7): 0, 1, 1, 2, 3, 5, 8, 13
    expr_fib = "f(n) -> { if(n <= 1) return n; return f(n-1) + f(n-2); }; f(7)"
    res_fib = evaluate(expr_fib)
    print(f"Recursive Fib Test: f(7)={res_fib} (expected 13.0)")

    # 4. Test Isolated Block Scoping
    # Variables defined inside blocks should not leak to outer scope
    expr_scope = "x = 1; { x = 2; y = 10; }; x"
    # x should be modified to 2 inside block, but reverts to 1 after block
    # y should not be accessible outside block
    res_scope = evaluate(expr_scope)
    print(f"Isolated Scope Test: x={res_scope} (expected 1.0)")
    # 4b. Test that modifications to existing variables persist
    expr_scope2 = "x = 1; { x = x + 1; }; x"
    res_scope2 = evaluate(expr_scope2)
    print(f"Modified Variable Test: x={res_scope2} (expected 2.0)")

    # 5. Test Return from top level
    expr_top_return = "a = 10; return a + 1; 20"
    res_top_return = evaluate(expr_top_return)
    print(f"Top-level Return Test: {res_top_return} (expected 11.0)")

    # 6. Test Deep Recursion with Procedural logic
    # f(i) -> { if (i <= 0) return depth; return f(i-1); }; f(2000)
    # Recursion limit is 10000, so 2000 should pass.
    expr_deep = "f(i) -> { if (i <= 0) return depth; return f(i-1); }; f(2000)"
    res_deep = evaluate(expr_deep)
    print(f"Deep Recursion Test: f(2000)={res_deep} (expected 2001.0)")
