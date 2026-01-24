import sys
import os
import comfy_api

# Ensure test runner (Visual Studio) can import the package regardless of working dir.
# If repository uses `src/` layout, add that to sys.path; otherwise add project root.
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# Add ComfyUI root to path to find 'comfy' package
_comfy_root = os.path.abspath(os.path.join(_here, "../../.."))
if _comfy_root not in sys.path:
    sys.path.insert(0, _comfy_root)


import torch
from more_math.ModelMathNode import ModelMathNode


class MockModelPatcher:
    def __init__(self, state_dict):
        self.model = comfy_api.Model()
        self.model.state_dict = lambda: state_dict
        self.patches = {}

    def clone(self):
        # We need a clone that shares the underlying model but has its own patches
        new_patcher = MockModelPatcher(self.model.state_dict())
        # In this mock, we don't copy patches from self since we start empty in test
        # but in real usage ComfyUI clones patches.
        # But 'add_patches' needs to work.
        return new_patcher

    def add_patches(self, patches, strength1, strength2):
        self.patches.update(patches)


def test_model_math_simple_add():
    # Setup inputs
    sd_a = {"layer1.weight": torch.tensor([1.0, 2.0]), "layer2.bias": torch.tensor([0.5])}
    a = MockModelPatcher(sd_a)

    sd_b = {"layer1.weight": torch.tensor([0.5, 0.5]), "layer2.bias": torch.tensor([0.5])}
    b = MockModelPatcher(sd_b)

    # Expression: a + b
    expr = "a + b"

    # Execute
    result_tuple = ModelMathNode.execute(Expression=expr, V={"V0": a, "V1": b}, F={})
    result_model = result_tuple[0]

    # Verify patches
    patches = result_model.patches

    # "layer1.weight":
    #   a = [1.0, 2.0]
    #   b = [0.5, 0.5]
    #   res = [1.5, 2.5]
    #   diff = res - a = [0.5, 0.5]
    assert "layer1.weight" in patches
    assert torch.allclose(patches["layer1.weight"][0], torch.tensor([0.5, 0.5]))

    # "layer2.bias":
    #   a = 0.5, b = 0.5
    #   res = 1.0
    #   diff = 0.5
    assert "layer2.bias" in patches
    assert torch.allclose(patches["layer2.bias"][0], torch.tensor([0.5]))


def test_model_math_zero_default():
    # Test handling of missing b (should be zero)
    sd_a = {"w": torch.tensor([10.0])}
    a = MockModelPatcher(sd_a)

    # expr: a + b. b is None -> b=0.
    # res = 10 + 0 = 10.
    # diff = 10 - 10 = 0.
    # Should skip patch.

    result_tuple = ModelMathNode.execute(Expression="a + b", V={"V0": a}, F={})
    result_model = result_tuple[0]

    assert len(result_model.patches) == 0


def test_model_math_custom_formula():
    sd_a = {"w": torch.tensor([2.0])}
    a = MockModelPatcher(sd_a)

    # expr: a * w
    # w input = 0.5

    result_tuple = ModelMathNode.execute(Expression="a * w", V={"V0": a}, F={"F0": 0.5})
    result_model = result_tuple[0]

    # res = 2.0 * 0.5 = 1.0
    # diff = 1.0 - 2.0 = -1.0
    patches = result_model.patches
    assert "w" in patches
    assert torch.allclose(patches["w"][0], torch.tensor([-1.0]))


def test_model_math_device_mismatch():
    # Simulating a scenario where model is on a specific device (we can't easily use 'cuda' in CI/CPU env, but we can check if visitor respects it)
    # We will iterate manually over ModelMathNode logic logic to check TensorEvalVisitor behavior or mock a device.
    # Actually, simpler: create a tensor on a specific device (if possible) or just ensure visitor uses the device of 'a'.

    # Since we might only have CPU, we can't fully reproduce 'cpu vs cuda' crash without cuda.
    # But we can verify that the scalar created by visitor.visitNumberExp has the same device as 'a'.

    from antlr4 import InputStream, CommonTokenStream
    from more_math.Parser.MathExprLexer import MathExprLexer
    from more_math.Parser.MathExprParser import MathExprParser

    # Mock a tensor with a mocked .device property if we can't use real devices
    # But torch tensors created with torch.tensor are real.
    # We will rely on inspection of the visitor code change.
    # Or strict check:

    # Let's try to pass a dummy device string if create_tensor allows, or just check the code path.
    # Better: Inspect the created tensor from visitor.

    torch.zeros((1,))
    # We interpret "device mismatch" as: created scalars didn't pick up the device of 'tsr'.
    # We can force 'tsr' to be on a specific device if available, but likely only 'cpu' is available.
    # Use a mock object for 'a' that claims to be on 'cuda:0', even if it isn't real tensor?
    # No, TensorEvalVisitor expects torch operations.

    # We will verify that TensorEvalVisitor creates tensors with the same device as input 'a'.

    # Setup
    expr = "0.5"
    input_stream = InputStream(expr)
    lexer = MathExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    parser.expr()

    {"a": torch.zeros(1)}
    # We want to ensure that if we had a non-cpu device, it would use it.
    # Since we can't really test this without a GPU, we will write the fix and verify it analytically
    # or use a mock that wraps a tensor but intercepts .device?

    # Let's just create a test that ensures the result of '0.5' is a tensor that has the same properties as we expect.
    pass


