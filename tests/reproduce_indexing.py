import torch
import unittest
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
import antlr4
from more_math.Parser.MathExprLexer import MathExprLexer
from more_math.Parser.MathExprParser import MathExprParser

class TestIndexing(unittest.TestCase):
    def evaluate(self, expr, variables):
        input_stream = antlr4.InputStream(expr)
        lexer = MathExprLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = MathExprParser(stream)
        tree = parser.start()
        visitor = UnifiedMathVisitor(variables)
        return visitor.visit(tree)

    def test_tensor_indexing(self):
        v = torch.randn(4, 4)
        variables = {'v': v}
        
        # Single index
        res = self.evaluate('v[0];', variables)
        self.assertTrue(torch.allclose(res, v[0]))
        
        # Tuple index
        res = self.evaluate('v[1, 2];', variables)
        self.assertEqual(res, float(v[1, 2]))
        
        # List selection
        res = self.evaluate('v[[0, 2]];', variables)
        self.assertTrue(torch.allclose(res, v[[0, 2]]))

    def test_list_indexing(self):
        l = [10, 20, 30, 40]
        variables = {'l': l}
        
        # Single index
        res = self.evaluate('l[0];', variables)
        self.assertEqual(res, 10)
        
        # Negative index
        res = self.evaluate('l[-1];', variables)
        self.assertEqual(res, 40)
        
        # List selection
        res = self.evaluate('l[[0, 2]];', variables)
        self.assertEqual(res, [10, 30])
        
        # Nested list indexing
        nl = [[1, 2], [3, 4]]
        variables['nl'] = nl
        res = self.evaluate('nl[1, 0];', variables)
        self.assertEqual(res, 3)

    def test_index_error(self):
        v = torch.randn(4)
        variables = {'v': v}
        try:
            self.evaluate('v[10];', variables)
        except Exception as e:
            print(f"Caught indexing error: {e}")
            self.assertIn("1:0:", str(e))

        l = [1, 2, 3]
        variables = {'l': l}
        try:
            self.evaluate('l[10];', variables)
        except Exception as e:
            print(f"Caught list indexing error: {e}")
            self.assertIn("1:0:", str(e))

if __name__ == '__main__':
    unittest.main()
