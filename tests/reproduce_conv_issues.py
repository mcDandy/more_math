import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

_comfy_root = os.path.abspath(os.path.join(_here, "../../.."))
if _comfy_root not in sys.path:
    sys.path.insert(0, _comfy_root)

import torch
import pytest
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor

from more_math.LatentMathNode import LatentMathNode


def test_conv_1d():
    """
    Test 1D convolution.
    Input: [Batch, Length, Channels] = [1, 10, 4]
    Kernel: 1D size 3
    """
    print("\n--- Testing 1D Conv ---")
    node = LatentMathNode()
    shape = (1, 10, 4)
    a_val = torch.randn(*shape)

    # conv(a, 3, 1.0) -> implies kernel of ones, size 3
    # Result should correspond to 1D conv
    try:
        # LatentMathNode expects latent dicts usually
        input_dict = {"samples": a_val}
        res = node.execute("conv(a, 3, 1.0)", a=input_dict)

        # LatentMathNode returns list of dicts
        res_tensor = res[0]["samples"]

        print(f"1D Conv Result Shape: {res_tensor.shape}")
        # Expect (1, 10, 4)
        assert res_tensor.shape == shape
    except Exception as e:
        print(f"1D Conv Failed: {e}")
        raise


def test_conv_3d():
    """
    Test 3D convolution.
    Input: [Batch, Depth, Height, Width, Channels] = [1, 5, 32, 32, 4]
    Kernel: 3D size 3x3x3
    """
    print("\n--- Testing 3D Conv ---")
    node = LatentMathNode()
    shape = (1, 5, 32, 32, 4)
    a_val = torch.randn(*shape)

    try:
        input_dict = {"samples": a_val}
        res = node.execute("conv(a, 3, 3, 3, 1.0)", a=input_dict)
        res_tensor = res[0]["samples"]
        print(f"3D Conv Result Shape: {res_tensor.shape}")
        assert res_tensor.shape == shape
    except Exception as e:
        print(f"3D Conv Failed: {e}")
        raise


def test_conv_arbitrary_batch():
    """
    Test generic tensor with extra batch dims.
    Input: [B1, B2, H, W, C] = [2, 2, 16, 16, 4] -> Should be treated as Batch=4
    """
    print("\n--- Testing Arbitrary Batch ---")
    node = LatentMathNode()
    shape = (2, 2, 16, 16, 4)
    a_val = torch.randn(*shape)

    try:
        # conv(a, 3, 3, 1.0) -> 2D conv on (16,16)
        input_dict = {"samples": a_val}
        res = node.execute("conv(a, 3, 3, 1.0)", a=input_dict)
        res_tensor = res[0]["samples"]
        print(f"Arbitrary Batch Result Shape: {res_tensor.shape}")
        assert res_tensor.shape == shape
    except Exception as e:
        print(f"Arbitrary Batch Failed: {e}")
        raise


