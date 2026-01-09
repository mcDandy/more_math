#!/usr/bin/env python

"""Tests for `more_math` package."""

import os
import sys

# Ensure test runner (Visual Studio) can import the package regardless of working dir.
# If repository uses `src/` layout, add that to sys.path; otherwise add project root.
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
_src_path = os.path.join(_project_root, "src")

if os.path.isdir(_src_path) and _src_path not in sys.path:
    sys.path.insert(0, _src_path)
elif _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# Add ComfyUI root to path to find 'comfy' and 'comfy_api' packages
_comfy_root = os.path.abspath(os.path.join(_here, "../../.."))
if _comfy_root not in sys.path:
    sys.path.insert(0, _comfy_root)

import torch
from more_math.ConditioningMathNode import ConditioningMathNode
from more_math.LatentMathNode import LatentMathNode
from more_math.ImageMathNode import ImageMathNode
from more_math.FloatMathNode import FloatMathNode
from more_math.AudioMathNode import AudioMathNode


# ==========================================
# Node Initialization and Metadata Tests
# ==========================================


def test_conditioning_math_node_initialization():
    node = ConditioningMathNode()
    assert isinstance(node, ConditioningMathNode)


def test_conditioning_math_node_metadata():
    assert ConditioningMathNode.RETURN_TYPES == ["CONDITIONING"]
    assert ConditioningMathNode.FUNCTION == "EXECUTE_NORMALIZED"
    assert ConditioningMathNode.CATEGORY == "More math"


def test_latent_math_node_initialization():
    node = LatentMathNode()
    assert isinstance(node, LatentMathNode)


def test_latent_math_node_metadata():
    assert LatentMathNode.RETURN_TYPES == ["LATENT"]
    assert LatentMathNode.FUNCTION == "EXECUTE_NORMALIZED"
    assert LatentMathNode.CATEGORY == "More math"


def test_image_math_node_initialization():
    node = ImageMathNode()
    assert isinstance(node, ImageMathNode)


def test_image_math_node_metadata():
    assert ImageMathNode.RETURN_TYPES == ["IMAGE"]
    assert ImageMathNode.FUNCTION == "EXECUTE_NORMALIZED"
    assert ImageMathNode.CATEGORY == "More math"


# ==========================================
# FFT Tests
# ==========================================


def test_fft_invertibility():
    # Create random input latent (Batch, Channel, Height, Width)
    input_tensor = torch.randn(1, 4, 32, 32, dtype=torch.float32)
    input_dict = {"samples": input_tensor}
    # Execute ifft(fft(a))
    result = LatentMathNode.execute(Latent="ifft(fft(a))", a=input_dict)
    output_tensor = result[0]["samples"]
    assert torch.allclose(input_tensor, output_tensor, atol=1e-5), f"Max difference: {(input_tensor - output_tensor).abs().max()}"


def test_image_fft_dims():
    # Image input is (Batch, Height, Width, Channel)
    input_tensor = torch.randn(1, 32, 32, 3, dtype=torch.float32)
    result = ImageMathNode.execute(Image="ifft(fft(a))", a=input_tensor)
    output_tensor = result[0]
    assert input_tensor.shape == output_tensor.shape
    assert torch.allclose(input_tensor, output_tensor, atol=1e-5), (
        f"Image FFT round trip failed. Max diff: {(input_tensor - output_tensor).abs().max()}"
    )


# ==========================================
# Latent Math Basic Functions (Evaluated on Tensors)
# ==========================================


def test_latent_lerp():
    node = LatentMathNode()
    l_a = {"samples": torch.zeros(1, 4, 32, 32)}
    l_b = {"samples": torch.full((1, 4, 32, 32), 10.0)}
    res_lerp = node.execute("lerp(a, b, 0.5)", a=l_a, b=l_b)[0]["samples"]
    assert torch.allclose(res_lerp, torch.full_like(res_lerp, 5.0))


def test_latent_step_true():
    node = LatentMathNode()
    # step(x, edge) where x=0.8, edge=0.5 -> 1
    res_step = node.execute("step(a, 0.5)", a={"samples": torch.full((1, 1, 1, 1), 0.8)})[0]["samples"]
    assert torch.allclose(res_step, torch.ones_like(res_step))


def test_latent_step_false():
    node = LatentMathNode()
    # step(x, edge) where x=0.2, edge=0.5 -> 0
    res_step2 = node.execute("step(a, 0.5)", a={"samples": torch.full((1, 1, 1, 1), 0.2)})[0]["samples"]
    assert torch.allclose(res_step2, torch.zeros_like(res_step2))


