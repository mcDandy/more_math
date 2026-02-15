import torch
from more_math.ImageMathNode import ImageMathNode
from more_math.AudioMathNode import AudioMathNode
from more_math.LatentMathNode import LatentMathNode
from more_math.helper_functions import normalize_to_common_shape

def test_normalize_broadcast_unit_dim():
    # a: (1, 1, 4, 4), b: (1, 1, 1, 1)
    a = torch.ones((1, 1, 4, 4))
    b = torch.ones((1, 1, 1, 1)) * 0.5

    # Broadcast b to match a
    an, bn = normalize_to_common_shape(a, b, mode="tile")

    assert bn.shape == (1, 1, 4, 4)
    assert torch.all(bn == 0.5)

def test_normalize_pad_unit_dim():
    # a: (1, 1, 4, 4), b: (1, 1, 1, 1)
    a = torch.ones((1, 1, 4, 4))
    b = torch.ones((1, 1, 1, 1)) * 0.5

    # Pad b to match a (should be top-left)
    an, bn = normalize_to_common_shape(a, b, mode="pad")

    assert bn.shape == (1, 1, 4, 4)
    assert bn[0, 0, 0, 0] == 0.5
    assert bn[0, 0, 0, 1] == 0.0

def test_image_node_broadcasting_pixel():
    # Single red pixel (1, 1, 1, 3) broadcast into (1, 512, 512, 3)
    a = torch.zeros((1, 512, 512, 3))
    b = torch.tensor([[[[1.0, 0.0, 0.0]]]])

    # Broadcast mode: fills entire image with red
    result_list, stack = ImageMathNode.execute(V={"V0": a, "V1": b}, F={}, Expression="a + b", length_mismatch="tile")
    result = result_list[0]
    assert result.shape == (1, 512, 512, 3)
    assert result[0,255,255,0] == 1.0
    assert torch.allclose(result, torch.tensor([1.0, 0.0, 0.0]).view(1, 1, 1, 3))

def test_image_node_broadcasting_stretch():
    # Stretching a 1-wide column (red) across a 512-wide zero field
    # a: (1, 512, 512, 3), b: (1, 512, 1, 3)
    a = torch.zeros((1, 512, 512, 3))
    b = torch.ones((1, 512, 1, 3)) * torch.tensor([1.0, 0.0, 0.0])

    result_list, stack = ImageMathNode.execute(V={"V0": a, "V1": b}, F={}, Expression="a + b", length_mismatch="tile")
    result = result_list[0]
    assert result.shape == (1, 512, 512, 3)
    # Check middle pixel to ensure it broadcasted horizontally
    assert torch.allclose(result[0, 256, 256, :], torch.tensor([1.0, 0.0, 0.0]))

def test_audio_node_broadcasting_channels():
    # a: stereo (1, 2, 100), b: mono (1, 1, 100)
    a_bg = torch.zeros((1, 2, 100))
    b_fg = torch.ones((1, 1, 100)) * 0.5

    a = {"waveform": a_bg, "sample_rate": 44100}
    b = {"waveform": b_fg, "sample_rate": 44100}

    # Executing AudioMathNode with broadcast should make both channels 0.5
    result_list, stack = AudioMathNode.execute(V={"V0": a, "V1": b}, F={}, Expression="a + b", length_mismatch="tile")
    result_dict = result_list[0]
    result = result_dict["waveform"]
    assert result.shape == (1, 2, 100)
    assert torch.all(result == 0.5)

def test_latent_node_broadcasting_spatial():
    # a: (1, 4, 64, 64), b: (1, 4, 1, 1)
    a_in = {"samples": torch.zeros((1, 4, 64, 64))}
    b_in = {"samples": torch.ones((1, 4, 1, 1)) * 0.7}

    result_list, stack = LatentMathNode.execute(V={"V0": a_in, "V1": b_in}, F={}, Expression="a + b", length_mismatch="tile", batching=0)
    result_dict = result_list[0]
    result = result_dict["samples"]
    assert result.shape == (1, 4, 64, 64)
    assert torch.all(result == 0.7)

if __name__ == "__main__":
    test_normalize_broadcast_unit_dim()
    test_normalize_pad_unit_dim()
    test_image_node_broadcasting_pixel()
    test_image_node_broadcasting_stretch()
    test_audio_node_broadcasting_channels()
    test_latent_node_broadcasting_spatial()
    print("All comprehensive broadcasting tests passed!")
