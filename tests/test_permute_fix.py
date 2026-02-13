import torch
import sys
import os

# Add paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))) # ComfyUI root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "more_math", "Parser")))

import optical_flow_utils as ofu
from comfy.nested_tensor import NestedTensor

def test_permute_and_apply():
    print("\n--- Testing Permute and Flow Apply ---")
    
    # 1. Test Permute on NestedTensor
    print("Testing NestedTensor.permute...")
    nt = NestedTensor([torch.randn(1, 256, 256, 3) for _ in range(2)])
    try:
        # Reorder [B, H, W, C] to [B, C, H, W]
        nt_permuted = nt.permute(0, 3, 1, 2)
        print(f"Original shape: {nt.shape}")
        print(f"Permuted shape: {nt_permuted.shape}")
        if nt_permuted.shape == (1, 3, 256, 256):
            print("NestedTensor.permute SUCCESS!")
        else:
            print(f"NestedTensor.permute FAILED: Got {nt_permuted.shape}")
    except Exception as e:
        print(f"NestedTensor.permute FAILED with error: {e}")
        import traceback
        traceback.print_exc()

    # 2. Test apply_flow
    print("\nTesting ofu.apply_flow...")
    img = torch.randn(1, 128, 128, 3)
    flow = torch.zeros(1, 128, 128, 2) # Zero flow should be identity
    flow[..., 0] = 10.0 # Shift 10px right
    
    try:
        warped = ofu.apply_flow(img, flow)
        print(f"Warped shape: {warped.shape}")
        if warped.shape == img.shape:
            print("ofu.apply_flow SUCCESS!")
        else:
            print(f"ofu.apply_flow FAILED: Got {warped.shape}")
    except Exception as e:
        print(f"ofu.apply_flow FAILED with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_permute_and_apply()
