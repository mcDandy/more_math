import torch
import sys
import os

# Ensure we can import the module
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor

def test_large_quantile_fallback():
    print("Testing large quantile fallback in UnifiedMathVisitor...")
    # 36 million elements
    size = 36_000_000
    try:
        val = torch.rand(size)
        q = torch.tensor([0.0, 0.1, 0.5, 0.9, 1.0])

        visitor = UnifiedMathVisitor({})

        print(f"Calling _quartile_helper with size {size}...")
        # This should trigger the fallback
        res = visitor._quartile_helper(val, q)
        print(f"Success! Result: {res}")
    except Exception as e:
        print(f"Failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_large_quantile_fallback()
