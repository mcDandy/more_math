from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream, CommonTokenStream

import torch

from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser


class ThrowingErrorListener(ErrorListener):
    """Error listener that raises ValueError on syntax errors."""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError(f"Syntax error in expression at line {line}, col {column}: {msg}")


def as_tensor(value, shape):
    if getattr(value, "is_nested", False):
        return value
    if isinstance(value, torch.Tensor):
        # Pass tensors through unchanged; the expression defines the output shape.
        return value.contiguous()
    if isinstance(value, (float, int)):
        value = (value,)
    # If it's a scalar or list, broadcast to the reference shape provided.
    return torch.broadcast_to(torch.Tensor(value).to(dtype=torch.float32), shape).contiguous()


def parse_expr(expr: str):
    """Parse a math expression and return the parse tree."""
    input_stream = InputStream(expr)
    lexer = MathExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    parser.addErrorListener(ThrowingErrorListener())
    return parser.start()


def getIndexTensorAlongDim(tensor, dim):
    """Create a tensor of indices along a dimension, broadcasted to full shape."""
    shape = tensor.shape
    values = torch.arange(shape[dim], dtype=torch.float32, device=tensor.device)
    view_shape = [1] * len(shape)
    view_shape[dim] = shape[dim]
    values = values.view(*view_shape)
    return values.expand(*shape)


def commonLazy(expr, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
    """Determine which lazy inputs are needed based on expression variables."""
    variables = {"a": a, "b": b, "c": c, "d": d, "w": w, "x": x, "y": y, "z": z}
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
        variables[f"D{dim}"] = getIndexTensorAlongDim(tensor, dim)
        variables[f"S{dim}"] = torch.full(tensor.shape, fill_value=size, dtype=torch.float32, device=tensor.device)
    return variables


def prepare_inputs(a, b, c, d):
    """
    Ensures optional inputs b, c, d are zero-initialized like a if None.
    Returns the prepared (a, b, c, d).
    """
    b = b if b is not None else make_zero_like(a)
    c = c if c is not None else make_zero_like(a)
    d = d if d is not None else make_zero_like(a)
    return a, b, c, d


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

    # Conditioning: list of tuples [(tensor, dict)]
    if isinstance(ref, list) and len(ref) > 0 and isinstance(ref[0], (list, tuple)) and len(ref[0]) >= 2:
        zeroed_cond = []
        for entry in ref:
            ref_tensor = entry[0]
            ref_dict = entry[1]
            if torch.is_tensor(ref_tensor):
                new_dict = ref_dict.copy()
                if "pooled_output" in new_dict and torch.is_tensor(new_dict["pooled_output"]):
                    new_dict["pooled_output"] = torch.zeros_like(new_dict["pooled_output"])
                zeroed_cond.append((torch.zeros_like(ref_tensor), new_dict))
        return zeroed_cond

    # Audio or Latent: dict
    if isinstance(ref, dict):
        if "waveform" in ref:  # Audio
            return {"waveform": make_zero_like(ref["waveform"]), "sample_rate": ref["sample_rate"]}
        if "samples" in ref:  # Latent
            return {"samples": make_zero_like(ref["samples"])}

    # NestedTensor
    if getattr(ref, "is_nested", False):
        from comfy.nested_tensor import NestedTensor
        return NestedTensor([torch.zeros_like(t) for t in ref.tensors])

    # VideoComponents or other objects with images/audio attributes
    if hasattr(ref, "images") and hasattr(ref, "audio"):
        # Dynamically create same type (e.g. VideoComponents)
        return type(ref)(
            images=torch.zeros_like(ref.images),
            audio={"waveform": torch.zeros_like(ref.audio["waveform"]), "sample_rate": ref.audio["sample_rate"]},
            frame_rate=ref.frame_rate,
            metadata=None,
        )

    return None


def normalize_to_common_shape(*tensors, mode="pad"):
    """
    Normalize multiple tensors to a common shape.
    - mode="pad": Pad with zeros to the max shape.
    - mode="tile": Tile to match (or exceed) dimensions, then truncate excess.
    """
    if mode not in ("pad", "tile"):
        return tensors
    valid_tensors = [t for t in tensors if torch.is_tensor(t)]
    if len(valid_tensors) <= 1:
        return tensors

    # Check if all shapes are already the same
    if all(t.shape == valid_tensors[0].shape for t in valid_tensors[1:]):
        return tensors

    # Determine common shape
    target_ndim = max(t.ndim for t in valid_tensors)
    max_shape = [0] * target_ndim

    for t in valid_tensors:
        for i in range(t.ndim):
            # Align from trailing dimensions
            max_shape[-(i + 1)] = max(max_shape[-(i + 1)], t.shape[-(i + 1)])

    target_shape = tuple(max_shape)

    def normalize_one(t, shape):
        if t.shape == shape:
            return t.contiguous()

        # Match ndim first
        curr_t = t
        while curr_t.ndim < len(shape):
            curr_t = curr_t.unsqueeze(0)

        if mode == "tile":
            # Calculate required repeats for each dimension
            repeats = []
            for s1, s2 in zip(curr_t.shape, shape):
                if s1 == 0:  # Handle zero-sized tensors
                    return curr_t
                # Ceiling division to ensure coverage
                repeat_times = (s2 + s1 - 1) // s1
                repeats.append(repeat_times)

            # Repeat and truncate
            curr_t = curr_t.repeat(repeats)
            slices = tuple(slice(0, s2) for s2 in shape)
            return curr_t[slices].contiguous()

        # Fallback to padding if not tile mode
        out = torch.zeros(shape, dtype=curr_t.dtype, device=curr_t.device)
        slices = tuple(slice(0, d) for d in curr_t.shape)
        out[slices] = curr_t
        return out.contiguous()

    result = []
    for t in tensors:
        if torch.is_tensor(t):
            result.append(normalize_one(t, target_shape))
        else:
            result.append(t.contiguous())
    return tuple(result)
