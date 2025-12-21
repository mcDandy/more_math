from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream
from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser
from .Parser.TensorEvalVisitor import TensorEvalVisitor
from antlr4 import CommonTokenStream
import torch
from .helper_functions import getIndexTensorAlongDim, ThrowingErrorListener
import comfy.utils

def calculate_patches(Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
    # Parse expression
    input_stream = InputStream(Model)
    lexer = MathExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    parser.addErrorListener(ThrowingErrorListener())
    tree = parser.expr()

    sd_a = a.model.state_dict()
    sd_b = b.model.state_dict() if b is not None else {}
    sd_c = c.model.state_dict() if c is not None else {}
    sd_d = d.model.state_dict() if d is not None else {}

    patches = {}
    layer_count = len(sd_a)

    pbar = comfy.utils.ProgressBar(layer_count)

    # Iterate over all keys in the main model 'a'
    for i, (key, tens_a) in enumerate(sd_a.items()):
        # Get corresponding tensors from other models, defaulting to zeros if missing or models not provided
        tens_b = sd_b.get(key, None)
        if tens_b is None: tens_b = torch.zeros_like(tens_a,device=tens_a.device)
        else: tens_b = tens_b.to(tens_a.device)

        tens_c = sd_c.get(key, None)
        if tens_c is None: tens_c = torch.zeros_like(tens_a,device=tens_a.device)
        else: tens_c = tens_c.to(tens_a.device)

        tens_d = sd_d.get(key, None)
        if tens_d is None: tens_d = torch.zeros_like(tens_a,device=tens_a.device)
        else: tens_d = tens_d.to(tens_a.device)

        # Variables for the visitor
        variables = {
            'a': tens_a,
            'b': tens_b,
            'c': tens_c,
            'd': tens_d,
            'w': w, 'x': x, 'y': y, 'z': z,
            'L': i, 'layer': i,
            'LC': layer_count, 'layer_count': layer_count
        }

        for dim_idx in range(tens_a.ndim):
             idx_tensor = getIndexTensorAlongDim(tens_a, dim_idx)
             idx_tensor = idx_tensor.to(tens_a.device)
             variables[f'D{dim_idx}'] = idx_tensor
             variables[f'dim_{dim_idx}'] = idx_tensor

        visitor = TensorEvalVisitor(variables, tens_a.shape)
        result_tensor = visitor.visit(tree)

        # Calculate difference for patching
        # The patch should be: result - original
        # Because ComfyUI applies: original + patch
        diff = result_tensor - tens_a

        # Allow skipping zero patches to save memory
        if torch.all(diff == 0):
            continue

        # Store patch. ComfyUI expects { key: (tensor,) } usually
        patches[key] = (diff,)

        pbar.update(1)

    return patches