def test_conv_list_kernel():
    """
    Test conv with list kernel (Regression test for float64 mismatch).
    Kernel: 3x3x3 list of floats.
    """
    print("\n--- Testing List Kernel Conv ---")
    node = LatentMathNode()
    shape = (1, 5, 10, 10, 4)  # [B, D, H, W, C]
    a_val = torch.randn(*shape).float()

    # 3x3x3 kernel = 27 elements
    # Using the user's example kernel
    kernel_list = [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
    kernel_str = str(kernel_list)
    expr = f"conv(a, 3, 3, 3, {kernel_str})/8"

    try:
        input_dict = {"samples": a_val}
        res = node.execute(expr, a=input_dict)
        res_tensor = res[0]["samples"]
        print(f"List Kernel Result Shape: {res_tensor.shape}")
        assert res_tensor.shape == shape
        assert res_tensor.dtype == torch.float32
    except Exception as e:
        print(f"List Kernel Failed: {e}")
        raise


def test_conv_audio():
    """
    Test 1D conv on Audio [B, C, L].
    Input: [1, 2, 100]. Kernel: 3.
    Should be treated as Channels First -> [B, L, C].
    Output should preserve Channels First [B, 2, 100].
    """
    print("\n--- Testing Audio Conv [B, C, L] ---")
    node = LatentMathNode()
    shape = (1, 2, 100)  # [B, C, L] (L >> C)
    a_val = torch.randn(*shape).float()

    # conv(a, 3, 1.0) on last dim (L)
    # Expected: result shape same as input
    try:
        input_dict = {"samples": a_val}
        res = node.execute("conv(a, 3, 1.0)", a=input_dict)
        res_tensor = res[0]["samples"]
        print(f"Audio Result Shape: {res_tensor.shape}")

        if res_tensor.shape != shape:
            print(f"Likely interpreted as Channels Last [B, L, C] where C is small? No.")
            # If interpreted as Channels last [..., C].
            # [1, 2, 100]. Spatial=[2]. Channel=100.
            # Output [1, 2, 100] (but confusing channels).
            pass

        assert res_tensor.shape == shape
    except Exception as e:
        print(f"Audio Conv Failed: {e}")
        raise


def test_conv_deep_latent():
    """
    Test 3D conv on Deep Latent [B, 32, H, W] (User request).
    Input: [1, 32, 16, 16]. Kernel: 3x3x3.
    Should be treated as Channels First -> [B, 32, 16, 16, 1].
    Depth=32. H=16. W=16.
    """
    print("\n--- Testing Deep Latent Conv [B, 32, H, W] ---")
    node = LatentMathNode()
    shape = (1, 32, 16, 16)
    a_val = torch.randn(*shape).float()

    # conv(a, 3, 3, 3, 1.0)
    # 3D kernels need D,H,W.
    # D=32 (Channel). H=16. W=16.
    try:
        input_dict = {"samples": a_val}
        res = node.execute("conv(a, 3, 3, 3, 1.0)", a=input_dict)
        res_tensor = res[0]["samples"]
        print(f"Deep Latent Result Shape: {res_tensor.shape}")
        assert res_tensor.shape == shape

        # Identity check (ensure D neighbors engaged)
        # Using simple kernel, center only vs ones.
        # But this test just checks shape and execution path.
    except Exception as e:
        print(f"Deep Latent Failed: {e}")
        raise


def test_conv_padding():
    """
    Test padding consistency, especially for even kernels.
    Input: [1, 10, 10, 1]. Kernel: 4x4.
    Should produce [1, 10, 10, 1] output (Same padding).
    """
    print("\n--- Testing Padding (Even Kernel Size 4) ---")
    node = LatentMathNode()
    shape = (1, 10, 10, 1)
    a_val = torch.randn(*shape).float()

    # conv(a, 4, 4, 1.0)
    # If padding is symmetric 2, result is 11x11.
    # If padding is symmetric 1, result is 9x9.
    # We need asymmetric pad (1, 2) to get 10x10.
    try:
        input_dict = {"samples": a_val}
        res = node.execute("conv(a, 4, 4, 1.0)", a=input_dict)
        res_tensor = res[0]["samples"]
        print(f"Padding Test Result Shape: {res_tensor.shape}")
        assert res_tensor.shape == shape
    except Exception as e:
        print(f"Padding Test Failed: {e}")
        raise


def test_conv_complex_padding():
    """
    Test asymmetric padding with mixed odd/even kernel sizes.
    Kernel: (3, 4). Input: (1, 10, 10, 1).
    Should produce (1, 10, 10, 1).
    """
    print("\n--- Testing Complex Padding (3, 4) ---")
    node = LatentMathNode()
    shape = (1, 10, 10, 1)
    a_val = torch.randn(*shape).float()

    try:
        input_dict = {"samples": a_val}
        res = node.execute("conv(a, 3, 4, 1.0)", a=input_dict)
        res_tensor = res[0]["samples"]
        print(f"Complex Padding Result Shape: {res_tensor.shape}")
        assert res_tensor.shape == shape
    except Exception as e:
        print(f"Complex Padding Failed: {e}")
        raise


def test_conv_3d_asymmetric():
    """
    Test 3D conv with asymmetric spatial dims.
    Input: [1, 5, 10, 20, 1]. Kernel: 3x3x3.
    """
    print("\n--- Testing 3D Asymmetric Input ---")
    node = LatentMathNode()
    shape = (1, 5, 10, 20, 1)
    a_val = torch.randn(*shape).float()

    try:
        input_dict = {"samples": a_val}
        res = node.execute("conv(a, 3, 3, 3, 1.0)", a=input_dict)
        res_tensor = res[0]["samples"]
        print(f"3D Asymmetric Result Shape: {res_tensor.shape}")
        assert res_tensor.shape == shape
    except Exception as e:
        print(f"3D Asymmetric Failed: {e}")
        raise


if __name__ == "__main__":
    try:
        test_conv_1d()
        test_conv_3d()
        test_conv_arbitrary_batch()
        test_conv_list_kernel()
        test_conv_audio()
        test_conv_deep_latent()
        test_conv_padding()
        test_conv_complex_padding()
        test_conv_3d_asymmetric()
        print("All Conv tests passed!")
    except Exception as e:
        import traceback

        traceback.print_exc()
        sys.exit(1)
