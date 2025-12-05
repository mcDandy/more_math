#!/usr/bin/env python

"""Tests for `more_math` package."""

import unittest
import torch
from more_math.ConditioningMathNode import ConditioningMathNode
from more_math.LatentMathNode import LatentMathNode
from more_math.ImageMathNode import ImageMathNode
import tokenize
from io import StringIO

def tokenize_expression(expr):
    if not expr.endswith('\n'):
        expr = expr + '\n'
    f = StringIO(expr)
    tokens = tokenize.generate_tokens(f.readline)
    filtered_tokens = []
    for toktype, tokval, _, _, _ in tokens:
        token_name = tokenize.tok_name[toktype]
        # Opravíme ERRORTOKEN na OP pro !, &, |, ^
        if token_name == 'ERRORTOKEN' and tokval in {'!', '&', '|', '^'}:
            token_name = 'OP'
        if token_name in {'COMMENT', 'NL', 'NEWLINE', 'INDENT', 'DEDENT'}:
            continue
        filtered_tokens.append((token_name, tokval.strip()))
    return filtered_tokens


class TestMoreMath(unittest.TestCase):
    def test_conditioning_math_node_initialization(self):
        node = ConditioningMathNode()
        self.assertIsInstance(node, ConditioningMathNode)

    def test_conditioning_math_node_metadata(self):
        self.assertEqual(ConditioningMathNode.RETURN_TYPES, ["CONDITIONING"])
        self.assertEqual(ConditioningMathNode.FUNCTION, "EXECUTE_NORMALIZED")
        self.assertEqual(ConditioningMathNode.CATEGORY, "More math")

    def test_latent_math_node_initialization(self):
        node = LatentMathNode()
        self.assertIsInstance(node, LatentMathNode)

    def test_latent_math_node_metadata(self):
        self.assertEqual(LatentMathNode.RETURN_TYPES, ["LATENT"])
        self.assertEqual(LatentMathNode.FUNCTION, "EXECUTE_NORMALIZED")
        self.assertEqual(LatentMathNode.CATEGORY, "More math")

    def test_image_math_node_initialization(self):
        node = ImageMathNode()
        self.assertIsInstance(node, ImageMathNode)

    def test_image_math_node_metadata(self):
        self.assertEqual(ImageMathNode.RETURN_TYPES, ["IMAGE"])
        self.assertEqual(ImageMathNode.FUNCTION, "EXECUTE_NORMALIZED")
        self.assertEqual(ImageMathNode.CATEGORY, "More math")

    def test_fft_invertibility(self):
        # 1. Create random input latent (Batch, Channel, Height, Width)
        input_tensor = torch.randn(1, 4, 32, 32, dtype=torch.float32)
        input_dict = {"samples": input_tensor}
    
        # 2. Execute ifft(fft(a))
        # Note: execute is a classmethod
        result = LatentMathNode.execute(
            Latent="ifft(fft(a))",
            a=input_dict
        )
    
        # 3. Get output tensor
        output_tensor = result[0]["samples"]
    
        # 4. Check correctness (approximate equality)
        self.assertTrue(torch.allclose(input_tensor, output_tensor, atol=1e-5), \
            f"Max difference: {(input_tensor - output_tensor).abs().max()}")

    def test_image_fft_dims(self):
        # Image input is (Batch, Height, Width, Channel)
        # Verify 2D FFT works by doing a round trip
        input_tensor = torch.randn(1, 32, 32, 3, dtype=torch.float32)
        
        result = ImageMathNode.execute(
            Image="ifft(fft(a))",
            a=input_tensor
        )
        output_tensor = result[0]
        
        self.assertEqual(input_tensor.shape, output_tensor.shape)
        self.assertTrue(torch.allclose(input_tensor, output_tensor, atol=1e-5), \
            f"Image FFT round trip failed. Max diff: {(input_tensor - output_tensor).abs().max()}")


