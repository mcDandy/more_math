import os
import sys

# Ensure test discovery (Visual Studio / pytest) can import the package.
# conftest.py is imported during collection, so top-level path changes affect discovery.
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
_src_path = os.path.join(_project_root, "src")

if os.path.isdir(_src_path):
    _path_to_add = _src_path
else:
    _path_to_add = _project_root

if _path_to_add not in sys.path:
    sys.path.insert(0, _path_to_add)
    # also make it visible to subprocesses that inspect PYTHONPATH
    os.environ["PYTHONPATH"] = _path_to_add + os.pathsep + os.environ.get("PYTHONPATH", "")

import pytest

@pytest.fixture(scope="session", autouse=True)
def session_setup():
    """
    Session-scoped autouse fixture kept for future per-session initialization.
    Top-level sys.path modification already runs during collection, so this fixture
    ensures any further session setup can be added without changing tests.
    """
    yield

