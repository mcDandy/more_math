import pytest
import torch

from more_math.AudioToSpectrogramNode import AudioToSpectrogram
from more_math.BatchLoraNode import BatchLoraNode
from more_math.SpectrogramToAudioNode import SpectrogramToAudio


def test_spectrogram_validation_rejects_window_longer_than_fft():
    result = AudioToSpectrogram.validate_inputs(window_length=1024, bucket_count=2)
    assert result == "window_length (1024) must be no greater than the FFT size (2)."


def test_spectrogram_validation_accepts_window_within_fft():
    assert AudioToSpectrogram.validate_inputs(window_length=1024, bucket_count=513) is True


def test_spectrogram_execute_reports_invalid_window():
    audio = {"waveform": torch.zeros(1, 1, 2048), "sample_rate": 44100}
    with pytest.raises(ValueError, match="window_length .* must be no greater"):
        AudioToSpectrogram.execute(audio, 1024, 256, 2, "hann")


def test_spectrogram_to_audio_validation_checks_frequency_bins_and_channels():
    image = torch.zeros(1, 1026, 32, 3)
    assert SpectrogramToAudio.validate_inputs(image, 2, 1024) is True
    assert "divisible by channel_count" in SpectrogramToAudio.validate_inputs(image, 4, 1024)
    assert "FFT size (2)" in SpectrogramToAudio.validate_inputs(torch.zeros(1, 4, 32, 3), 2, 1024)


def test_spectrogram_to_audio_requires_two_bins_per_channel():
    image = torch.zeros(1, 2, 32, 3)
    assert "at least 2 frequency bins" in SpectrogramToAudio.validate_inputs(image, 2, 1)


def test_spectrogram_to_audio_execute_reports_incompatible_channels():
    image = torch.zeros(1, 5, 32, 3)
    with pytest.raises(ValueError, match="must be divisible by channel_count"):
        SpectrogramToAudio.execute(image, 2, 44100, 2, 1, "hann")


def test_batch_lora_rejects_empty_model_strengths(monkeypatch):
    monkeypatch.setattr(
        "more_math.BatchLoraNode.folder_paths.get_filename_list",
        lambda _: ["style\\adapter.safetensors"],
    )

    def parse_strengths(expression, stack, lora_list, lora_count, base_model):
        return [], stack

    monkeypatch.setattr(BatchLoraNode, "_parse_strengths", staticmethod(parse_strengths))

    with pytest.raises(ValueError, match="model_strength expression must produce at least one value"):
        BatchLoraNode.execute(
            model=object(),
            clip=object(),
            folder="style",
            add_no_lora=False,
            model_strength="[]",
            clip_strength="[1]",
        )
