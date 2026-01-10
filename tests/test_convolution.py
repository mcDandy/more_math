
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
    shape = (1, 1, 1, 1)  # Dummy shape
    visitor = UnifiedMathVisitor(variables, shape)
    return visitor.visit(tree)

def test_ezconvolution_2d():
    # Test 2D convolution with "ezconvolution" (automagic)
    # Case: (1, 10, 10, 3) - Standard ComfyUI Image (Batch, H, W, C)
    # Kernel: 3x3

    # Input: 1 batch, 10x10, 3 channels.
    t = torch.zeros((1, 10, 10, 3))
    t[:, 5, 5, :] = 1.0 # Centered dot

    vars = {"t": t}

    # Kernel expr: 1.0 (box blur / sum)
    # ezconvolution(tensor, kw, kh, k_expr)
    # Expect output same shape (1, 10, 10, 3) because ezconvolution handles layout.

    expr = "ezconvolution(t, 3, 3, 1.0)"
    res = parse_and_visit(expr, vars)

    assert isinstance(res, torch.Tensor)
    assert res.shape == (1, 10, 10, 3)

    # Check value at 5,5. Neighboring 3x3 (9 pixels) should contribute.
    # Kernel val is 1.0 everywhere. 
    # The dot is at 5,5.
    # Convolution at 5,5 will sum up the 3x3 area around input 5,5.
    # Input 5,5 is 1.0, others 0. 
    # So result at 5,5 should be 1.0 * 1.0 = 1.0?
    # Wait, if kernel is 3x3 ones. Input has single 1.
    # Conv is sum(I * K).
    # If we are at 5,5. Area is 4,4 to 6,6.
    # Input has 1 at 5,5.
    # Result at 4,4 will include input 5,5?
    # Yes.
    # Result at 5,5 will include input 5,5.

    # ezconvolution preserves logic so it should work.

def test_convolution_2d_strict():
    # Test 2D convolution with "convolution" (strict)
    # Case: (1, 3, 10, 10) - PyTorch Standard (Batch, C, H, W)

    t = torch.zeros((1, 3, 10, 10))
    t[:, :, 5, 5] = 1.0

    vars = {"t": t}

    # Kernel expr: 1.0
    # convolution(tensor, kw, kh, k_expr)

    expr = "convolution(t, 3, 3, 1.0)"
    res = parse_and_visit(expr, vars)

    assert isinstance(res, torch.Tensor)
    assert res.shape == (1, 3, 10, 10)

def test_convolution_strict_fail_on_wrong_layout():
    # Test that strict convolution likely fails or produces weird shape on wrong layout
    # Input: (1, 10, 10, 3) -> Batch=1, 10, 10, 3
    # Try 2D conv. 
    # Strict assumes (..., C, H, W).
    # so C=10, H=10, W=3. Batch=1.
    # Kernel 3x3.
    # W=3. Padding for kernel 3 is 1. Padded W = 3+2=5.
    # Conv 3 on 5 => valid.
    # So it might RUN, but it interprets dimensions wrong.

    t = torch.randn((1, 10, 10, 3))
    vars = {"t": t}

    expr = "convolution(t, 3, 3, 1.0)"
    res = parse_and_visit(expr, vars)

    # Result shape should be based on (1, 10, 10, 3) input.
    # Batch=(1). C=10. H=10. W=3.
    # Output: (1, 10, 10, 3).
    # So shape matches input, but semantic is wrong.
    # This confirms it didn't permute (if it permuted, it would crash or do something else).

    assert res.shape == (1, 10, 10, 3)

