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

import pytest

@pytest.fixture(scope="session", autouse=True)
def session_setup():
    """
    Session-scoped autouse fixture kept for future per-session initialization.
    Top-level sys.path modification already runs during collection, so this fixture
    ensures any further session setup can be added without changing tests.
    """
    yield

