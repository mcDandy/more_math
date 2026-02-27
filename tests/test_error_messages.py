import sys
import os
import torch

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
    tree = parser.start()
    visitor = UnifiedMathVisitor(variables, (1, 64, 64))
    return visitor.visit(tree)

def test_variable_not_found_error():
    try:
        parse_and_visit("x + 1", {})
    except ValueError as e:
        msg = str(e)
        assert "1:0: Variable 'x' not found" in msg
    else:
        raise AssertionError("Expected ValueError not raised")

def test_unknown_function_error():
    try:
        parse_and_visit("unknown_func(1)", {})
    except ValueError as e:
        msg = str(e)
        assert "1:0: Unknown function: unknown_func" in msg
    else:
        raise AssertionError("Expected ValueError not raised")

def test_get_value_invalid_arg_error():
    try:
        parse_and_visit("get_value(1, [0])", {})
    except ValueError as e:
        msg = str(e)
        assert "1:0: get_value expects a tensor as first argument" in msg
    else:
        raise AssertionError("Expected ValueError not raised")

def test_conv_arg_count_error():
    try:
        parse_and_visit("conv(1, 1)", {})
    except ValueError as e:
        msg = str(e)
        assert "1:0: conv() requires at least 3 arguments" in msg
    else:
        raise AssertionError("Expected ValueError not raised")

def test_pop_empty_slot_error():
    try:
        parse_and_visit("stack_pop(0)", {})
    except ValueError as e:
        msg = str(e)
        assert "1:0: Pop from empty slot: 0" in msg
    else:
        raise AssertionError("Expected ValueError not raised")

def test_indexed_assignment_not_found_error():
    # Indexed assignment y[0] = 1; requires statement context
    # Try with semicolon and proper statement syntax
    try:
        parse_and_visit("y[0] = 1;", {})
    except ValueError as e:
        msg = str(e)
        assert "Variable 'y' not found" in msg or "not found for indexed assignment" in msg
    else:
        raise AssertionError("Expected ValueError not raised")

def run_tests():
    tests = [
        test_variable_not_found_error,
        test_unknown_function_error,
        test_get_value_invalid_arg_error,
        test_conv_arg_count_error,
        test_pop_empty_slot_error,
        test_indexed_assignment_not_found_error
    ]
    passed = 0
    for test in tests:
        print(f"Running {test.__name__}...")
        try:
            test()
            print("  PASSED")
            passed += 1
        except Exception as e:
            print(f"  FAILED: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{passed}/{len(tests)} tests passed.")
    if passed < len(tests):
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
