from antlr4 import InputStream, CommonTokenStream
from more_math.Parser.MathExprLexer import MathExprLexer
from more_math.Parser.MathExprParser import MathExprParser
import sys

def test_expr(expr):
    print(f"Testing: {expr}")
    input_stream = InputStream(expr)
    lexer = MathExprLexer(input_stream)
    # Redirect stderr to catch ANTLR errors
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    
    class ErrorCountListener:
        def __init__(self):
            self.count = 0
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Error at {line}:{column}: {msg}")
            self.count += 1
            
    listener = ErrorCountListener()
    parser.removeErrorListeners()
    parser.addErrorListener(listener)
    
    tree = parser.start()
    if listener.count > 0:
        print("FAILED")
    else:
        print("PASSED")

if __name__ == "__main__":
    test_expr("1+1")
    test_expr("1+1;")
    test_expr("x = 1; x")
    test_expr("x = 1; x;")
