from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream, CommonTokenStream

import torch

from .Parser.MathExprLexer import MathExprLexer
from .Parser.MathExprParser import MathExprParser

import re

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
        return torch.broadcast_to(torch.Tensor(value).to(dtype=torch.float32), shape).contiguous()
    return torch.cat(value)


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
        variables[f"S{dim}"] = float(size)  # Scalar size, not tensor
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

def get_v_variable(v_norm_dict, length_mismatch="error"):
    """
    Collects V0, V1, ... from the dict, stacks them into a V tensor,
    and returns (V_stacked, V_count).
    """
    sorted_keys = sorted([k for k in v_norm_dict.keys() if k.startswith("V")], key=lambda x: int(x[1:]))
    listt = list()
    for i in range(0,len(sorted_keys)):
        listt.append(v_norm_dict[sorted_keys[i]])
    return listt,len(listt)

def get_f_variable(f_dict):
    """
    Collects F0, F1, ... from the dict, stacks them into an F 1D tensor,
    and returns (F_stacked, F_count).
    """
    sorted_keys = sorted([k for k in f_dict.keys() if k.startswith("F")], key=lambda x: int(x[1:]))
    ordered_values = []

    for k in sorted_keys:
        val = f_dict[k]
        if torch.is_tensor(val):
            # If it's a tensor, just get the first element if it's a scalar or keep as is if it's already 1D?
            # Usually F inputs are floats. If they are tensors, we'll try to treat them as values.
            ordered_values.append(val.flatten()[0] if val.numel() > 0 else torch.tensor(0.0))
        elif isinstance(val, (int, float)):
             ordered_values.append(torch.tensor(float(val)))
        else:
             ordered_values.append(torch.tensor(0.0))

    if not ordered_values:
         return None, 0

    try:
        stacked = torch.stack(ordered_values)
        return stacked, len(ordered_values)
    except Exception:
        return None, len(ordered_values)

def _collect_reads_only(cls, node, needed_vars, assigned_vars, shadowed_vars):
    if node is None:
        return

    node_type = type(node).__name__

    if node_type == 'VariableExpContext':
        var_name = node.VARIABLE().getText()
        if var_name in shadowed_vars:
            return
        if var_name not in assigned_vars:
            needed_vars.add(var_name)
        return

    if node_type == 'FunctionDefContext':
        return

    if node_type == 'VarDefContext':
        for expr in node.expr():
            cls._collect_reads_only(expr, needed_vars, assigned_vars, shadowed_vars)
        return

    for i in range(node.getChildCount()):
        cls._collect_reads_only(node.getChild(i), needed_vars, assigned_vars, shadowed_vars)

def _collect_vars_from_node(cls, node, needed_vars, assigned_vars, shadowed_vars):
    """Recursively collect variable reads from an AST node"""
    if node is None:
        return

    node_type = type(node).__name__

    # Found a variable read
    if node_type == 'VariableExpContext':
        var_name = node.VARIABLE().getText()
        # Skip if shadowed
        if var_name in shadowed_vars:
            return
        if var_name not in assigned_vars:
            needed_vars.add(var_name)
        return

    # Skip
    if node_type == 'FunctionDefContext':
        return

    # Recursively visit children
    for i in range(node.getChildCount()):
        cls._collect_vars_from_node(node.getChild(i), needed_vars, assigned_vars, shadowed_vars)

def checkLazyNew(Expression, V, F):
    tree = None
    parser = None
    if isinstance(Expression,str):
        tree = parse_expr(Expression)
        parser = tree.parser
    else:
        tree = Expression
        parser = tree.parser
    
    # Support aliases
    aliases = {"a": "V0", "b": "V1", "c": "V2", "d": "V3",
               "w": "F0", "x": "F1", "y": "F2", "z": "F3"}
    
    assigned_vars = set()
    needed_vars = set()
    
    # Process all top-level statements
    for child in tree.children:
        if not hasattr(child, 'getRuleIndex'):
            continue
    
        rule_name = parser.ruleNames[child.getRuleIndex()] if child.getRuleIndex() < len(parser.ruleNames) else None
    
        # Process function definitions: scan for reads but ignore writes
        if rule_name == 'funcDef':
            func_params = set()
            if child.paramList():
                for param in child.paramList().VARIABLE():
                    func_params.add(param.getText())
    
            _collect_reads_only(child, needed_vars, assigned_vars, func_params)
    
        # Top-level assignments
        elif rule_name == 'varDef':
            var_name = child.VARIABLE().getText()
            _collect_vars_from_node(child, needed_vars, assigned_vars, set())
            assigned_vars.add(var_name)
    
        # Track other top-level statements
        else:
            _collect_vars_from_node(child, needed_vars, assigned_vars, set())
    
    # Normalize variable names through aliases
    needed = set()
    for var in needed_vars:
        norm = aliases.get(var, var)
        if var == "V":
            needed.update(V.keys())
        if var == "F":
            needed.update(F.keys())
        if re.match(r"[VF][0-9]+", norm):
            needed.add(norm)
    
    return needed