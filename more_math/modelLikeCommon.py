from .helper_functions import generate_dim_variables, parse_expr, as_tensor, get_v_variable, get_f_variable, get_tensor_device, move_to_device
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
import comfy
import comfy.model_management
import torch


def _get_model_patcher(obj):
    patcher = getattr(obj, "patcher", None)
    if patcher is None and hasattr(obj, "model"):
        patcher = getattr(obj.model, "patcher", None)
    return patcher


def get_effective_state_dict(obj):
    if hasattr(obj, "patcher") and hasattr(obj.patcher, "model_state_dict"):
        return obj.patcher.model_state_dict()
    if hasattr(obj, "model_state_dict"):
        return obj.model_state_dict()
    if hasattr(obj, "model") and hasattr(obj.model, "patcher") and hasattr(obj.model.patcher, "model_state_dict"):
        return obj.model.patcher.model_state_dict()
    if hasattr(obj, "model") and hasattr(obj.model, "model_state_dict"):
        return obj.model.model_state_dict()
    if hasattr(obj, "model") and hasattr(obj.model, "state_dict"):
        return obj.model.state_dict()
    if hasattr(obj, "state_dict"):
        return obj.state_dict()
    return None


def get_effective_weight(obj, key):
    patcher = _get_model_patcher(obj)
    if patcher is not None and hasattr(patcher, "patch_weight_to_device"):
        try:
            return patcher.patch_weight_to_device(key, return_weight=True)
        except Exception:
            pass

    if hasattr(obj, "patch_weight_to_device"):
        try:
            return obj.patch_weight_to_device(key, return_weight=True)
        except Exception:
            pass

    sd = get_effective_state_dict(obj)
    if sd is not None:
        return sd.get(key, None)
    return None


def get_base_weight(obj, key):
    patcher = _get_model_patcher(obj)
    if patcher is not None and hasattr(patcher, "use_ejected") and hasattr(patcher, "model"):
        try:
            with patcher.use_ejected():
                weight, _, _ = comfy.model_patcher.get_key_weight(patcher.model, key)
                return weight
        except Exception:
            pass

    sd = get_effective_state_dict(obj)
    if sd is not None:
        return sd.get(key, None)
    return None


def get_base_state_dict(obj):
    patcher = _get_model_patcher(obj)
    if patcher is not None and hasattr(patcher, "use_ejected") and hasattr(patcher, "model"):
        try:
            with patcher.use_ejected():
                return get_effective_state_dict(obj)
        except Exception:
            pass
    return get_effective_state_dict(obj)


def coerce_like(weight, reference, device=None):
    if isinstance(weight, torch.Tensor) and isinstance(reference, torch.Tensor):
        target_device = device if device is not None else reference.device
        if weight.device != target_device or weight.dtype != reference.dtype:
            return weight.to(device=target_device, dtype=reference.dtype)
    return weight


def calculate_patches(Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0, use_compute_device=False):
    """Legacy calculate_patches for backward compatibility."""
    return calculate_patches_autogrow(Model, V={"V0": a, "V1": b, "V2": c, "V3": d}, F={"F0": w, "F1": x, "F2": y, "F3": z}, pbar=None, mapping={"a": "V0", "b": "V1", "c": "V2", "d": "V3", "w": "F0", "x": "F1", "y": "F2", "z": "F3"}, use_compute_device=use_compute_device)

def calculate_patches_autogrow(Expr, V, F, pbar=None, mapping=None, stack=[], use_compute_device=False):
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
        sd = get_effective_state_dict(m)
        if sd is None:
            sd_keys = []
        else:
            sd_keys = sd.keys()

        for key in sd_keys:
            if key not in seen_keys:
                seen_keys.add(key)
                all_keys_list.append(key)

    # Function to get weight from a valid object
    def get_weight(obj, key):
        return get_effective_weight(obj, key)

    tree = None
    if isinstance(Expr,str):
        tree = parse_expr(Expr)
    else:
        tree = Expr
    patches = {}
    original_device = None
    compute_device = comfy.model_management.get_torch_device() if use_compute_device else None
    needs_deltas = isinstance(Expr, str) and "_d" in Expr or not isinstance(Expr, str)

    current_state_dicts = {}
    base_state_dicts = {}
    for v_name, v_val in V.items():
        if v_val is None:
            continue
        current_sd = get_effective_state_dict(v_val)
        if current_sd is None:
            continue
        if original_device is None:
            original_device = get_tensor_device(current_sd)
        if compute_device is not None and original_device is not None and compute_device != original_device:
            current_sd = move_to_device(current_sd, compute_device)
        current_state_dicts[v_name] = current_sd
        if needs_deltas:
            base_sd = get_base_state_dict(v_val)
            if base_sd is not None and compute_device is not None and original_device is not None and compute_device != original_device:
                base_sd = move_to_device(base_sd, compute_device)
            base_state_dicts[v_name] = base_sd

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
        deltas = {}

        for v_name in V.keys():
            current_sd = current_state_dicts.get(v_name)
            if current_sd is None:
                continue
            w_tensor = current_sd.get(key, None)
            if w_tensor is not None:
                variables[v_name] = w_tensor
                ref_tensor = w_tensor
                valid_key = True
                if needs_deltas:
                    base_sd = base_state_dicts.get(v_name)
                    base_tensor = base_sd.get(key, None) if base_sd is not None else None
                    if base_tensor is None:
                        base_tensor = w_tensor
                    base_tensor = coerce_like(base_tensor, w_tensor, device=compute_device)
                    try:
                        deltas[v_name] = w_tensor - base_tensor
                    except Exception:
                        deltas[v_name] = torch.zeros_like(w_tensor)
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
            if v_name not in deltas:
                deltas[v_name] = torch.zeros_like(variables[v_name])
            variables[f"{v_name}_d"] = deltas[v_name]

        # Populate aliases for V (a, b, c, d)
        for alias, target in mapping.items():
            if target in variables:
                variables[alias] = variables[target]
            elif target in V:
                # V key exists in input dict but this specific layer key is missing
                variables[alias] = torch.zeros_like(ref_tensor)
            else:
                # Target doesn't exist at all (e.g., V1 not provided)
                # Check if it's a V-key pattern and zero-fill
                if target.startswith("V") and target[1:].isdigit():
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
        variables |= {f"{v_name}_d": variables[v_name] - variables["V0"] for v_name in V.keys() if v_name in variables and "V0" in variables}

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

        if pbar is not None:
            pbar.update(1)

    if compute_device is not None and original_device is not None and original_device != compute_device:
        patches = {
            key: ((value[0].to(device=original_device),) if isinstance(value, tuple) and value and torch.is_tensor(value[0]) else value)
            for key, value in patches.items()
        }

    return patches
