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
        G = {"G0": g0, "G1": g1}
        F = {"F0": 0.5}

        # Expression: Average G0 and G1
        expr = "G0 * 0.5 + G1 * 0.5"

        math_guider = MathGuider(G, F, expr)

        # Pseudo input
        x = torch.zeros((1, 4, 16, 16))
        sigma = torch.tensor(1.0)

        # Call
        result = math_guider(x, sigma)

        # Expected: 1.0 * 0.5 + 2.0 * 0.5 = 1.5
        self.assertTrue(torch.allclose(result, torch.tensor(1.5)))

    def test_math_guider_aliases(self):
        g0 = MockGuider(10.0)
        G = {"G0": g0}
        F = {"F0": 2.0}

        # a = G0, w = F0
        expr = "a + w"

        math_guider = MathGuider(G, F, expr)
        x = torch.zeros((1, 4, 8, 8))
        sigma = torch.tensor(1.0)

        result = math_guider(x, sigma)
        self.assertTrue(torch.allclose(result, torch.tensor(12.0)))

    def test_math_guider_model_patcher(self):
        # Verify that math_guider exposes model_patcher from its input guider
        g0 = MockGuider(1.0)
        G = {"G0": g0}
        F = {}
        math_guider = MathGuider(G, F, "G0")

        # Check if the property exists and matches g0's patcher
        self.assertIsNotNone(math_guider.model_patcher)
        self.assertEqual(math_guider.model_patcher, g0.model_patcher)

    def test_math_guider_model_patcher_missing(self):
        # Verify behavior when input guiders don't have model_patcher (e.g. None or broken)
        g0 = MockGuider(1.0)
        del g0.model_patcher # force remove
        G = {"G0": g0}
        F = {}
        math_guider = MathGuider(G, F, "G0")
        self.assertIsNone(math_guider.model_patcher)

    def test_math_guider_steps_context(self):
        # Mock sigmas: [10.0, 5.0, 0.0] -> 2 steps
        sigmas = torch.tensor([10.0, 5.0, 0.0])
        g0 = MockGuider(1.0)
        G = {"G0": g0}

        math_guider = MathGuider(G, {}, "current_step / steps")
        math_guider.sigmas = sigmas # sets sigmas directly for testing

        # Step 0: sigma = 10.0
        x = torch.zeros((1, 1, 1, 1))
        res0 = math_guider(x, torch.tensor(10.0))
        self.assertTrue(torch.allclose(res0, torch.tensor(0.0 / 2.0)))

        # Step 1: sigma = 5.0
        res1 = math_guider(x, torch.tensor(5.0))
        self.assertTrue(torch.allclose(res1, torch.tensor(1.0 / 2.0)))

        # Intermediate sigma should find closest
        res_near = math_guider(x, torch.tensor(4.8))
        self.assertTrue(torch.allclose(res_near, torch.tensor(1.0 / 2.0)))

if __name__ == '__main__':
    unittest.main()
