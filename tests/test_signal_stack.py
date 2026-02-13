import torch
import sys
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.MathExprLexer import MathExprLexer
from more_math.Parser.MathExprParser import MathExprParser
from antlr4 import InputStream, CommonTokenStream

def parse_and_visit(expr, variables, state_storage=None):
    from antlr4.error.ErrorListener import ErrorListener
    class ThrowingErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            raise Exception(f"line {line}:{column}: {msg}")

    input_stream = InputStream(expr)
    lexer = MathExprLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())

    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())

    tree = parser.start()

    visitor = UnifiedMathVisitor(variables, (1,), state_storage=state_storage)
    return visitor.visit(tree)

def test_all():
    with open("tests/test_debug.log", "w") as f_log:
        def log(msg):
            print(msg)
            f_log.write(msg + "\n")
            f_log.flush()

        # Mock the visitor's print if needed, but the trampoline prints to stdout.
        # We'll just run the tests and then read the log.
        log("Starting tests...")

        # 1. Return Bubbling
        program1 = "f(x) -> { return (x + (1 * 2 / 0.5)); }; f(10);"
        res1 = parse_and_visit(program1, {})
        log(f"Test 1 (Return): res={res1}, type={type(res1)}")
        assert abs(res1 - 14.0) < 1e-6

        # 2. Stack Storage
        state2 = [] 
        program2 = "stack_push(0, 42); stack_get(0);"
        res2 = parse_and_visit(program2, {}, state_storage=state2)
        log(f"Test 2 (Stack): res={res2}, type={type(res2)}")
        assert res2 == 42.0

        # 3. Block Cleanup
        variables3 = {"x": 1.0}
        program3 = "f() -> { { y = 10; return y; } }; f();"
        res3 = parse_and_visit(program3, variables3)
        log(f"Test 3 (Cleanup): res={res3}, type={type(res3)}")
        assert res3 == 10.0
        assert "y" not in variables3

        # 4. Break Bubbling
        program4 = "x = 0; while(x < 10) { z = (x > 2 ? break : 1); x = x + 1; } x;"
        res4 = parse_and_visit(program4, {})
        log(f"Test 4 (Break): res={res4}, type={type(res4)}")
        assert res4 == 3.0

        # 5. Count Function
        log("Test 5 (Count): list, tensor, scalar")
        assert parse_and_visit("count([1, 2, 3])", {}) == 3.0
        assert parse_and_visit("cnt([1, 2, 3])", {}) == 3.0
        assert parse_and_visit("length([1, 2, 3])", {}) == 3.0

        t = torch.randn(5, 10)
        assert parse_and_visit("count(t)", {"t": t}) == 5.0
        assert parse_and_visit("count(42)", {}) == 1.0
        
        # 6. Tensor Function
        log("Test 6 (Tensor): creation")
        t_empty = parse_and_visit("tensor([2, 3], 1.5)", {})
        assert t_empty.shape == (2, 3)
        assert torch.all(t_empty == 1.5)
        log(f"Test 6 (Tensor): shape={t_empty.shape}, value={t_empty[0,0]}")
        
        # 7. Batch Shuffle Function
        log("Test 7 (Shuffle): reordering")
        t_base = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]) # 3x2
        # shuffle(t, [0, 0, 2]) -> should be [[1,2], [1,2], [5,6]]
        t_shuffled = parse_and_visit("shuffle(t, [0, 0, 2])", {"t": t_base})
        assert t_shuffled.shape == (3, 2)
        assert t_shuffled[0, 0] == 1.0
        assert t_shuffled[1, 0] == 1.0
        assert t_shuffled[2, 0] == 5.0
        log(f"Test 7 (Shuffle): shape={t_shuffled.shape}")

        log("All tests passed successfully!")

if __name__ == "__main__":
    try:
        test_all()
    except Exception as e:
        print(f"FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
