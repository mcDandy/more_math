from .helper_functions import generate_dim_variables, parse_expr, as_tensor, get_v_variable, get_f_variable, get_tensor_device, move_to_device, LazyVariableDict, checkLazyNew
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
import comfy.model_management
import torch


def calculate_lora_dict_autogrow(Expr, V, F, pbar=None, mapping=None, stack=[], use_compute_device=False):
    """
    Calculate a new LORA_MODEL dict[str, Tensor] from math expressions applied
    over the UNION of keys from all input LoRA dicts, using Autogrow inputs.

    Unlike calculate_patches_autogrow (Model/VAE/CLIP), there is no
    ModelPatcher/backup involved here - a LORA_MODEL is just raw tensors
    (lora_up.weight, lora_down.weight, alpha, diff, ...). So V{n} is simply
    that tensor as-is (zero-filled when a given key is missing from that
    input), and there is no V{n}_d - these tensors already *are* deltas.
    """
    if V is None: V = {}
    if F is None: F = {}
    if mapping is None: mapping = {}

    needed_vars = checkLazyNew(Expr, V, F)
    needed_v_names = [v_name for v_name in V.keys() if v_name in needed_vars]
    if not needed_v_names:
        needed_v_names = [v_name for v_name in V.keys() if V.get(v_name) is not None]

    if not any(V.get(v_name) is not None for v_name in needed_v_names):
        return {}

    # Collect all unique keys from all inputs, preserving order from first input
    all_keys_list = []
    seen_keys = set()
    for d in V.values():
        if d is None:
            continue
        for key in d.keys():
            if key not in seen_keys:
                seen_keys.add(key)
                all_keys_list.append(key)

    tree = parse_expr(Expr) if isinstance(Expr, str) else Expr

    original_device = None
    compute_device = comfy.model_management.get_torch_device() if use_compute_device else None

    const_f_vars = {k: val if val is not None else 0.0 for k, val in F.items()}
    const_f_alias_vars = {
        alias: (F[target] if F[target] is not None else 0.0)
        for alias, target in mapping.items()
        if target in F
    }
    mapping_items = tuple(mapping.items())

    input_dicts = {}
    for v_name in needed_v_names:
        d = V.get(v_name)
        if d is None:
            continue
        if original_device is None:
            original_device = get_tensor_device(d)
        if compute_device is not None and original_device is not None and compute_device != original_device:
            d = move_to_device(d, compute_device)
        input_dicts[v_name] = d

    layer_count = len(all_keys_list)

    def make_lazy(value_fn):
        def lazy_eval():
            return value_fn()
        lazy_eval.is_lazy_var = True
        return lazy_eval

    result = {}

    for layer_idx, key in enumerate(all_keys_list):
        variables = LazyVariableDict(const_f_vars)
        variables.update(const_f_alias_vars)

        variables["L"] = float(layer_idx)
        variables["layer"] = float(layer_idx)
        variables["LC"] = float(layer_count)
        variables["layer_count"] = float(layer_count)
        variables["K"] = key
        variables["key"] = key

        ref_tensor = None
        present = {}
        for v_name in V.keys():
            d = input_dicts.get(v_name)
            if d is None:
                continue
            t = d.get(key, None)
            if t is not None:
                present[v_name] = t
                if ref_tensor is None:
                    ref_tensor = t

        if ref_tensor is None:
            continue

        for v_name in V.keys():
            if v_name in present:
                t = present[v_name]
                variables[v_name] = make_lazy(lambda t=t: t)
            else:
                variables[v_name] = make_lazy(lambda rt=ref_tensor: torch.zeros_like(rt))

        # Populate aliases for V (a, b, c, d)
        for alias, target in mapping_items:
            if target in variables:
                variables[alias] = variables[target]
            elif target.startswith("V") and target[1:].isdigit():
                variables[alias] = make_lazy(lambda rt=ref_tensor: torch.zeros_like(rt))

        v_cache = [None]

        def lazy_v_stack():
            if v_cache[0] is None:
                v_cache[0] = get_v_variable(variables)
            return v_cache[0][0]

        lazy_v_stack.is_lazy_var = True

        def lazy_v_count():
            if v_cache[0] is None:
                v_cache[0] = get_v_variable(variables)
            return float(v_cache[0][1])

        lazy_v_count.is_lazy_var = True

        variables["V"] = lazy_v_stack
        variables["Vcnt"] = lazy_v_count
        variables["V_count"] = lazy_v_count

        f_stacked, f_cnt = get_f_variable(F)
        if f_stacked is not None:
            variables["F"] = f_stacked
            variables["Fcnt"] = float(f_cnt)
            variables["F_count"] = float(f_cnt)

        variables = variables | generate_dim_variables(ref_tensor)

        visitor = UnifiedMathVisitor(variables, ref_tensor.shape, state_storage=stack)
        res = visitor.visit(tree)
        res = as_tensor(res, ref_tensor.shape)

        if compute_device is not None and original_device is not None and original_device != compute_device:
            res = res.to(device=original_device)

        result[key] = res

        if pbar is not None:
            pbar.update(1)

    return result
