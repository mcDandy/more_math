import torch
import sys
import os

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
    tree = parser.expr()
    shape = (1, 1, 1, 1)
    visitor = UnifiedMathVisitor(variables, shape)
    return visitor.visit(tree)

def reproduce():
    print("Reproducing percentile(list, tensor)...")
    a = torch.rand(1, 4, 128, 128) * 100.0 # 0-100 range for percentile
    l = [0.1, 1.0, 0.3]

    vars = {"a": a, "l": l}
    # Note: percentile(l, a) -> a/100.0 will be 0-1.
    try:
        res = parse_and_visit("percentile(l, a)", vars)
        print(f"Success! Result type: {type(res)}, shape: {res.shape}")
    except Exception:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    reproduce()
