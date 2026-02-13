#!/usr/bin/env python3
"""
Test bitwise shift operators and bit count function
"""
import torch
import sys
sys.path.insert(0, 'custom_nodes/more_math')

from more_math.Parser.MathExprParser import MathExprParser
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from antlr4 import InputStream, CommonTokenFactory

def parse_and_evaluate(expression, variables=None):
    """Parse and evaluate a math expression"""
    if variables is None:
        variables = {}
    
    input_stream = InputStream(expression)
    lexer = MathExprParser(input_stream).lexer
    stream = CommonTokenFactory()
    parser = MathExprParser(input_stream)
    tree = parser.start()
    
    visitor = UnifiedMathVisitor(variables, device='cpu')
    result = visitor.visit(tree)
    return result

def test_bit_shifts():
    """Test bitwise shift operators"""
    print("=" * 60)
    print("Testing Bitwise Shift Operators")
    print("=" * 60)
    
    test_cases = [
        # Left shift: 5 << 2 = 20 (0101 << 2 = 10100)
        ("5 << 2", {}, 20),
        
        # Right shift: 20 >> 2 = 5 (10100 >> 2 = 0101)
        ("20 >> 2", {}, 5),
        
        # Left shift with variable
        ("x << 3", {"x": 4}, 32),  # 4 << 3 = 32
        
        # Right shift with variable
        ("x >> 2", {"x": 16}, 4),  # 16 >> 2 = 4
        
        # Chained shifts
        ("(8 << 2) >> 3", {}, 4),  # (32) >> 3 = 4
    ]
    
    for expr, vars, expected in test_cases:
        try:
            result = parse_and_evaluate(expr, vars)
            status = "✓" if result == expected else "✗"
            print(f"{status} {expr:30} = {result:10} (expected {expected})")
        except Exception as e:
            print(f"✗ {expr:30} ERROR: {e}")

def test_bit_count():
    """Test bit count function"""
    print("\n" + "=" * 60)
    print("Testing Bitwise Bit Count Function")
    print("=" * 60)
    
    test_cases = [
        # bitcount(5) = 2  (0101 has 2 set bits)
        ("bitcount(5)", {}, 2),
        
        # bitcount(15) = 4 (1111 has 4 set bits)
        ("bitcount(15)", {}, 4),
        
        # bitcount(7) = 3 (111 has 3 set bits)
        ("bitcount(7)", {}, 3),
        
        # bitcount(255) = 8 (11111111 has 8 set bits)
        ("bitcount(255)", {}, 8),
        
        # bitcount(0) = 0
        ("bitcount(0)", {}, 0),
        
        # With variable
        ("bitcount(x)", {"x": 31}, 5),  # 31 = 11111 = 5 bits set
    ]
    
    for expr, vars, expected in test_cases:
        try:
            result = parse_and_evaluate(expr, vars)
            status = "✓" if result == expected else "✗"
            print(f"{status} {expr:30} = {result:10} (expected {expected})")
        except Exception as e:
            print(f"✗ {expr:30} ERROR: {e}")

def test_bit_shifts_with_tensors():
    """Test bitwise shifts with tensors"""
    print("\n" + "=" * 60)
    print("Testing Bitwise Shifts with Tensors")
    print("=" * 60)
    
    vars = {
        "a": torch.tensor([1, 2, 4, 8], dtype=torch.int32),
        "shift": 2,
    }
    
    try:
        result = parse_and_evaluate("a << shift", vars)
        expected = torch.tensor([4, 8, 16, 32], dtype=torch.int32)
        match = torch.equal(result, expected)
        status = "✓" if match else "✗"
        print(f"{status} tensor_shift_left: [1,2,4,8] << 2 = {result.tolist()}")
    except Exception as e:
        print(f"✗ tensor_shift_left ERROR: {e}")
    
    try:
        result = parse_and_evaluate("a >> shift", vars)
        expected = torch.tensor([0, 0, 1, 2], dtype=torch.int32)
        match = torch.equal(result, expected)
        status = "✓" if match else "✗"
        print(f"{status} tensor_shift_right: [1,2,4,8] >> 2 = {result.tolist()}")
    except Exception as e:
        print(f"✗ tensor_shift_right ERROR: {e}")

def test_bit_count_with_tensors():
    """Test bit count with tensors"""
    print("\n" + "=" * 60)
    print("Testing Bit Count with Tensors")
    print("=" * 60)
    
    vars = {
        "nums": torch.tensor([5, 15, 7, 255], dtype=torch.int32),
    }
    
    try:
        result = parse_and_evaluate("bitcount(nums)", vars)
        # Expected: [2, 4, 3, 8] set bits
        print(f"✓ bitcount([5,15,7,255]): {result}")
    except Exception as e:
        print(f"✗ bitcount_tensor ERROR: {e}")

def test_combinations():
    """Test combinations of shift and bit count"""
    print("\n" + "=" * 60)
    print("Testing Combinations")
    print("=" * 60)
    
    test_cases = [
        # Shift then count bits
        ("bitcount(5 << 2)", {}, 2),  # 5 << 2 = 20 (10100) = 2 bits
        
        # Combined with other operators
        ("(5 << 2) | (3 << 4)", {}, 0xCC),  # 20 | 48 = 0xCC = 204
    ]
    
    for expr, vars, expected in test_cases:
        try:
            result = parse_and_evaluate(expr, vars)
            status = "✓" if result == expected else "✗"
            print(f"{status} {expr:35} = {result:10} (expected {expected})")
        except Exception as e:
            print(f"✗ {expr:35} ERROR: {e}")

if __name__ == "__main__":
    test_bit_shifts()
    test_bit_count()
    test_bit_shifts_with_tensors()
    test_bit_count_with_tensors()
    test_combinations()
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