def test_latent_swap():
    node = LatentMathNode()
    t_lat = torch.tensor([0.0, 10.0, 20.0, 30.0]).view(1, 4, 1, 1)
    # Swap channels 0 and 3 -> 30, 10, 20, 0
    l_swap = {"samples": t_lat}
    res_swap = node.execute("swap(a, 1, 0, 3)", a=l_swap)[0]["samples"]
    expected = torch.tensor([30.0, 10.0, 20.0, 0.0]).view(1, 4, 1, 1)
    assert torch.allclose(res_swap, expected)


def test_latent_relu():
    node = LatentMathNode()
    l_a = {"samples": torch.zeros(1, 4, 32, 32)}
    res_relu = node.execute("relu(-5.0)", a=l_a)[0]["samples"]
    assert torch.allclose(res_relu, torch.zeros_like(res_relu))


def test_latent_sign():
    node = LatentMathNode()
    l_a = {"samples": torch.zeros(1, 4, 32, 32)}
    res_sign = node.execute("sign(-5.0)", a=l_a)[0]["samples"]
    assert torch.allclose(res_sign, torch.full_like(res_sign, -1.0))


def test_latent_fract():
    node = LatentMathNode()
    l_a = {"samples": torch.zeros(1, 4, 32, 32)}
    res_fract = node.execute("fract(1.5)", a=l_a)[0]["samples"]
    assert torch.allclose(res_fract, torch.full_like(res_fract, 0.5))


# ==========================================
# Float Math Basic Functions (Evaluated on Scalars)
# ==========================================


def test_float_lerp():
    node = FloatMathNode()
    res = node.execute("lerp(a, b, 0.5)", a=0.0, b=10.0)[0]
    assert abs(res - 5.0) < 1e-5


def test_float_step():
    node = FloatMathNode()
    res = node.execute("step(a, 0.5)", a=0.8)[0]
    assert abs(res - 1.0) < 1e-5


def test_float_relu():
    node = FloatMathNode()
    res = node.execute("relu(a)", a=-5.0)[0]
    assert abs(res - 0.0) < 1e-5


def test_float_smoothstep():
    node = FloatMathNode()
    res = node.execute("smoothstep(a, 0, 1)", a=0.5)[0]
    assert abs(res - 0.5) < 1e-5


# ==========================================
# Float Math Extended Functions
# ==========================================


def test_float_fract():
    node = FloatMathNode()
    res = node.execute("fract(a)", a=1.5)[0]
    assert abs(res - 0.5) < 1e-5


def test_float_softplus():
    node = FloatMathNode()
    res = node.execute("softplus(a)", a=0.0)[0]
    assert abs(res - 0.69314718) < 1e-5


def test_float_sign_negative():
    node = FloatMathNode()
    assert node.execute("sign(a)", a=-10.0)[0] == -1.0


def test_float_sign_positive():
    node = FloatMathNode()
    assert node.execute("sign(a)", a=10.0)[0] == 1.0


def test_float_sign_zero():
    node = FloatMathNode()
    assert node.execute("sign(a)", a=0.0)[0] == 0.0


def test_float_gelu():
    node = FloatMathNode()
    assert node.execute("gelu(a)", a=0.0)[0] == 0.0


# ==========================================
# Latent Math Extended Functions
# ==========================================


def test_latent_smoothstep():
    node = LatentMathNode()
    l_a = {"samples": torch.zeros(1, 4, 32, 32)}
    res = node.execute("smoothstep(0.5, 0, 1)", a=l_a)[0]["samples"]
    assert torch.allclose(res, torch.full_like(res, 0.5))


def test_latent_softplus():
    node = LatentMathNode()
    l_a = {"samples": torch.zeros(1, 4, 32, 32)}
    res = node.execute("softplus(0.0)", a=l_a)[0]["samples"]
    assert torch.allclose(res, torch.full_like(res, 0.69314718))


def test_latent_gelu():
    node = LatentMathNode()
    l_a = {"samples": torch.zeros(1, 4, 32, 32)}
    res = node.execute("gelu(0.0)", a=l_a)[0]["samples"]
    assert torch.allclose(res, torch.zeros_like(res))


# ==========================================
# Image Math Operations
# ==========================================


