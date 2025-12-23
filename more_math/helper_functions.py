from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
from antlr4 import CommonTokenStream

import torch

def getIndexTensorAlongDim(tensor, dim):
    shape = tensor.shape

    # Create values: shape (size of dim)
    values = torch.arange(shape[dim], dtype=torch.float32)

    # Reshape values to align with the target dimension
    view_shape = [1] * len(shape)
    view_shape[dim] = shape[dim]
    values = values.view(*view_shape)

    # Broadcast to full shape
    return values.expand(*shape)

def time_to_freq(element: torch.Tensor) -> torch.Tensor:
    if element.ndim < 2:
        raise ValueError("FFT requires at least 2 dimensions (Batch, Channel)")
    dims = tuple(range(2, element.ndim))
    return torch.fft.fftn(element, dim=dims)

def freq_to_time(element: torch.Tensor) -> torch.Tensor:
    if element.ndim < 2:
        raise ValueError("IFFT requires at least 2 dimensions (Batch, Channel)")
    dims = tuple(range(2, element.ndim))
    return torch.fft.ifftn(element, dim=dims).real

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError(f"Syntax error in expression at line {line}, col {column}: {msg}")


def comonLazy(expr, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
    variables = {'a':a,'b':b,'c':c,'d':d,'w':w,'x':x,'y':y,'z':z}
    need_eval = []
    print(a,b,c,d,w,x,y,z)
    input_stream = InputStream(expr)

    lexer = MathExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()
    for token in filter(lambda t: t.type == MathExprParser.VARIABLE, stream.tokens):
        if token.text in variables and variables[token.text] is None:
            need_eval.append(token.text)
    return need_eval