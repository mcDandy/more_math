import torch
from comfy_api.latest import io

windows = {"bartlett": torch.bartlett_window, "blackman": torch.blackman_window, "hamming": torch.hamming_window, "hann": torch.hann_window, "kaiser": torch.kaiser_window}


class SpectrogramToAudio(io.ComfyNode):
    """
    Converts an Image spectrogram back to Audio.
    Red is real part and blue is imaginary. Green is ignored.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ImageSpectrogramToAudio",
            category="More math/converters",
            display_name="Spectrogram -> Audio",
            inputs=[
                io.Image.Input(id="image", tooltip="Input spectrogram image (R=Real, G=Magnitude, B=Imaginary)"),
                io.Int.Input(id="channel_count", default=1, min=1, tooltip="Number of audio channels"),
                io.Int.Input(id="sample_rate", default=44100, min=1, tooltip="Sample rate of the output audio"),
                io.Int.Input(id="window_length", default=1024, min=16, tooltip="Window length in samples"),
                io.Int.Input(id="hop_length", default=256, min=1, tooltip="Stride of the window (hop length) in samples"),
                io.Combo.Input(id="window_type", default="hann", options=list(windows.keys()), tooltip="Type of window function to apply"),
            ],
            outputs=[
                io.Audio.Output(id="audio", tooltip="Output audio"),
            ],
        )

    @classmethod
    def validate_inputs(cls, image, channel_count, window_length, **kwargs):
        if channel_count <= 0:
            return "channel_count must be greater than zero."
        _, height, _, _ = image.shape
        if height % channel_count != 0:
            return f"Spectrogram height ({height}) must be divisible by channel_count ({channel_count})."
        bucket_count = height // channel_count
        if bucket_count < 2:
            return "Each audio channel must have at least 2 frequency bins."
        n_fft = (bucket_count - 1) * 2
        if window_length > n_fft:
            return f"window_length ({window_length}) must be no greater than the FFT size ({n_fft})."
        return True

    @classmethod
    def execute(cls, image, channel_count, sample_rate, window_length, hop_length, window_type):
        B, H, W, _ = image.shape
        if channel_count <= 0:
            raise ValueError("channel_count must be greater than zero.")
        if H % channel_count != 0:
            raise ValueError(f"Spectrogram height ({H}) must be divisible by channel_count ({channel_count}).")
        bucket_count = H // channel_count
        if bucket_count < 2:
            raise ValueError("Each audio channel must have at least 2 frequency bins.")
        n_fft = (bucket_count - 1) * 2
        if window_length > n_fft:
            raise ValueError(f"window_length ({window_length}) must be no greater than the FFT size ({n_fft}).")
        real = image[..., 0].reshape(B * channel_count, bucket_count, W)
        imag = image[..., 2].reshape(B * channel_count, bucket_count, W)
        stft_complex = torch.complex(real, imag)
        window = windows[window_type](window_length, device=image.device)
        waveform = torch.istft(
            stft_complex,
            n_fft=n_fft,
            hop_length=hop_length,
            win_length=window_length,
            window=window,
            center=True,
            normalized=False,
            onesided=True,
        )

        waveform = waveform.reshape(B, channel_count, -1)
        return ({"waveform": waveform, "sample_rate": sample_rate},)
