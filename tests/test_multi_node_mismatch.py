import torch
import pytest
from more_math.ImageMathNode import ImageMathNode
from more_math.AudioMathNode import AudioMathNode
from more_math.MaskMathNode import MaskMathNode

def test_image_mismatch_broadcast_a_longer():
    # a: 2 frames, b: 1 frame
    a = torch.ones((2, 64, 64, 3))
    b = torch.ones((1, 64, 64, 3)) * 0.5

    # a + b -> [1+0.5, 1+0.5]
    result, = ImageMathNode.execute("a + b", a, b=b, length_mismatch="tile")
    assert result.shape[0] == 2
    assert torch.allclose(result, torch.ones((2, 64, 64, 3)) * 1.5)

def test_image_mismatch_broadcast_b_longer():
    # a: 1 frame, b: 2 frames
    a = torch.ones((1, 64, 64, 3))
    b = torch.ones((2, 64, 64, 3)) * 0.5

    # a + b -> [1+0.5, 1+0.5] (a broadcasted to length 2)
    result, = ImageMathNode.execute("a + b", a, b=b, length_mismatch="tile")
    assert result.shape[0] == 2
    assert torch.allclose(result, torch.ones((2, 64, 64, 3)) * 1.5)

def test_image_mismatch_error():
    a = torch.ones((2, 64, 64, 3))
    b = torch.ones((1, 64, 64, 3)) * 0.5

    with pytest.raises(ValueError, match="Input 'b' has shape 1, expected 2 to match largest input."):
        ImageMathNode.execute("a + b", a, b=b, length_mismatch="error")

def test_image_mismatch_pad_b_longer():
    # a: 1 frame, b: 2 frames
    a = torch.ones((1, 64, 64, 3))
    b = torch.ones((2, 64, 64, 3)) * 0.5

    # a + b -> [1+0.5, 0+0.5] = [1.5, 0.5]
    result, = ImageMathNode.execute("a + b", a, b=b, length_mismatch="pad")
    assert result.shape[0] == 2
    assert torch.allclose(result[0], torch.ones((64, 64, 3)) * 1.5)
    assert torch.allclose(result[1], torch.ones((64, 64, 3)) * 0.5)

def test_audio_mismatch_error():
    a = torch.ones((1, 2, 100))
    b = torch.ones((1, 2, 50)) * 0.5
    with pytest.raises(ValueError, match=r"Input 'b' has shape \(1, 50\), expected \(1, 100\) to match largest input."):
        AudioMathNode.execute("a + b", {"waveform": a, "sample_rate": 44100}, b={"waveform": b, "sample_rate": 44100}, length_mismatch="error")

def test_mask_mismatch_error():
    a = torch.ones((2, 64, 64))
    b = torch.ones((1, 64, 64)) * 0.5
    with pytest.raises(ValueError, match="Input 'b' has shape 1, expected 2 to match largest input."):
        MaskMathNode.execute("a + b", a, b=b, length_mismatch="error")