def test_image_lerp():
    node = ImageMathNode()
    img_red = torch.tensor([1.0, 0.0, 0.0]).view(1, 1, 1, 3)
    img_blue = torch.tensor([0.0, 0.0, 1.0]).view(1, 1, 1, 3)
    res_blend = node.execute("lerp(a, b, 0.5)", a=img_red, b=img_blue)[0]
    expected = torch.tensor([0.5, 0.0, 0.5]).view(1, 1, 1, 3)
    assert torch.allclose(res_blend, expected)


def test_image_swap():
    node = ImageMathNode()
    img_red = torch.tensor([1.0, 0.0, 0.0]).view(1, 1, 1, 3)
    img_blue = torch.tensor([0.0, 0.0, 1.0]).view(1, 1, 1, 3)
    res_swap = node.execute("swap(a, 3, 0, 2)", a=img_red)[0]
    assert torch.allclose(res_swap, img_blue)


# ==========================================
# Audio Math Operations
# ==========================================


def test_audio_math_basic():
    node = AudioMathNode()
    waveform = torch.randn(1, 1, 1024)
    audio = {"waveform": waveform, "sample_rate": 44100}
    # result = a * 2.0
    res = node.execute("a * 2.0", a=audio)[0]
    assert isinstance(res, dict)
    assert "waveform" in res
    assert res["sample_rate"] == 44100
    assert torch.allclose(res["waveform"], waveform * 2.0)


# ==========================================
# Nested Expressions
# ==========================================


def test_float_nested_expressions_true():
    node = FloatMathNode()
    # lerp(0, 10, step(0.8, 0.5)) -> lerp(0, 10, 1) -> 10
    res = node.execute("lerp(0, 10, step(0.8, 0.5))", a=0.0)[0]
    assert res == 10.0


def test_float_nested_expressions_false():
    node = FloatMathNode()
    # lerp(0, 10, step(0.2, 0.5)) -> lerp(0, 10, 0) -> 0
    res2 = node.execute("lerp(0, 10, step(0.2, 0.5))", a=0.0)[0]
    assert res2 == 0.0


# ==========================================
# 5D Tensor Support
# ==========================================


def test_5d_tensors_identity():
    node = LatentMathNode()
    samples = torch.randn(1, 5, 4, 32, 32)
    l_in = {"samples": samples}
    res = node.execute("a * 1.0", a=l_in)[0]["samples"]
    assert res.shape == (1, 5, 4, 32, 32)
    assert torch.allclose(res, samples)


def test_5d_tensors_variable_T():
    node = LatentMathNode()
    samples = torch.randn(1, 5, 4, 32, 32)
    l_in = {"samples": samples}
    # In 5D, T maps to dim -4 (size 5)
    res_t = node.execute("a + T", a=l_in)[0]["samples"]
    assert torch.allclose(res_t, samples + 5.0)


def test_5d_tensors_fft():
    node = LatentMathNode()
    samples = torch.randn(1, 5, 4, 32, 32)
    l_in = {"samples": samples}
    res_fft = node.execute("ifft(fft(a))", a=l_in)[0]["samples"]
    assert torch.allclose(res_fft, samples, atol=1e-5)


# ==========================================
# Noise Math Node 5D Support
# ==========================================


def test_noise_math_5d():
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

    assert res.shape == (1, 5, 4, 32, 32)
    assert torch.allclose(res, samples + 5.0)


# ==========================================
# NestedTensor Support
# ==========================================


def test_nested_tensor_support():
    try:
        from comfy.nested_tensor import NestedTensor
    except ImportError:
        assert False, "Could not import comfy.nested_tensor."

    node = LatentMathNode()
    t1 = torch.full((1, 4, 32, 32), 1.0)
    t2 = torch.full((2, 4, 32, 32), 2.0)
    nt_in = NestedTensor([t1, t2])
    l_in = {"samples": nt_in}

    res_lat = node.execute("a + 1.0", a=l_in)[0]["samples"]

    assert getattr(res_lat, "is_nested", False)
    res_list = res_lat.unbind()
    assert len(res_list) == 2
    assert torch.allclose(res_list[0], torch.full_like(t1, 2.0))
    assert torch.allclose(res_list[1], torch.full_like(t2, 3.0))


# ==========================================
# Comprehensive Math Function Tests
# ==========================================


