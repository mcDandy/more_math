try:
    from .more_math.nodes import comfy_entrypoint as comfy_entrypoint
except ImportError:
    # During testing, comfy_api may not be available
    # This is fine - tests import modules directly
    print("Something is seriously wrong")