import torch
import comfy.utils

from .helper_functions import getIndexTensorAlongDim, parse_expr, eval_tensor_expr_with_tree, as_tensor


def calculate_patches(Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
    """Calculate model weight patches by applying math expression to state dicts."""
    # Parse expression once
    tree = parse_expr(Model)

    sd_a = a.model.state_dict()
    sd_b = b.model.state_dict() if b is not None else {}
    sd_c = c.model.state_dict() if c is not None else {}
    sd_d = d.model.state_dict() if d is not None else {}

    patches = {}
    layer_count = len(sd_a)
    pbar = comfy.utils.ProgressBar(layer_count)

    for i, (key, tens_a) in enumerate(sd_a.items()):
        # Get tensors from other models, default to zeros
        tens_b = sd_b.get(key)
        tens_b = tens_b.to(tens_a.device) if tens_b is not None else torch.zeros_like(tens_a)

        tens_c = sd_c.get(key)
        tens_c = tens_c.to(tens_a.device) if tens_c is not None else torch.zeros_like(tens_a)

        tens_d = sd_d.get(key)
        tens_d = tens_d.to(tens_a.device) if tens_d is not None else torch.zeros_like(tens_a)

        # Build variables
        variables = {
            "a": tens_a,
            "b": tens_b,
            "c": tens_c,
            "d": tens_d,
            "w": w,
            "x": x,
            "y": y,
            "z": z,
            "L": i,
            "layer": i,
            "LC": layer_count,
            "layer_count": layer_count,
        }

        # Add dimension index tensors
        for dim_idx in range(tens_a.ndim):
            idx_tensor = getIndexTensorAlongDim(tens_a, dim_idx)
            variables[f"D{dim_idx}"] = idx_tensor
            variables[f"dim_{dim_idx}"] = idx_tensor

        result_tensor = as_tensor(eval_tensor_expr_with_tree(tree, variables, tens_a.shape), tens_a.shape)

        # Calculate patch (diff from original)
        diff = result_tensor - tens_a

        # Skip zero patches to save memory
        if not torch.all(diff == 0):
            patches[key] = (diff,)

        pbar.update(1)

    return patches
