#!/usr/bin/env python

"""Tests for `more_math` package."""

import unittest
import torch
from more_math.ConditioningMathNode import ConditioningMathNode
from more_math.LatentMathNode import LatentMathNode
from more_math.ImageMathNode import ImageMathNode
from more_math.FloatMathNode import FloatMathNode

class TestMoreMath(unittest.TestCase):
    # ==========================================
    # Node Initialization and Metadata Tests
    # ==========================================

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

    # ==========================================
    # FFT Tests
    # ==========================================

    def test_fft_invertibility(self):
        # 1. Create random input latent (Batch, Channel, Height, Width)
        input_tensor = torch.randn(1, 4, 32, 32, dtype=torch.float32)
        input_dict = {"samples": input_tensor}
        # 2. Execute ifft(fft(a))
        result = LatentMathNode.execute(
            Latent="ifft(fft(a))",
            a=input_dict
        )
        output_tensor = result[0]["samples"]
        self.assertTrue(torch.allclose(input_tensor, output_tensor, atol=1e-5), \
            f"Max difference: {(input_tensor - output_tensor).abs().max()}")

    def test_image_fft_dims(self):
        # Image input is (Batch, Height, Width, Channel)
        input_tensor = torch.randn(1, 32, 32, 3, dtype=torch.float32)
        result = ImageMathNode.execute(
            Image="ifft(fft(a))",
            a=input_tensor
        )
        output_tensor = result[0]
        self.assertEqual(input_tensor.shape, output_tensor.shape)
        self.assertTrue(torch.allclose(input_tensor, output_tensor, atol=1e-5), \
            f"Image FFT round trip failed. Max diff: {(input_tensor - output_tensor).abs().max()}")

    # ==========================================
    # Latent Math Basic Functions (Evaluated on Tensors)
    # ==========================================

    def test_latent_lerp(self):
        node = LatentMathNode()
        l_a = {"samples": torch.zeros(1, 4, 32, 32)}
        l_b = {"samples": torch.full((1, 4, 32, 32), 10.0)}
        res_lerp = node.execute("lerp(a, b, 0.5)", a=l_a, b=l_b)[0]["samples"]
        self.assertTrue(torch.allclose(res_lerp, torch.full_like(res_lerp, 5.0)))

    def test_latent_step_true(self):
        node = LatentMathNode()
        # step(0.5, a) where a=0.8 -> 1
        res_step = node.execute("step(0.5, a)", a={"samples": torch.full((1,1,1,1), 0.8)})[0]["samples"]
        self.assertTrue(torch.allclose(res_step, torch.ones_like(res_step)))

    def test_latent_step_false(self):
        node = LatentMathNode()
        # step(0.5, a) where a=0.2 -> 0
        res_step2 = node.execute("step(0.5, a)", a={"samples": torch.full((1,1,1,1), 0.2)})[0]["samples"]
        self.assertTrue(torch.allclose(res_step2, torch.zeros_like(res_step2)))

    def test_latent_swap(self):
        node = LatentMathNode()
        t_lat = torch.tensor([0.0, 10.0, 20.0, 30.0]).view(1,4,1,1)
        # Swap channels 0 and 3 -> 30, 10, 20, 0
        l_swap = {"samples": t_lat}
        res_swap = node.execute("swap(a, 1, 0, 3)", a=l_swap)[0]["samples"]
        expected = torch.tensor([30.0, 10.0, 20.0, 0.0]).view(1,4,1,1)
        self.assertTrue(torch.allclose(res_swap, expected))

    def test_latent_relu(self):
        node = LatentMathNode()
        l_a = {"samples": torch.zeros(1, 4, 32, 32)}
        res_relu = node.execute("relu(-5.0)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res_relu, torch.zeros_like(res_relu)))

    def test_latent_sign(self):
        node = LatentMathNode()
        l_a = {"samples": torch.zeros(1, 4, 32, 32)}
        res_sign = node.execute("sign(-5.0)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res_sign, torch.full_like(res_sign, -1.0)))

    def test_latent_fract(self):
        node = LatentMathNode()
        l_a = {"samples": torch.zeros(1, 4, 32, 32)}
        res_fract = node.execute("fract(1.5)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res_fract, torch.full_like(res_fract, 0.5)))

    # ==========================================
    # Float Math Basic Functions (Evaluated on Scalars)
    # ==========================================

    def test_float_lerp(self):
        node = FloatMathNode()
        res = node.execute("lerp(a, b, 0.5)", a=0.0, b=10.0)[0]
        self.assertAlmostEqual(res, 5.0)

    def test_float_step(self):
        node = FloatMathNode()
        res = node.execute("step(0.5, a)", a=0.8)[0]
        self.assertAlmostEqual(res, 1.0)

    def test_float_relu(self):
        node = FloatMathNode()
        res = node.execute("relu(a)", a=-5.0)[0]
        self.assertAlmostEqual(res, 0.0)

    def test_float_smoothstep(self):
        node = FloatMathNode()
        res = node.execute("smoothstep(0, 1, a)", a=0.5)[0]
        self.assertAlmostEqual(res, 0.5)

    # ==========================================
    # Float Math Extended Functions
    # ==========================================

    def test_float_fract(self):
        node = FloatMathNode()
        res = node.execute("fract(a)", a=1.5)[0]
        self.assertAlmostEqual(res, 0.5)

    def test_float_softplus(self):
        node = FloatMathNode()
        res = node.execute("softplus(a)", a=0.0)[0]
        self.assertAlmostEqual(res, 0.69314718, places=5)

    def test_float_sign(self):
        node = FloatMathNode()
        self.assertEqual(node.execute("sign(a)", a=-10.0)[0], -1.0)
        self.assertEqual(node.execute("sign(a)", a=10.0)[0], 1.0)
        self.assertEqual(node.execute("sign(a)", a=0.0)[0], 0.0)

    def test_float_gelu(self):
        node = FloatMathNode()
        self.assertEqual(node.execute("gelu(a)", a=0.0)[0], 0.0)

    # ==========================================
    # Latent Math Extended Functions
    # ==========================================

    def test_latent_smoothstep(self):
        node = LatentMathNode()
        l_a = {"samples": torch.zeros(1, 4, 32, 32)}
        res = node.execute("smoothstep(0, 1, 0.5)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res, torch.full_like(res, 0.5)))

    def test_latent_softplus(self):
        node = LatentMathNode()
        l_a = {"samples": torch.zeros(1, 4, 32, 32)}
        res = node.execute("softplus(0.0)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res, torch.full_like(res, 0.69314718)))

    def test_latent_gelu(self):
        node = LatentMathNode()
        l_a = {"samples": torch.zeros(1, 4, 32, 32)}
        res = node.execute("gelu(0.0)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res, torch.zeros_like(res)))

    # ==========================================
    # Image Math Operations
    # ==========================================

    def test_image_lerp(self):
        node = ImageMathNode()
        img_red = torch.tensor([1.0, 0.0, 0.0]).view(1, 1, 1, 3)
        img_blue = torch.tensor([0.0, 0.0, 1.0]).view(1, 1, 1, 3)
        res_blend = node.execute("lerp(a, b, 0.5)", a=img_red, b=img_blue)[0]
        expected = torch.tensor([0.5, 0.0, 0.5]).view(1, 1, 1, 3)
        self.assertTrue(torch.allclose(res_blend, expected))

    def test_image_swap(self):
        node = ImageMathNode()
        img_red = torch.tensor([1.0, 0.0, 0.0]).view(1, 1, 1, 3)
        img_blue = torch.tensor([0.0, 0.0, 1.0]).view(1, 1, 1, 3)
        res_swap = node.execute("swap(a, 1, 0, 2)", a=img_red)[0]
        self.assertTrue(torch.allclose(res_swap, img_blue))

    # ==========================================
    # Nested Expressions
    # ==========================================

    def test_float_nested_expressions_true(self):
        node = FloatMathNode()
        # lerp(0, 10, step(0.5, 0.8)) -> lerp(0, 10, 1) -> 10
        res = node.execute("lerp(0, 10, step(0.5, 0.8))", a=0.0)[0]
        self.assertEqual(res, 10.0)

    def test_float_nested_expressions_false(self):
        node = FloatMathNode()
        # lerp(0, 10, step(0.5, 0.2)) -> lerp(0, 10, 0) -> 0
        res2 = node.execute("lerp(0, 10, step(0.5, 0.2))", a=0.0)[0]
        self.assertEqual(res2, 0.0)

    # ==========================================
    # 5D Tensor Support
    # ==========================================

    def get_5d_fixture(self):
        # Create a 5D tensor: 1 Batch, 5 Frames, 4 Channels, 32 Height, 32 Width
        samples = torch.randn(1, 5, 4, 32, 32)
        l_in = {"samples": samples}
        return samples, l_in

    def test_5d_tensors_identity(self):
        node = LatentMathNode()
        samples, l_in = self.get_5d_fixture()
        res = node.execute("a * 1.0", a=l_in)[0]["samples"]
        self.assertEqual(res.shape, (1, 5, 4, 32, 32))
        self.assertTrue(torch.allclose(res, samples))

    def test_5d_tensors_variable_T(self):
        node = LatentMathNode()
        samples, l_in = self.get_5d_fixture()
        # In 5D, T maps to dim -4 (size 5)
        res_t = node.execute("a + T", a=l_in)[0]["samples"]
        self.assertTrue(torch.allclose(res_t, samples + 5.0))

    def test_5d_tensors_fft(self):
        node = LatentMathNode()
        samples, l_in = self.get_5d_fixture()
        res_fft = node.execute("ifft(fft(a))", a=l_in)[0]["samples"]
        self.assertTrue(torch.allclose(res_fft, samples, atol=1e-5))

    # ==========================================
    # Noise Math Node 5D Support
    # ==========================================

    def test_noise_math_5d(self):
        from more_math.NoiseMathNode import NoiseMathNode
        class MockNoise:
            def __init__(self, tensor):
                self.tensor = tensor
            def generate_noise(self, input_latent):
                return self.tensor

        node = NoiseMathNode()
        samples = torch.randn(1, 5, 4, 32, 32)
        noise_a = MockNoise(samples)

        result_executor = node.execute("a + T", a=noise_a)[0]
        dummy_latent = {"samples": samples}
        res = result_executor.generate_noise(dummy_latent)

        self.assertEqual(res.shape, (1, 5, 4, 32, 32))
        self.assertTrue(torch.allclose(res, samples + 5.0))

    # ==========================================
    # NestedTensor Support
    # ==========================================

    def test_nested_tensor_support(self):
        try:
            from comfy.nested_tensor import NestedTensor
        except ImportError:
            self.fail("Could not import comfy.nested_tensor.")

        node = LatentMathNode()
        t1 = torch.full((1, 4, 32, 32), 1.0)
        t2 = torch.full((2, 4, 32, 32), 2.0)
        nt_in = NestedTensor([t1, t2])
        l_in = {"samples": nt_in}

        res_lat = node.execute("a + 1.0", a=l_in)[0]["samples"]

        self.assertTrue(getattr(res_lat, 'is_nested', False))
        res_list = res_lat.unbind()
        self.assertEqual(len(res_list), 2)
        self.assertTrue(torch.allclose(res_list[0], torch.full_like(t1, 2.0)))
        self.assertTrue(torch.allclose(res_list[1], torch.full_like(t2, 3.0)))
