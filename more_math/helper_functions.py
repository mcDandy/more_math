from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream, CommonTokenStream

import torch

from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser



class ThrowingErrorListener(ErrorListener):
    """Error listener that raises ValueError on syntax errors."""
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError(f"Syntax error in expression at line {line}, col {column}: {msg}")

def as_tensor(value,shape):
    if isinstance(value,torch.Tensor):
        return value
    if isinstance(value,(float,int)):
        value = (value,)
    return torch.broadcast_to(torch.Tensor(value),shape)

def parse_expr(expr: str):
    """Parse a math expression and return the parse tree."""
    input_stream = InputStream(expr)
    lexer = MathExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    parser.addErrorListener(ThrowingErrorListener())
    return parser.expr()


def eval_tensor_expr(expr: str, variables: dict, shape: tuple, device=None):
    """Parse and evaluate a tensor math expression."""
    from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
    tree = parse_expr(expr)
    visitor = UnifiedMathVisitor(variables, shape, device=device)
    return visitor.visit(tree)


def eval_tensor_expr_with_tree(tree, variables: dict, shape: tuple, device=None):
    """Evaluate a pre-parsed expression tree with UnifiedMathVisitor."""
    from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
    visitor = UnifiedMathVisitor(variables, shape, device=device)
    return visitor.visit(tree)


def eval_float_expr(expr: str, variables: dict):
    """Parse and evaluate a float math expression."""
    from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
    tree = parse_expr(expr)
    # Float eval context often has no shape. Pass None/Empty.
    visitor = UnifiedMathVisitor(variables, shape=None)
    return visitor.visit(tree)

def eval_float_expr_with_tree(tree, variables: dict):
    """Evaluate a pre-parsed expression tree with UnifiedMathVisitor."""
    from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
    visitor = UnifiedMathVisitor(variables, shape=None)
    return visitor.visit(tree)


def getIndexTensorAlongDim(tensor, dim):
    """Create a tensor of indices along a dimension, broadcasted to full shape."""
    shape = tensor.shape
    values = torch.arange(shape[dim], dtype=torch.float32, device=tensor.device)
    view_shape = [1] * len(shape)
    view_shape[dim] = shape[dim]
    values = values.view(*view_shape)
    return values.expand(*shape)


def comonLazy(expr, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
    """Determine which lazy inputs are needed based on expression variables."""
    variables = {'a': a, 'b': b, 'c': c, 'd': d, 'w': w, 'x': x, 'y': y, 'z': z}
    need_eval = []
    input_stream = InputStream(expr)
    lexer = MathExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()
    for token in filter(lambda t: t.type == MathExprParser.VARIABLE, stream.tokens):
        if token.text in variables and variables[token.text] is None:
            need_eval.append(token.text)
    return need_eval

def generate_dim_variables(tensor: torch.Tensor):
    """Generate index and size tensors for each dimension of the input tensor."""
    variables = {}
    for dim, size in enumerate(tensor.shape):
        variables[f'D{dim}'] = getIndexTensorAlongDim(tensor, dim)
        variables[f'S{dim}'] = torch.full(tensor.shape, fill_value=size, dtype=torch.float32, device=tensor.device)
    return variables

def make_zero_like(ref):
    """
    Create a zero-initialized version of the reference object, maintaining its structure.
    Handles Conditioning, Audio, Latent, VideoComponents, and Tensors.
    """
    if ref is None:
        return None

    # raw torch tensor
    if torch.is_tensor(ref):
        return torch.zeros_like(ref)

    # Conditioning: list of lists [[tensor, dict]]
    if isinstance(ref, list) and len(ref) > 0 and isinstance(ref[0], list) and len(ref[0]) >= 2:
        ref_tensor = ref[0][0]
        # Ensure it's a tensor-like structure
        if torch.is_tensor(ref_tensor):
            ref_pooled = ref[0][1].get("pooled_output")
            return [[
                torch.zeros_like(ref_tensor),
                {"pooled_output": torch.zeros_like(ref_pooled) if ref_pooled is not None else None}
            ]]

    # Audio or Latent: dict
    if isinstance(ref, dict):
        if 'waveform' in ref:  # Audio
            return {
                'waveform': torch.zeros_like(ref['waveform']),
                'sample_rate': ref['sample_rate']
            }
        if 'samples' in ref:  # Latent
            return {
                'samples': torch.zeros_like(ref['samples'])
            }

    # VideoComponents or other objects with images/audio attributes
    if hasattr(ref, 'images') and hasattr(ref, 'audio'):
        # Dynamically create same type (e.g. VideoComponents)
        return type(ref)(
            images=torch.zeros_like(ref.images),
            audio={'waveform': torch.zeros_like(ref.audio['waveform']), 'sample_rate': ref.audio['sample_rate']},
            frame_rate=ref.frame_rate,
            metadata=None
        )

    return None


# Legacy FFT functions (kept for backward compatibility, but now unused)
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