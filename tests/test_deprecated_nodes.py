import torch
import sys
import os

# Ensure test runner usage (Visual Studio) can import the package regardless of working dir.
_here = os.path.abspath(os.path.dirname(__file__))
_project_root = os.path.abspath(os.path.join(_here, os.pardir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# Add ComfyUI root to path to find 'comfy' and 'comfy_api' packages
_comfy_root = os.path.abspath(os.path.join(_here, "../../.."))
if _comfy_root not in sys.path:
    sys.path.insert(0, _comfy_root)

from more_math.deprecated.ImageMathNode import ImageMathNodeOLD
from more_math.deprecated.LatentMathNode import LatentMathNodeOLD
from more_math.deprecated.MaskMathNode import MaskMathNodeOLD
from more_math.deprecated.AudioMathNode import AudioMathNodeOLD
from more_math.deprecated.ModelMathNode import ModelMathNodeOLD
from more_math.deprecated.VaeMathNode import VAEMathNodeOLD
from more_math.deprecated.ClipMathNode import CLIPMathNodeOLD
import comfy_api

# Mock objects for Model/VAE/CLIP tests
class MockModelPatcher:
    def __init__(self, state_dict):
        self.model = comfy_api.Model()
        self.model.state_dict = lambda: state_dict
        self.patches = {}

    def clone(self):
        new_patcher = MockModelPatcher(self.model.state_dict())
        return new_patcher

    def add_patches(self, patches, strength1, strength2):
        self.patches.update(patches)

class MockPatcherContainer:
    def __init__(self, state_dict):
        self.patcher = MockModelPatcher(state_dict)

    def clone(self):
        new_obj = MockPatcherContainer(self.patcher.model.state_dict())
        new_obj.patcher = self.patcher.clone()
        return new_obj

    def add_patches(self, patches, s1, s2):
        self.patcher.add_patches(patches, s1, s2)

class MockVAE(MockPatcherContainer):
    pass # VAE structure is similar enough for simple patching test

def test_deprecated_image_math():
    t1 = torch.zeros((1, 32, 32, 3))
    t2 = torch.full((1, 32, 32, 3), 1.0)
    # OLD signature: Image, a, b=...
    res = ImageMathNodeOLD.execute(Image="a+b", a=t1, b=t2)[0]
    assert torch.allclose(res, torch.ones_like(res))

def test_deprecated_latent_math():
    l1 = {"samples": torch.zeros((1, 4, 32, 32))}
    l2 = {"samples": torch.full((1, 4, 32, 32), 1.0)}
    # OLD signature: Latent, a, b=...
    res = LatentMathNodeOLD.execute(Latent="a+b", a=l1, b=l2)[0]["samples"]
    assert torch.allclose(res, torch.ones_like(res))

def test_deprecated_mask_math():
    m1 = torch.zeros((1, 32, 32))
    m2 = torch.full((1, 32, 32), 1.0)
    # OLD signature: Mask, a, b=...
    res = MaskMathNodeOLD.execute(Mask="a+b", a=m1, b=m2)[0]
    assert torch.allclose(res, torch.ones_like(res))

def test_deprecated_audio_math():
    a1 = {"waveform": torch.zeros((1, 1, 100)), "sample_rate": 44100}
    a2 = {"waveform": torch.full((1, 1, 100), 1.0), "sample_rate": 44100}
    # OLD signature: Audio, a, b=...
    res = AudioMathNodeOLD.execute(Audio="a+b", a=a1, b=a2)[0]["waveform"]
    assert torch.allclose(res, torch.ones_like(res))

def test_deprecated_model_math():
    sd_a = {"w": torch.tensor([1.0])}
    sd_b = {"w": torch.tensor([2.0])}
    patcher_a = MockModelPatcher(sd_a)
    patcher_b = MockModelPatcher(sd_b)

    # OLD signature: Model, a, b=...
    res = ModelMathNodeOLD.execute(Model="a+b", a=patcher_a, b=patcher_b)[0]
    print(f"DEBUG: res.patches keys: {res.patches.keys()}")
    if "w" in res.patches:
        print(f"DEBUG: res.patches['w']: {res.patches['w']}")
    # a+b = 1+2 = 3. diff = 3-1 = 2.
    assert "w" in res.patches
    assert torch.allclose(res.patches["w"][0], torch.tensor([2.0]))

def test_deprecated_vae_math():
    sd_a = {"w": torch.tensor([1.0])}
    vae_a = MockVAE(sd_a) # VAE wrapper

    # OLD signature: Model, a, b=... (Note: VAE node param name was Model in old schema too)
    res = VAEMathNodeOLD.execute(Model="a+1", a=vae_a)[0]
    # 1+1=2. diff=1.
    assert "w" in res.patcher.patches
    assert torch.allclose(res.patcher.patches["w"][0], torch.tensor([1.0]))

def test_deprecated_clip_math():
    sd_a = {"w": torch.tensor([1.0])}
    clip_a = MockPatcherContainer(sd_a)

    # OLD signature: Model, a, b=...
    res = CLIPMathNodeOLD.execute(Model="a*2", a=clip_a)[0]
    # 1*2=2. diff=1.
    assert "w" in res.patcher.patches
    assert torch.allclose(res.patcher.patches["w"][0], torch.tensor([1.0]))
