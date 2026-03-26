import traceback

try:
    from .more_math.nodes import comfy_entrypoint as comfy_entrypoint
except ImportError:
    print("Something is seriously wrong")
    traceback.print_exc()

WEB_DIRECTORY = "./web"
__all__ = ["comfy_entrypoint", "WEB_DIRECTORY"]