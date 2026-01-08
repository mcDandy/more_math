import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
_comfy_root = os.path.abspath(os.path.join(_project_root, os.pardir, os.pardir))

# Add project root and ComfyUI root to sys.path
# This ensures import comfy_api and import comfy work.
for p in [_project_root, _comfy_root]:
    if p not in sys.path:
        sys.path.insert(0, p)
        # also make it visible to subprocesses that inspect PYTHONPATH
        os.environ["PYTHONPATH"] = p + os.pathsep + os.environ.get("PYTHONPATH", "")

# Special case: 'more_math' root folder has an __init__.py which conflicts with the 'more_math' subfolder.
# We want 'import more_math' to resolve to the subfolder package.
_subfolder = os.path.join(_project_root, "more_math")
_sub_init = os.path.join(_subfolder, "__init__.py")

# Check if we are accidentally importing the root folder as the package
def _is_root_package():
    if "more_math" not in sys.modules:
        return False
    m = sys.modules["more_math"]
    m_file = getattr(m, "__file__", "") or ""
    # If the module file is NOT in the subfolder, it's likely the root folder's __init__.py
    return os.path.abspath(m_file) != os.path.abspath(_sub_init)

if _is_root_package() or "more_math" not in sys.modules:
    import importlib.util
    _spec = importlib.util.spec_from_file_location("more_math", _sub_init)
    if _spec:
        _m = importlib.util.module_from_spec(_spec)
        sys.modules["more_math"] = _m
        _spec.loader.exec_module(_m)

# Redirect comfy_api.Model to comfy_api.latest.io.Model if needed
# as requested by user to support the 'latest' API position.
try:
    import comfy_api
    import comfy_api.latest as latest
    if not hasattr(comfy_api, "Model") and hasattr(latest, "io") and hasattr(latest.io, "Model"):
        comfy_api.Model = latest.io.Model
        comfy_api.io = latest.io
except (ImportError, AttributeError):
    pass

import pytest


@pytest.fixture(scope="session", autouse=True)
def session_setup():
    """
    Session-scoped autouse fixture kept for future per-session initialization.
    Top-level sys.path modification already runs during collection, so this fixture
    ensures any further session setup can be added without changing tests.
    """
    yield