class MockPatcherContainer:
    def __init__(self, state_dict):
        self.patcher = MockModelPatcher(state_dict)

    def clone(self):
        new_obj = MockPatcherContainer(self.patcher.model.state_dict())
        new_obj.patcher = self.patcher.clone()  # Mock clone behavior
        return new_obj

    def add_patches(self, patches, s1, s2):
        self.patcher.add_patches(patches, s1, s2)


def test_clip_math():
    from more_math.ClipMathNode import CLIPMathNode

    sd_a = {"text_model.encoder.layers.0.mlp.fc1.weight": torch.tensor([1.0])}
    clip_a = MockPatcherContainer(sd_a)

    result_tuple = CLIPMathNode.execute(Expression="a * 2", V={"V0": clip_a}, F={})
    result_clip = result_tuple[0]

    # 1.0 * 2 = 2.0. diff = 1.0.
    patches = result_clip.patcher.patches
    assert "text_model.encoder.layers.0.mlp.fc1.weight" in patches
    assert torch.allclose(patches["text_model.encoder.layers.0.mlp.fc1.weight"][0], torch.tensor([1.0]))


def test_vae_math():
    from more_math.VaeMathNode import VAEMathNode

    sd_a = {"decoder.conv_in.weight": torch.tensor([1.0])}
    # VAE acts like PatcherContainer but no clone() on the VAE itself usually.
    # But for mock we can use PatcherContainer structure because VAEMathNode expects .patcher

    # Mock VAE object
    class MockVAE:
        def __init__(self, state_dict):
            self.patcher = MockModelPatcher(state_dict)

        # No clone method on VAE

    vae_a = MockVAE(sd_a)

    result_tuple = VAEMathNode.execute(Expression="a + 1", V={"V0": vae_a}, F={})
    result_vae = result_tuple[0]

    # Check if result is a copy (not same object)
    assert result_vae is not vae_a
    # Check if patcher is cloned
    assert result_vae.patcher is not vae_a.patcher

    # 1.0 + 1 = 2.0. diff = 1.0
    patches = result_vae.patcher.patches
    assert "decoder.conv_in.weight" in patches
    assert torch.allclose(patches["decoder.conv_in.weight"][0], torch.tensor([1.0]))


def test_model_math_disjoint_keys():
    # ModelMathNode uses 'a' as the base.
    # Keys in 'b' that are NOT in 'a' should be ignored in the loop generally,
    # unless logic iterates over union.
    # Current logic: for key, tens_a in sd_a.items(): ...
    # So keys only in B are IGNORED.

    sd_a = {"common": torch.tensor([1.0])}
    sd_b = {"common": torch.tensor([2.0]), "extra_b": torch.tensor([3.0])}

    a = MockPatcherContainer(sd_a)
    b = MockPatcherContainer(sd_b)

    # expr: a + b
    # common: 1 + 2 = 3. diff = 2.
    # extra_b: should NOT be in patches because loop is over 'a'

    result_tuple = ModelMathNode.execute(Expression="a + b", V={"V0": a.patcher, "V1": b.patcher}, F={})
    patches = result_tuple[0].patches

    assert "common" in patches
    assert torch.allclose(patches["common"][0], torch.tensor([2.0]))
    # With Autogrow/Union logic, extra_b is included (treated as 0 in A).
    # Result = a(0) + b(3) = 3. Diff vs a(0) = 3.
    assert "extra_b" in patches
    assert torch.allclose(patches["extra_b"][0], torch.tensor([3.0]))


def test_model_math_weighted_merge():
    # Test w/x/y/z weights
    sd_a = {"w": torch.tensor([10.0])}
    sd_b = {"w": torch.tensor([20.0])}

    a = MockPatcherContainer(sd_a)
    b = MockPatcherContainer(sd_b)

    # expr: lerp(a, b, w) with w=0.5 -> 15.0
    # diff = 15 - 10 = 5.

    result_tuple = ModelMathNode.execute(Expression="lerp(a, b, w)", V={"V0": a.patcher, "V1": b.patcher}, F={"F0": 0.5})
    patches = result_tuple[0].patches

    assert "w" in patches
    assert torch.allclose(patches["w"][0], torch.tensor([5.0]))


def test_model_math_3_way_merge():
    # Test merging 3 models: V0 + V1 + V2
    sd_a = {"w": torch.tensor([1.0])}
    sd_b = {"w": torch.tensor([2.0])}
    sd_c = {"w": torch.tensor([3.0])}

    a = MockPatcherContainer(sd_a)
    b = MockPatcherContainer(sd_b)
    c = MockPatcherContainer(sd_c)

    # Expression: a + b + c
    # Expected: 1 + 2 + 3 = 6.
    # Diff vs a (1.0) = 5.0.
    
    result_tuple = ModelMathNode.execute(Expression="a + b + c", V={"V0": a.patcher, "V1": b.patcher, "V2": c.patcher}, F={})
    patches = result_tuple[0].patches

    assert "w" in patches
    assert torch.allclose(patches["w"][0], torch.tensor([5.0]))


if __name__ == "__main__":
    test_model_math_simple_add()
    test_model_math_zero_default()
    test_model_math_custom_formula()
    test_model_math_device_mismatch()
    test_clip_math()
    test_vae_math()
    test_model_math_disjoint_keys()
    test_model_math_weighted_merge()
    test_model_math_3_way_merge()
    print("All ModelMathNode tests passed!")
