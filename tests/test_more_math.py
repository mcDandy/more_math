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
        res = node.execute("smoothstep(0, 1, a)", a=0.5)[0]
        self.assertAlmostEqual(res, 0.5)

    def test_float_math_extended(self):
        node = FloatMathNode()
        # Test Fract: fract(1.5) -> 0.5
        res = node.execute("fract(a)", a=1.5)[0]
        self.assertAlmostEqual(res, 0.5)
        
        # Test Softplus: softplus(0) = log(1+exp(0)) = log(2) ~= 0.6931
        res = node.execute("softplus(a)", a=0.0)[0]
        self.assertAlmostEqual(res, 0.69314718, places=5)
        
        # Test Sign: sign(-10) -> -1.0, sign(10) -> 1.0, sign(0) -> 0.0
        self.assertEqual(node.execute("sign(a)", a=-10.0)[0], -1.0)
        self.assertEqual(node.execute("sign(a)", a=10.0)[0], 1.0)
        self.assertEqual(node.execute("sign(a)", a=0.0)[0], 0.0)

        # Test Gelu: gelu(0) -> 0.0
        self.assertEqual(node.execute("gelu(a)", a=0.0)[0], 0.0)

    def test_latent_math_extended(self):
        node = LatentMathNode()
        l_a = {"samples": torch.zeros(1, 4, 32, 32)}
        
        # Smoothstep
        # smoothstep(0, 1, 0.5) -> 0.5
        res = node.execute("smoothstep(0, 1, 0.5)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res, torch.full_like(res, 0.5)))
        
        # Softplus
        res = node.execute("softplus(0.0)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res, torch.full_like(res, 0.69314718)))

        # Gelu
        res = node.execute("gelu(0.0)", a=l_a)[0]["samples"]
        self.assertTrue(torch.allclose(res, torch.zeros_like(res)))

    def test_image_math_operations(self):
        node = ImageMathNode()
        # Image is (Batch, Height, Width, Channel)
        # Create Red image [1, 0, 0] and Blue image [0, 0, 1]
        img_red = torch.tensor([1.0, 0.0, 0.0]).view(1, 1, 1, 3)
        img_blue = torch.tensor([0.0, 0.0, 1.0]).view(1, 1, 1, 3)
        
        # Test Lerp (Blend)
        # lerp(red, blue, 0.5) -> [0.5, 0.0, 0.5] (Purple)
        res_blend = node.execute("lerp(a, b, 0.5)", a=img_red, b=img_blue)[0]
        expected = torch.tensor([0.5, 0.0, 0.5]).view(1, 1, 1, 3)
        self.assertTrue(torch.allclose(res_blend, expected))
        
        # Test Swap Channels (Red <-> Blue)
        # Input: Red [1, 0, 0]. Swap R(0) and B(2). Result: [0, 0, 1] (Blue)
        # Note: In ImageMathNode, Channel is dim 1 (internally permuted to B,C,H,W)
        res_swap = node.execute("swap(a, 1, 0, 2)", a=img_red)[0]
        self.assertTrue(torch.allclose(res_swap, img_blue))

    def test_nested_expressions(self):
        node = FloatMathNode()
        # lerp(0, 10, step(0.5, 0.8)) -> lerp(0, 10, 1) -> 10
        res = node.execute("lerp(0, 10, step(0.5, 0.8))", a=0.0)[0]
        self.assertEqual(res, 10.0)
        
        # lerp(0, 10, step(0.5, 0.2)) -> lerp(0, 10, 0) -> 0
        res2 = node.execute("lerp(0, 10, step(0.5, 0.2))", a=0.0)[0]
        self.assertEqual(res2, 0.0)

    def test_5d_tensors(self):
        # Test support for 5D tensors: (Batch, Time, Channel, Height, Width)
        # LatentMathNode expects this structure if ndim >= 5.
        
        node = LatentMathNode()
        # Create a 5D tensor: 1 Batch, 5 Frames, 4 Channels, 32 Height, 32 Width
        # Shape: (1, 5, 4, 32, 32)
        samples = torch.randn(1, 5, 4, 32, 32)
        l_in = {"samples": samples}
        
        # Test 1: Identity/Passthrough using a basic operation
        # a * 1.0 should return same shape and values
        res = node.execute("a * 1.0", a=l_in)[0]["samples"]
        self.assertEqual(res.shape, (1, 5, 4, 32, 32))
        self.assertTrue(torch.allclose(res, samples))
        
        # Test 2: Accessing 'T' (batch_count/time) variable
        # In 5D, T maps to dim -4 (size 5)
        # Expression: "a + T" -> Adds 5.0 to every element
        res_t = node.execute("a + T", a=l_in)[0]["samples"]
        self.assertTrue(torch.allclose(res_t, samples + 5.0))
        
        # Test 3: FFT on 5D tensor
        # FFT logic operates on dims [2:] -> (Channel, Height, Width) for 5D input?? 
        # Wait, LatentMathNode.eval_single_tensor sets:
        # channel_dim = -3, height_dim = -2, width = -1.
        # So for (B, T, C, H, W), it processes C, H, W as spatial?
        # Let's verify standard roundtrip
        res_fft = node.execute("ifft(fft(a))", a=l_in)[0]["samples"]
        self.assertTrue(torch.allclose(res_fft, samples, atol=1e-5))

    def test_noise_math_5d(self):
        # NoiseMathNode takes objects that have a 'generate_noise' method.
        # We need to mock this for testing.
        from more_math.NoiseMathNode import NoiseMathNode
        
        class MockNoise:
            def __init__(self, tensor):
                self.tensor = tensor
            def generate_noise(self, input_latent):
                # Return the stored tensor, ignoring input_latent for this test
                return self.tensor

        node = NoiseMathNode()
        # Create 5D tensor (1, 5, 4, 32, 32)
        samples = torch.randn(1, 5, 4, 32, 32)
        
        # In NoiseMathNode, 'input_latent' is passed to generate_noise. 
        # The node execution logic calls generate_noise on inputs a,b,c,d.
        # But wait, NoiseMathNode.execute returns a NoiseExecutor object.
        # The actual calculation happens when NoiseExecutor.generate_noise() is called.
        
        noise_a = MockNoise(samples)
        
        # 1. Execute node to get executor
        # Noise="a + T"
        # We need to verify that T is 5 (frames) not 1 (batch)
        result_executor = node.execute("a + T", a=noise_a)[0]
        
        # 2. Call generate_noise on the result executor
        # We need to pass a dummy input_latent because generate_noise expects it.
        # The input_latent structure dictates dimensions if a,b,c,d don't override?
        # Actually NoiseMathNode uses the 'samples' from input_latent as 'merged_samples' usually?
        # Let's check logic:
        # samples = input_latent["samples"]
        # a_val = self.a.generate_noise()
        # ...
        # if samples is nested... 
        # else: merged_samples = samples. 
        #
        # So 'merged_samples' comes from 'input_latent' passed to generate_noise!
        # The 'a' input is just a generator. 
        # So to test 5D support, we must pass a 5D latent to generate_noise.
        
        dummy_latent = {"samples": samples} # This sets the context dimensions
        
        # If we pass a MockNoise that returns 'samples', then a_val will be 'samples'.
        # And merged_samples will be 'samples'.
        # So a + T -> samples + frame_count.
        
        res = result_executor.generate_noise(dummy_latent)
        
        self.assertEqual(res.shape, (1, 5, 4, 32, 32))
        res = result_executor.generate_noise(dummy_latent)
        
        self.assertEqual(res.shape, (1, 5, 4, 32, 32))
        self.assertTrue(torch.allclose(res, samples + 5.0), 
                        f"Expected samples + 5.0, got {res[0,0,0,0,0]} vs {samples[0,0,0,0,0]+5.0}")

    def test_nested_tensor_support(self):
        # Test compatibility with comfy.nested_tensor.NestedTensor
        try:
            from comfy.nested_tensor import NestedTensor
        except ImportError:
            # If comfy is not in path or fails to import, we might need to skip or mock
            # But run_tests.py adds the root, so it should work.
            # If it fails, fail the test to alert us.
            self.fail("Could not import comfy.nested_tensor. Make sure ComfyUI root is in sys.path")

        node = LatentMathNode()
        
        # Create two tensors with different dimensions to simulate nesting
        # Tensor 1: (1, 4, 32, 32)
        t1 = torch.full((1, 4, 32, 32), 1.0)
        # Tensor 2: (2, 4, 32, 32)
        t2 = torch.full((2, 4, 32, 32), 2.0)
        
        # Create NestedTensor
        nt_in = NestedTensor([t1, t2])
        l_in = {"samples": nt_in}
        
        # Operation: a + 1.0
        # Expected: t1 becomes 2.0s, t2 becomes 3.0s
        res_lat = node.execute("a + 1.0", a=l_in)[0]["samples"]
        
        # Verify result is NestedTensor
        self.assertTrue(getattr(res_lat, 'is_nested', False), "Result should be a NestedTensor")
        
        # Verify contents
        res_list = res_lat.unbind()
        self.assertEqual(len(res_list), 2)
        
        self.assertTrue(torch.allclose(res_list[0], torch.full_like(t1, 2.0)))
        self.assertTrue(torch.allclose(res_list[1], torch.full_like(t2, 3.0)))


