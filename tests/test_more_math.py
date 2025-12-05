#!/usr/bin/env python

"""Tests for `more_math` package."""

import unittest
import torch
from more_math.ConditioningMathNode import ConditioningMathNode
from more_math.LatentMathNode import LatentMathNode
from more_math.LatentMathNode import LatentMathNode
from more_math.ImageMathNode import ImageMathNode
from more_math.FloatMathNode import FloatMathNode
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

    def test_new_math_functions(self):
        node = LatentMathNode()
        # Test Lerp
        # lerp(a, b, 0.5) where a=0, b=10 -> 5
        l_a = {"samples": torch.zeros(1, 4, 32, 32)}
        l_b = {"samples": torch.full((1, 4, 32, 32), 10.0)}
        res_lerp = node.execute("lerp(a, b, 0.5)", a=l_a, b=l_b)[0]["samples"]
        self.assertTrue(torch.allclose(res_lerp, torch.full_like(res_lerp, 5.0)))

        # Test Step
        # step(0.5, a) where a=0.8 -> 1
        res_step = node.execute("step(0.5, a)", a={"samples": torch.full((1,1,1,1), 0.8)})[0]["samples"]
        self.assertTrue(torch.allclose(res_step, torch.ones_like(res_step)))
        # step(0.5, a) where a=0.2 -> 0
        res_step2 = node.execute("step(0.5, a)", a={"samples": torch.full((1,1,1,1), 0.2)})[0]["samples"]
        self.assertTrue(torch.allclose(res_step2, torch.zeros_like(res_step2)))

        # Test Swap
        # tensor 1x3: [0, 1, 2]. Swap(dim=1, 0, 2) -> [2, 1, 0]
        t = torch.tensor([[[0.0, 1.0, 2.0]]]) # 1x1x3
        l_t = {"samples": t}
        # dim 2 (channel dim in 1x1x3? No, dims are B,C,H,W usually but here shape is 1x1x3)
        # LatentMathNode uses "samples" directly.
        # eval_single_tensor exposes 'a'.
        # Let's use simple Latent 1x4x1x1 (B,C,H,W)
        t_lat = torch.tensor([0.0, 10.0, 20.0, 30.0]).view(1,4,1,1)
        # Swap channels 0 and 3 -> 30, 10, 20, 0
        l_swap = {"samples": t_lat}
        # swap(a, 1, 0, 3) . Dim 1 is channel (B=0, C=1)
        res_swap = node.execute("swap(a, 1, 0, 3)", a=l_swap)[0]["samples"]
        expected = torch.tensor([30.0, 10.0, 20.0, 0.0]).view(1,4,1,1)
        self.assertTrue(torch.allclose(res_swap, expected))

        # Test Relu, Sign, Fract
        res_relu = node.execute("relu(-5.0)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res_relu, torch.zeros_like(res_relu)))
        
        res_sign = node.execute("sign(-5.0)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res_sign, torch.full_like(res_sign, -1.0)))

        res_fract = node.execute("fract(1.5)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res_fract, torch.full_like(res_fract, 0.5)))

    def test_float_math_functions(self):
        node = FloatMathNode()
        # Test Lerp: lerp(0, 10, 0.5) -> 5.0
        res = node.execute("lerp(a, b, 0.5)", a=0.0, b=10.0)[0]
        self.assertAlmostEqual(res, 5.0)

        # Test Step: step(0.5, 0.8) -> 1.0
        res = node.execute("step(0.5, a)", a=0.8)[0]
        self.assertAlmostEqual(res, 1.0)
        
        # Test Relu: relu(-5) -> 0.0
        res = node.execute("relu(a)", a=-5.0)[0]
        self.assertAlmostEqual(res, 0.0)
        
        # Test Smoothstep: smoothstep(0, 1, 0.5) -> 0.5
        # 0.5*0.5*(3 - 2*0.5) = 0.25 * 2 = 0.5
        res = node.execute("smoothstep(0, 1, a)", a=0.5)[0]
        self.assertAlmostEqual(res, 0.5)