def test_trig_functions():
    node = FloatMathNode()
    # Sin/Cos checks
    # sin(0) = 0, cos(0) = 1
    assert abs(node.execute("sin(0)", a=0.0)[0] - 0.0) < 1e-5
    assert abs(node.execute("cos(0)", a=0.0)[0] - 1.0) < 1e-5
    # tan(0) = 0
    assert abs(node.execute("tan(0)", a=0.0)[0] - 0.0) < 1e-5


def test_inverse_trig_functions():
    node = FloatMathNode()
    # asin(0) = 0, acos(1) = 0, atan(0) = 0
    assert abs(node.execute("asin(0)", a=0.0)[0] - 0.0) < 1e-5
    assert abs(node.execute("acos(1)", a=0.0)[0] - 0.0) < 1e-5
    assert abs(node.execute("atan(0)", a=0.0)[0] - 0.0) < 1e-5


def test_pow_log_functions():
    node = FloatMathNode()
    # pow(2, 3) = 8
    assert abs(node.execute("pow(2, 3)", a=0.0)[0] - 8.0) < 1e-5
    # sqrt(4) = 2
    assert abs(node.execute("sqrt(4)", a=0.0)[0] - 2.0) < 1e-5
    # exp(0) = 1
    assert abs(node.execute("exp(0)", a=0.0)[0] - 1.0) < 1e-5
    # log(100) = 2 (base 10)
    assert abs(node.execute("log(100)", a=0.0)[0] - 2.0) < 1e-5
    # ln(e) = 1. Using 'e' constant logic check or approx 2.718
    assert abs(node.execute("ln(2.7182818)", a=0.0)[0] - 1.0) < 1e-4


def test_min_max_functions():

    node = FloatMathNode()
    print("Testing tmin...", flush=True)
    # tmin(2, 5) = 2, tmax(2, 5) = 5
    assert abs(node.execute("tmin(2, 5)", a=0.0)[0] - 2.0) < 1e-5
    print("Testing tmax...", flush=True)
    assert abs(node.execute("tmax(2, 5)", a=0.0)[0] - 5.0) < 1e-5

    # smin/smax (Smooth min/max? Or just multi-arg min/max? TensorEvalVisitor uses stack.min/max)
    # smin(1, 2, 3) = 1
    print("Testing smin...", flush=True)
    res_smin = node.execute("smin(1, 2, 3)", a=0.0)[0]
    print(f"smin result: {res_smin} type: {type(res_smin)}", flush=True)
    assert abs(res_smin - 1.0) < 1e-5

    print("Testing smax...", flush=True)
    res_smax = node.execute("smax(1, 2, 3)", a=0.0)[0]
    print(f"smax result: {res_smax} type: {type(res_smax)}", flush=True)
    assert abs(res_smax - 3.0) < 1e-5


def test_basic_utilities():
    node = FloatMathNode()
    # abs(-5) = 5
    assert abs(node.execute("abs(-5)", a=0.0)[0] - 5.0) < 1e-5
    # floor(1.9) = 1
    assert abs(node.execute("floor(1.9)", a=0.0)[0] - 1.0) < 1e-5
    # ceil(1.1) = 2
    assert abs(node.execute("ceil(1.1)", a=0.0)[0] - 2.0) < 1e-5
    # round(1.6) = 2, round(1.4) = 1
    assert abs(node.execute("round(1.6)", a=0.0)[0] - 2.0) < 1e-5
    assert abs(node.execute("round(1.4)", a=0.0)[0] - 1.0) < 1e-5
    # clamp(10, 0, 5) = 5, clamp(-5, 0, 5) = 0
    assert abs(node.execute("clamp(10, 0, 5)", a=0.0)[0] - 5.0) < 1e-5
    assert abs(node.execute("clamp(-5, 0, 5)", a=0.0)[0] - 0.0) < 1e-5


def test_advanced_activations():
    node = FloatMathNode()
    # sigm(0) = 0.5
    assert abs(node.execute("sigm(0)", a=0.0)[0] - 0.5) < 1e-5


if __name__ == "__main__":
    import sys

    try:
        test_conditioning_math_node_initialization()
        test_conditioning_math_node_metadata()
        test_latent_math_node_initialization()
        test_latent_math_node_metadata()
        test_image_math_node_initialization()
        test_image_math_node_metadata()
        test_trig_functions()
        test_inverse_trig_functions()
        test_pow_log_functions()
        test_min_max_functions()
        test_basic_utilities()
        test_advanced_activations()
        print("All tests passed!")
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
    print("All tests in test_more_math.py passed!")
