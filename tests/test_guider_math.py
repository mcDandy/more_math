import torch
import unittest
from unittest.mock import MagicMock
from more_math.GuiderMathNode import MathGuider

class MockGuider:
    def __init__(self, value, device="cpu"):
        self.value = value
        self.device = device
        self.model_patcher = MagicMock()
        self.model_patcher.load_device = device
        self.model_patcher.offload_device = "cpu"
        self.model_patcher.model_dtype = lambda: torch.float32
        self.original_conds = {}
        self.model_options = {}

    def __call__(self, x, sigma, model_options={}, seed=None):
        return torch.full_like(x, self.value)

class TestMathGuider(unittest.TestCase):
    def test_math_guider_call(self):
        # Setup input guiders
        g0 = MockGuider(1.0)
        g1 = MockGuider(2.0)
        V = {"V0": g0, "V1": g1}
        F = {"F0": 0.5}

        # Expression: Average V0 and V1
        expr = "V0 * 0.5 + V1 * 0.5"

        math_guider = MathGuider(V, F, expr, expr)  # Add expression1 parameter

        # Pseudo input
        x = torch.zeros((1, 4, 16, 16))
        sigma = torch.tensor(1.0)

        # Call
        result = math_guider(x, sigma)

        # Expected: 1.0 * 0.5 + 2.0 * 0.5 = 1.5
        self.assertTrue(torch.allclose(result, torch.tensor(1.5)))

    def test_math_guider_aliases(self):
        g0 = MockGuider(10.0)
        V = {"V0": g0}
        F = {"F0": 2.0}

        # a = V0, w = F0
        expr = "a + w"

        math_guider = MathGuider(V, F, expr, expr)  # Add expression1 parameter
        x = torch.zeros((1, 4, 8, 8))
        sigma = torch.tensor(1.0)

        result = math_guider(x, sigma)
        self.assertTrue(torch.allclose(result, torch.tensor(12.0)))

    def test_math_guider_model_patcher(self):
        # Verify that math_guider exposes model_patcher from its input guider
        g0 = MockGuider(1.0)
        V = {"V0": g0}
        F = {}
        math_guider = MathGuider(V, F, "V0", "V0")  # Add expression1 parameter

        # Check if the property exists and matches g0's patcher
        self.assertIsNotNone(math_guider.model_patcher)
        self.assertEqual(math_guider.model_patcher, g0.model_patcher)

    def test_math_guider_model_patcher_missing(self):
        # Verify behavior when input guiders don't have model_patcher (e.g. None or broken)
        g0 = MockGuider(1.0)
        del g0.model_patcher # force remove
        V = {"V0": g0}
        F = {}
        math_guider = MathGuider(V, F, "V0", "V0")  # Add expression1 parameter
        self.assertIsNone(math_guider.model_patcher)

    def test_math_guider_steps_context(self):
        # Mock sigmas: [10.0, 5.0, 0.0] -> 2 steps
        sigmas = torch.tensor([10.0, 5.0, 0.0])
        g0 = MockGuider(1.0)
        V = {"V0": g0}

        expr = "steps > 0 ? current_step / steps : 0.0"  # Handle division by zero
        math_guider = MathGuider(V, {}, expr, expr)
        math_guider.sigmas = sigmas # sets sigmas directly for testing
        math_guider.steps = len(sigmas) - 1  # steps = num_sigmas - 1 (2 steps)

        # Step 0: sigma = 10.0 (exact match to sigmas[0])
        x = torch.zeros((1, 1, 1, 1))
        res0 = math_guider(x, torch.tensor(10.0))
        # At step 0 with 2 steps: 0 / 2 = 0.0
        self.assertTrue(torch.allclose(res0, torch.tensor(0.0)))

        # Step 1: sigma = 5.0 (exact match to sigmas[1])
        res1 = math_guider(x, torch.tensor(5.0))
        # At step 1 with 2 steps: 1 / 2 = 0.5
        self.assertTrue(torch.allclose(res1, torch.tensor(1.0 / 2.0)))

        # Step 2: sigma = 0.0 (exact match to sigmas[2])
        res2 = math_guider(x, torch.tensor(0.0))
        # At step 2 with 2 steps: 2 / 2 = 1.0
        self.assertTrue(torch.allclose(res2, torch.tensor(1.0)))

    def test_math_guider_crop_function(self):
        """Test crop function within guider context"""
        g0 = MockGuider(1.0)
        V = {"V0": g0}
        F = {}
        
        # Create a guider with crop expression
        # Input shape is (1, 4, 4, 4) = (batch, channel, height, width)
        # crop(a, [0, 1, 1, 1], [1, 2, 2, 2]) extracts 2x2x2 region
        expr = "crop(a, [0, 1, 1, 1], [1, 2, 2, 2])"
        math_guider = MathGuider(V, F, expr, expr)
        
        # Input: 4D tensor (batch, channel, height, width)
        x = torch.ones((1, 4, 4, 4))
        sigma = torch.tensor(1.0)
        
        result = math_guider(x, sigma)
        # Result should be (1, 2, 2, 2)
        self.assertEqual(result.shape, (1, 2, 2, 2))
        self.assertTrue(torch.all(result == 1.0))

    def test_math_guider_text_upper_lower(self):
        """Test numeric expression in guider context"""
        g0 = MockGuider(5.0)  # guider returns tensor of 5.0s
        V = {"V0": g0}
        F = {}
        
        # Simple numeric expression
        expr = "a * 2"
        math_guider = MathGuider(V, F, expr, expr)
        
        x = torch.ones((1, 4, 4, 4))
        sigma = torch.tensor(1.0)
        
        result = math_guider(x, sigma)
        # Expression evaluates to a * 2 where a is the guider output (5.0)
        # So result = 5.0 * 2 = 10.0
        expected = torch.ones((1, 4, 4, 4)) * 10.0
        self.assertTrue(torch.allclose(result, expected))

    def test_math_guider_crop_with_scalar(self):
        """Test crop function with simple position and size"""
        g0 = MockGuider(3.0)  # guider returns tensor of 3.0s
        V = {"V0": g0}
        F = {}
        
        # crop with 4D parameters for 4D input (batch, channel, height, width)
        expr = "crop(a, [0, 0, 0, 0], [1, 2, 2, 2])"
        math_guider = MathGuider(V, F, expr, expr)
        
        x = torch.ones((1, 4, 4, 4))
        sigma = torch.tensor(1.0)
        
        result = math_guider(x, sigma)
        # Result shape should be (1, 2, 2, 2)
        self.assertEqual(result.shape, (1, 2, 2, 2))
        # Values from the cropped region (guider returns 3.0, crop extracts it)
        self.assertTrue(torch.all(result == 3.0))

if __name__ == '__main__':
    unittest.main()
