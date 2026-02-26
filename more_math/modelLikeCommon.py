from .helper_functions import generate_dim_variables, parse_expr, as_tensor, get_v_variable, get_f_variable
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
import torch


def calculate_patches(Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
    """Legacy calculate_patches for backward compatibility."""
    return calculate_patches_autogrow(Model, V={"V0": a, "V1": b, "V2": c, "V3": d}, F={"F0": w, "F1": x, "F2": y, "F3": z}, mapping={"a": "V0", "b": "V1", "c": "V2", "d": "V3", "w": "F0", "x": "F1", "y": "F2", "z": "F3"})

def calculate_patches_autogrow(Expr, V, F,pbar, mapping=None,stack = []):
    """
    Calculate patches for model-like objects (Model, VAE, CLIP) using Autogrow inputs.
    Iterates over the UNION of keys from all input models to support merging disjoint architectures/patches.

    Args:
        Expr: The math expression string or parse tree.
        V: Dictionary of input models (Autogrow Input).
        F: Dictionary of input floats (Autogrow Float).
        mapping: Optional dict mapping legacy alias names to V keys (e.g. {"a": "V0"}).
    """
    if V is None: V = {}
    if F is None: F = {}
    if mapping is None: mapping = {}

    # Collect all unique keys from all models, preserving order from first model
    all_keys_list = []  # Preserves order
    seen_keys = set()   # Fast O(1) duplicate checking

    models = [v for v in V.values() if v is not None]
    if not models:
        return {}

    for m in models:
        if hasattr(m, "model") and hasattr(m.model, "state_dict"):
            sd_keys = m.model.state_dict().keys()
        elif hasattr(m, "state_dict"): # VAE might have state_dict directly?
            sd_keys = m.state_dict().keys()
        else:
            sd_keys = []

        for key in sd_keys:
            if key not in seen_keys:
                seen_keys.add(key)
                all_keys_list.append(key)

    # Function to get weight from a valid object
    def get_weight(obj, key):
        if hasattr(obj, "model") and hasattr(obj.model, "state_dict"):
             sd = obj.model.state_dict()
             return sd.get(key, None)
        if hasattr(obj, "state_dict"):
             sd = obj.state_dict()
             return sd.get(key, None)
        return None

    tree = None
    if isinstance(Expr,str):
        tree = parse_expr(Expr)
    else:
        tree = Expr
    patches = {}

    # Progress bar if possible (comfy.utils.ProgressBar might assume unthreaded?)
    # Just skip for utility or use if substantial.
    layer_count = len(all_keys_list)
    for layer_idx, key in enumerate(all_keys_list):

        variables = {}
        # Populate F variables (constants for all keys)
        for k, val in F.items():
            variables[k] = val if val is not None else 0.0

        # Also populate mapped aliases for F (w, x, y, z)
        for alias, target in mapping.items():
            if target in F:
                variables[alias] = F[target] if F[target] is not None else 0.0

        variables["L"] = float(layer_idx)
        variables["layer"] = float(layer_idx)
        variables["LC"] = float(layer_count)
        variables["layer_count"] = float(layer_count)
        variables["K"] = key
        variables["key"] = key

        # Inject weights for this key from V models
        valid_key = False
        ref_tensor = None

        for v_name, v_val in V.items():
            if v_val is not None:
                w_tensor = get_weight(v_val, key)
                if w_tensor is not None:
                    variables[v_name] = w_tensor
                    ref_tensor = w_tensor
                    valid_key = True
                else:
                    # Missing key in this model will be handled later (zero init)
                    pass

        if not valid_key:
            continue

        # Find reference shape
        if ref_tensor is None:
            continue # Should not happen if valid_key is true

        # Fill missing models with zeros
        for v_name in V.keys():
            if v_name not in variables:
                variables[v_name] = torch.zeros_like(ref_tensor)

        # Populate aliases for V (a, b, c, d)
        for alias, target in mapping.items():
            if target in variables:
                variables[alias] = variables[target]
            elif target in V: # V exists but key missing
                 variables[alias] = torch.zeros_like(ref_tensor)

        v_stacked, v_cnt = get_v_variable(variables)
        if v_stacked is not None:
             variables["V"] = v_stacked
             variables["Vcnt"] = float(v_cnt)
             variables["V_count"] = float(v_cnt)

        f_stacked, f_cnt = get_f_variable(F)
        if f_stacked is not None:
             variables["F"] = f_stacked
             variables["Fcnt"] = float(f_cnt)
             variables["F_count"] = float(f_cnt)

        variables = variables | generate_dim_variables(ref_tensor)

        # Execute math

        visitor = UnifiedMathVisitor(variables, ref_tensor.shape,state_storage=stack)
        res = visitor.visit(tree)
        res = as_tensor(res, ref_tensor.shape)

        original = variables.get("V0")
        if original is None:
            original = torch.zeros_like(res)

        diff = res - original

        # Clean up: don't store zero patches
        if not torch.all(diff == 0):
            patches[key] = (diff,)

        pbar.update(1)

    return patches
