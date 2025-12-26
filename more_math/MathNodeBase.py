from comfy_api.latest import io
from .helper_functions import comonLazy, make_zero_like

class MathNodeBase(io.ComfyNode):
    """
    Base class for More Math nodes providing common utilities.
    """

    @classmethod
    def check_lazy_status(cls, **kwargs):
        """
        Generic check_lazy_status implementation.
        Finds the first argument name that isn't a known variable (a-d, w-z) and assumes it's the expression.
        """
        # Known variable inputs (and internal ones we might ignore)
        known_vars = {'a', 'b', 'c', 'd', 'w', 'x', 'y', 'z', 'pooled_output'}
        
        # Heuristic: The expression is usually the first argument that is not a known variable.
        # But `comonLazy` takes (expr, a, b, c, d, w, x, y, z).
        # We need to extract the values from kwargs correctly.
        
        expr_key = None
        # Try finding the expression key
        for k in kwargs:
            if k not in known_vars and isinstance(kwargs[k], str):
                expr_key = k
                break
        
        # If we can't find it heuristically (e.g. standard naming), fallback or error?
        # Let's try to be safe. If we can't find it, we might be in a node with custom logic like ConditioningMathNode.
        # ConditioningMathNode has 'Tensor' and 'pooled_output' as expressions.
        
        if expr_key:
             expr = kwargs[expr_key]
             a = kwargs.get('a', None)
             b = kwargs.get('b', [])
             c = kwargs.get('c', [])
             d = kwargs.get('d', [])
             w = kwargs.get('w', 0)
             x = kwargs.get('x', 0)
             y = kwargs.get('y', 0)
             z = kwargs.get('z', 0)
             return comonLazy(expr, a, b, c, d, w, x, y, z)
             
        # Fallback/Empty return if we can't determine dependencies automatically
        return []

    @staticmethod
    def prepare_inputs(a, b, c, d):
        """
        Ensures optional inputs b, c, d are zero-initialized like a if None.
        Returns the prepared (a, b, c, d).
        """
        b = b if b is not None else make_zero_like(a)
        c = c if c is not None else make_zero_like(a)
        d = d if d is not None else make_zero_like(a)
        return a, b, c, d
