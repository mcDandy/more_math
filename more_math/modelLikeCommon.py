from .helper_functions import parse_expr
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from .Parser.MathExprParser import MathExprParser
from antlr4 import InputStream, CommonTokenStream
from .Parser.MathExprLexer import MathExprLexer
import torch
import re

def calculate_patches(Expr, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0, V=None, F=None):
    """
    Calculate patches for model-like objects (Model, VAE, CLIP).
    Supports legacy a-d, w-z inputs and Autogrow V/F dictionaries.
    """
    if V is None: V = {}
    if F is None: F = {}

    # Map legacy inputs to V/F if provided
    # Note: caller is expected to handle V0=a mapping if using mixed mode, 
    # but strictly we should operate on one set.
    # We will prioritize V/F but populate from a-d if V is empty to support legacy calls if any.
    
    # Actually, simpler: Populate variables with legacy, then override/extend with V/F
    
    variables = {}
    
    # 1. Base variables (legacy)
    variables["a"] = a
    if b: variables["b"] = b
    if c: variables["c"] = c
    if d: variables["d"] = d
    
    variables["w"] = w
    variables["x"] = x
    variables["y"] = y
    variables["z"] = z
    
    # 2. Autogrow variables
    for k, v in V.items():
        if v is not None:
            variables[k] = v
    for k, v in F.items():
        if v is not None:
             variables[k] = v

    # 3. Aliases validation (ensure V0 exists if a is used etc? logic handled by visitor?)
    # The visitor just needs values.
    
    # We need to find all keys in the state dicts of all provided models
    models = [m for m in [a, b, c, d] if m is not None] + [v for v in V.values() if v is not None]
    if not models:
        return {}
    
    # Use first model as reference for keys
    ref_model = models[0]
    # For Model/CLIP/VAE wrappers, the keys are usually in the patcher or we iterate available keys?
    # standard ComfyUI model patching usually involves iterating keys in `model.get_key_patches(key)` or similar.
    # But here we are likely operating on the weights directly or creating a patch dict.
    
    # ComfyUI ModelPatcher logic:
    # We want to return a dict of {key: (weight, patch_func)} or just calculated weights?
    # ModelMathNode.execute acts as a merge.
    # calculate_patches typically iterates over all keys present in 'a' (or union of all).
    
    # Heuristic: collect all keys from all models
    # Objects might be ModelPatcher or the Model wrapper.
    # If it's a ComfyNode input of type MODEL, it's a ModelPatcher.
    
    # Let's inspect one model to see attributes.
    # Assuming standard Comfy `comfy.model_patcher.ModelPatcher`
    
    all_keys = set()
    for m in models:
        if hasattr(m, "model") and hasattr(m.model, "state_dict"):
             all_keys.update(m.model.state_dict().keys())
        elif hasattr(m, "state_dict"): # VAE might have state_dict directly?
             all_keys.update(m.state_dict().keys())
             
    # Function to get weight from a valid object
    def get_weight(obj, key):
        if hasattr(obj, "model") and hasattr(obj.model, "state_dict"):
             sd = obj.model.state_dict()
             return sd.get(key, None)
        if hasattr(obj, "state_dict"):
             sd = obj.state_dict()
             return sd.get(key, None)
        return None

    # Parse expression
    tree = parse_expr(Expr)
    
    patches = {}
    
    for key in all_keys:
        # Prepare variables for this key
        local_vars = variables.copy()
        
        # Inject weights for this key
        # We need to replace model objects in `local_vars` with their specific weight tensor for `key`
        # If a model doesn't have the key, treat as zero? Or skip?
        # Helper logic:
        # The variables dict currently holds Model objects.
        # We need to context-switch them to Tensors for the visitor.
        
        valid_key = False
        
        # Update local_vars with tensor values
        for var_name, var_val in variables.items():
            # Skip floats (w, x, y, z, F*)
            if isinstance(var_val, (float, int)):
                continue
            
            # Assume it's a model-like object
            w_tensor = get_weight(var_val, key)
            if w_tensor is not None:
                local_vars[var_name] = w_tensor
                valid_key = True # Found at least one model with this key
            else:
                # If model is missing key, what to do?
                # For now, maybe set to None? Visitor might handle or fail.
                # If we set to 0-tensor, we need shape. 
                # We can find shape from other models.
                pass
                
        if not valid_key:
            continue

        # Handle missing keys by initializing to zeros of matching shape
        # Find a reference tensor for shape
        ref_tensor = None
        for v in local_vars.values():
            if torch.is_tensor(v):
                ref_tensor = v
                break
                
        if ref_tensor is not None:
            for var_name in variables.keys():
                if var_name not in local_vars or local_vars[var_name] is None:
                     if not isinstance(variables[var_name], (float, int)): # it's a missing model weight
                        local_vars[var_name] = torch.zeros_like(ref_tensor)

        # Execute math
        try:
             visitor = UnifiedMathVisitor(local_vars, ref_tensor.shape if ref_tensor is not None else [1])
             res = visitor.visit(tree)
             if torch.is_tensor(res):
                 patches[key] = res
        except Exception as e:
            # print(f"Error calculating patch for key {key}: {e}")
            pass
            
    return patches
