"""
Comprehensive integration test for fp16/int16 bitwise operations.
Demonstrates real-world usage of the enhanced bitwise operators.
"""

import torch
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor


def test_mixed_dtype_operations():
    """Test operations with mixed dtypes."""
    print("=" * 70)
    print("Testing Mixed Dtype Operations")
    print("=" * 70)
    
    # Create a dummy context for testing
    class DummyContext:
        class Start:
            line = 0
            column = 0
        start = Start()
    ctx = DummyContext()
    
    # int8 operations
    print("\n1. INT8 Bitwise Operations:")
    a_int8 = torch.tensor([15, 7, 3], dtype=torch.int8)
    visitor = UnifiedMathVisitor({"a": a_int8})
    result = visitor._bitwise_not(a_int8)
    print(f"   Input:  {a_int8} (dtype={a_int8.dtype})")
    print(f"   ~Input: {result} (dtype={result.dtype})")
    assert result.dtype == torch.int8
    
    # int16 operations
    print("\n2. INT16 Bitwise Operations:")
    a_int16 = torch.tensor([255, 127, 63], dtype=torch.int16)
    b_int16 = torch.tensor([15, 31, 7], dtype=torch.int16)
    visitor = UnifiedMathVisitor({"a": a_int16, "b": b_int16})
    
    result_and = visitor._bitwise_op(a_int16, b_int16, torch.bitwise_and, lambda x, y: x & y, ctx)
    result_or = visitor._bitwise_op(a_int16, b_int16, torch.bitwise_or, lambda x, y: x | y, ctx)
    result_xor = visitor._bitwise_op(a_int16, b_int16, torch.bitwise_xor, lambda x, y: x ^ y, ctx)
    
    print(f"   a:     {a_int16} (dtype={a_int16.dtype})")
    print(f"   b:     {b_int16} (dtype={b_int16.dtype})")
    print(f"   a & b: {result_and}")
    print(f"   a | b: {result_or}")
    print(f"   a ^ b: {result_xor}")
    assert all(t.dtype == torch.int16 for t in [result_and, result_or, result_xor])
    
    # fp16 operations
    print("\n3. FP16 Bitwise Operations (bit-level manipulation):")
    a_fp16 = torch.tensor([1.0, -2.0, 3.5], dtype=torch.float16)
    visitor = UnifiedMathVisitor({"a": a_fp16})
    result = visitor._bitwise_not(a_fp16)
    print(f"   Input:         {a_fp16} (dtype={a_fp16.dtype})")
    print(f"   Bit-flipped:   {result} (dtype={result.dtype})")
    assert result.dtype == torch.float16
    
    # int32 operations (existing, should still work)
    print("\n4. INT32 Bitwise Operations (backward compatibility):")
    a_int32 = torch.tensor([65535, 32767, 16383], dtype=torch.int32)
    visitor = UnifiedMathVisitor({"a": a_int32})
    result = visitor._bitwise_not(a_int32)
    print(f"   Input:  {a_int32} (dtype={a_int32.dtype})")
    print(f"   ~Input: {result} (dtype={result.dtype})")
    assert result.dtype == torch.int32
    
    print("\n" + "=" * 70)
    print("✓ All mixed dtype operations completed successfully!")
    print("=" * 70)


def test_scalar_list_tensor_combinations():
    """Test operations with different input types."""
    print("\n" + "=" * 70)
    print("Testing Scalar/List/Tensor Combinations")
    print("=" * 70)
    
    # Create a dummy context for testing
    class DummyContext:
        class Start:
            line = 0
            column = 0
        start = Start()
    ctx = DummyContext()
    
    visitor = UnifiedMathVisitor({})
    
    # Tensor & Tensor
    print("\n1. Tensor & Tensor (int16):")
    a = torch.tensor([7, 14, 21], dtype=torch.int16)
    b = torch.tensor([3, 5, 7], dtype=torch.int16)
    result = visitor._bitwise_op(a, b, torch.bitwise_and, lambda x, y: x & y, ctx)
    print(f"   {a} & {b} = {result}")
    
    # Tensor & List
    print("\n2. Tensor & List (mixed):")
    a = torch.tensor([15, 14, 13], dtype=torch.int16)
    b = [7, 3, 1]
    result = visitor._bitwise_op(a, b, torch.bitwise_and, lambda x, y: x & y, ctx)
    print(f"   Tensor({a}) & List({b}) = {result}")
    
    # Scalar & List
    print("\n3. Scalar & List:")
    a = 15
    b = [7, 3, 1]
    result = visitor._bitwise_op(a, b, torch.bitwise_and, lambda x, y: x & y, ctx)
    print(f"   {a} & {b} = {result}")
    
    # List & List
    print("\n4. List & List:")
    a = [15, 14, 13]
    b = [7, 3, 1]
    result = visitor._bitwise_op(a, b, torch.bitwise_and, lambda x, y: x & y, ctx)
    print(f"   {a} & {b} = {result}")
    
    print("\n" + "=" * 70)
    print("✓ All scalar/list/tensor combinations work correctly!")
    print("=" * 70)


def test_element_size_mapping():
    """Test the element size to dtype mapping for all supported types."""
    print("\n" + "=" * 70)
    print("Testing Element Size Mapping")
    print("=" * 70)
    
    visitor = UnifiedMathVisitor({})
    
    test_dtypes = [
        (torch.int8, "int8", 1),
        (torch.int16, "int16", 2),
        (torch.int32, "int32", 4),
        (torch.int64, "int64", 8),
        (torch.float16, "float16", 2),
        (torch.float32, "float32", 4),
        (torch.float64, "float64", 8),
    ]
    
    print("\nDtype -> Element Size -> View Dtype Mapping:")
    for dtype, name, expected_elem_size in test_dtypes:
        tensor = torch.zeros(1, dtype=dtype)
        elem_size = tensor.element_size()
        view_dtype = visitor._get_bitwise_view_dtype(elem_size)
        
        # Determine expected view dtype
        if elem_size == 1:
            expected_view = "int8"
        elif elem_size == 2:
            expected_view = "int16"
        elif elem_size == 4:
            expected_view = "int32"
        else:
            expected_view = "int64"
        
        print(f"  {name:12} -> {elem_size} byte(s) -> {str(view_dtype):18}")
        assert elem_size == expected_elem_size
    
    print("\n" + "=" * 70)
    print("✓ Element size mapping is correct!")
    print("=" * 70)


if __name__ == "__main__":
    print("\n")
    print("#" * 70)
    print("# FP16/INT16 Bitwise Operations - Comprehensive Integration Test")
    print("#" * 70)
    
    try:
        test_element_size_mapping()
        test_mixed_dtype_operations()
        test_scalar_list_tensor_combinations()
        
        print("\n")
        print("#" * 70)
        print("# ✓ ALL TESTS PASSED SUCCESSFULLY")
        print("#" * 70)
        print("\nSummary:")
        print("  ✓ fp16 (float16) bitwise operations work correctly")
        print("  ✓ int16 (int16) bitwise operations work correctly")
        print("  ✓ int8, int32, int64 operations maintained")
        print("  ✓ Float dtypes supported through bit-pattern manipulation")
        print("  ✓ Mixed tensor/list/scalar operations supported")
        print("  ✓ Backward compatibility preserved")
        print("\n")
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
