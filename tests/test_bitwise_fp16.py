#!/usr/bin/env python3
"""Test script to verify fp16 and int16 support in bitwise operations."""

import sys
import os
import torch

# Add the custom_nodes/more_math directory to path
sys.path.insert(0, os.path.dirname(__file__))

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor

def test_bitwise_fp16():
    """Test bitwise NOT operation with fp16 tensors."""
    print("Testing bitwise operations with fp16...")
    
    # Create fp16 tensors
    a_fp16 = torch.tensor([1.5, 2.5, 3.5], dtype=torch.float16)
    
    variables = {"a": a_fp16}
    visitor = UnifiedMathVisitor(variables, shape=(3,))
    
    # Test bitwise NOT
    result = visitor._bitwise_not(a_fp16)
    print(f"  fp16 tensor: {a_fp16}")
    print(f"  bitwise_not result dtype: {result.dtype}")
    assert result.dtype == torch.float16, f"Expected float16, got {result.dtype}"
    print("  ✓ fp16 bitwise NOT test passed")

def test_bitwise_int16():
    """Test bitwise NOT operation with int16 tensors."""
    print("Testing bitwise operations with int16...")
    
    # Create int16 tensors
    a_int16 = torch.tensor([1, 2, 3], dtype=torch.int16)
    
    variables = {"a": a_int16}
    visitor = UnifiedMathVisitor(variables, shape=(3,))
    
    # Test bitwise NOT
    result = visitor._bitwise_not(a_int16)
    print(f"  int16 tensor: {a_int16}")
    print(f"  bitwise_not result dtype: {result.dtype}")
    assert result.dtype == torch.int16, f"Expected int16, got {result.dtype}"
    print("  ✓ int16 bitwise NOT test passed")

def test_bitwise_and_int16():
    """Test bitwise AND operation with int16 tensors."""
    print("Testing bitwise AND with int16...")
    
    a = torch.tensor([7, 14, 21], dtype=torch.int16)
    b = torch.tensor([3, 5, 7], dtype=torch.int16)
    
    variables = {"a": a, "b": b}
    visitor = UnifiedMathVisitor(variables)
    
    # Test bitwise AND
    result = visitor._bitwise_op(a, b, torch.bitwise_and, lambda x, y: x & y)
    print(f"  a: {a}, b: {b}")
    print(f"  bitwise_and result: {result}")
    assert result.dtype in [torch.int16, torch.int32], f"Unexpected dtype {result.dtype}"
    print("  ✓ int16 bitwise AND test passed")

def test_bitwise_int8():
    """Test bitwise operations with int8 tensors."""
    print("Testing bitwise operations with int8...")
    
    a_int8 = torch.tensor([1, 2, 3], dtype=torch.int8)
    
    variables = {"a": a_int8}
    visitor = UnifiedMathVisitor(variables, shape=(3,))
    
    # Test bitwise NOT
    result = visitor._bitwise_not(a_int8)
    print(f"  int8 tensor: {a_int8}")
    print(f"  bitwise_not result dtype: {result.dtype}")
    assert result.dtype == torch.int8, f"Expected int8, got {result.dtype}"
    print("  ✓ int8 bitwise NOT test passed")

def test_get_bitwise_view_dtype():
    """Test the element size to dtype mapping function."""
    print("Testing _get_bitwise_view_dtype...")
    
    visitor = UnifiedMathVisitor({})
    
    # Test various element sizes
    test_cases = [
        (1, torch.int8),
        (2, torch.int16),
        (4, torch.int32),
        (8, torch.int64),
    ]
    
    for elem_size, expected_dtype in test_cases:
        result_dtype = visitor._get_bitwise_view_dtype(elem_size)
        print(f"  element_size={elem_size} -> {result_dtype}")
        assert result_dtype == expected_dtype, f"Expected {expected_dtype}, got {result_dtype}"
    
    print("  ✓ All element size mappings correct")

if __name__ == "__main__":
    print("=" * 60)
    print("Testing fp16 and int16 support in bitwise operations")
    print("=" * 60)
    
    try:
        test_get_bitwise_view_dtype()
        print()
        test_bitwise_int8()
        print()
        test_bitwise_int16()
        print()
        test_bitwise_fp16()
        print()
        test_bitwise_and_int16()
        print()
        print("=" * 60)
        print("✓ All tests passed successfully!")
        print("=" * 60)
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
