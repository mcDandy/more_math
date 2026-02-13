#!/usr/bin/env python3
"""Quick test to verify bitwise operations work with tensors"""
import sys
sys.path.insert(0, r'D:\stability\Data\Packages\ComfyUI')

import torch
from custom_nodes.more_math.more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor

def test_bitwise_xor_float():
    """Test XOR with float tensors (the reported bug)"""
    print("Testing bitwise XOR with float tensors...")
    
    # Create float tensors (this was causing the error)
    a = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
    b = torch.tensor([4.0, 5.0, 6.0], dtype=torch.float32)
    
    visitor = UnifiedMathVisitor({"a": a, "b": b})
    
    try:
        # This should convert to int64, perform XOR, then convert back
        result = visitor._bitwise_op(a, b, torch.bitwise_xor, lambda x, y: x ^ y)
        print(f"✓ XOR succeeded!")
        print(f"  Input a (float32): {a}")
        print(f"  Input b (float32): {b}")
        print(f"  Result: {result}")
        print(f"  Result dtype: {result.dtype}")
        return True
    except Exception as e:
        print(f"✗ XOR failed: {e}")
        return False

def test_bitwise_and_float():
    """Test AND with float tensors"""
    print("\nTesting bitwise AND with float tensors...")
    
    a = torch.tensor([15.0, 14.0, 13.0], dtype=torch.float32)
    b = torch.tensor([7.0, 3.0, 1.0], dtype=torch.float32)
    
    visitor = UnifiedMathVisitor({"a": a, "b": b})
    
    try:
        result = visitor._bitwise_op(a, b, torch.bitwise_and, lambda x, y: x & y)
        print(f"✓ AND succeeded!")
        print(f"  Input a (float32): {a}")
        print(f"  Input b (float32): {b}")
        print(f"  Result: {result}")
        print(f"  Result dtype: {result.dtype}")
        return True
    except Exception as e:
        print(f"✗ AND failed: {e}")
        return False

def test_bitwise_or_float():
    """Test OR with float tensors"""
    print("\nTesting bitwise OR with float tensors...")
    
    a = torch.tensor([15.0, 14.0, 13.0], dtype=torch.float32)
    b = torch.tensor([7.0, 3.0, 1.0], dtype=torch.float32)
    
    visitor = UnifiedMathVisitor({"a": a, "b": b})
    
    try:
        result = visitor._bitwise_op(a, b, torch.bitwise_or, lambda x, y: x | y)
        print(f"✓ OR succeeded!")
        print(f"  Input a (float32): {a}")
        print(f"  Input b (float32): {b}")
        print(f"  Result: {result}")
        print(f"  Result dtype: {result.dtype}")
        return True
    except Exception as e:
        print(f"✗ OR failed: {e}")
        return False

def test_bitwise_not_float():
    """Test NOT with float tensors"""
    print("\nTesting bitwise NOT with float tensors...")
    
    a = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
    
    visitor = UnifiedMathVisitor({"a": a})
    
    try:
        result = visitor._bitwise_not(a)
        print(f"✓ NOT succeeded!")
        print(f"  Input a (float32): {a}")
        print(f"  Result: {result}")
        print(f"  Result dtype: {result.dtype}")
        return True
    except Exception as e:
        print(f"✗ NOT failed: {e}")
        return False

def test_int_tensors_preserved():
    """Ensure int tensors still work as before"""
    print("\nTesting that int tensor dtypes are preserved...")
    
    a = torch.tensor([15, 14, 13], dtype=torch.int16)
    b = torch.tensor([7, 3, 1], dtype=torch.int16)
    
    visitor = UnifiedMathVisitor({"a": a, "b": b})
    
    try:
        result = visitor._bitwise_op(a, b, torch.bitwise_and, lambda x, y: x & y)
        assert result.dtype == torch.int16, f"Expected int16, got {result.dtype}"
        print(f"✓ Int16 dtype preserved!")
        print(f"  Input a (int16): {a}")
        print(f"  Input b (int16): {b}")
        print(f"  Result (int16): {result}")
        return True
    except Exception as e:
        print(f"✗ Int16 test failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 70)
    print("Bitwise Operations Fix Verification")
    print("=" * 70)
    
    results = [
        test_bitwise_xor_float(),
        test_bitwise_and_float(),
        test_bitwise_or_float(),
        test_bitwise_not_float(),
        test_int_tensors_preserved(),
    ]
    
    print("\n" + "=" * 70)
    if all(results):
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed")
        sys.exit(1)
    print("=" * 70)
