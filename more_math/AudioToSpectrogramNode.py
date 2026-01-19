from comfy_api.latest import io
import torch

windows = {"bartlett": torch.bartlett_window, "blackman": torch.blackman_window, "hamming": torch.hamming_window, "hann": torch.hann_window, "kaiser": torch.kaiser_window}


class AudioToSpectrogram(io.ComfyNode):
    """
    Converts Audio to an Image spectrogram.
    Red = Real, Green = logarithm of value (just so it looks good), Blue = Imaginary.
    Each audio channel is stacked vertically.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_AudioToImageSpectrogram",
            category="More math",
            display_name="Audio -> Spectrogram",
            inputs=[
                io.Audio.Input(id="audio", tooltip="Input audio"),
                io.Int.Input(id="window_length", default=1024, min=16, max=4096, tooltip="Window length in samples"),
                io.Int.Input(id="hop_length", default=256, min=1, max=4096, tooltip="Stride of the window (hop length) in samples"),
                io.Int.Input(
                    id="bucket_count", default=513, min=2, max=4096, tooltip="Number of frequency buckets (determines resolution)"
                ),
                io.Combo.Input(id="window_type", default="hann", options=list(windows.keys()), tooltip="Type of window function to apply"),
            ],
            outputs=[
                io.Image.Output(id="image"),
                io.Int.Output(id="channel_count", display_name="Channel count", tooltip="Number of channels in the output image"),
                io.Int.Output(id="sample_rate", display_name="Sample rate", tooltip="Sample rate of the input audio"),
            ],
        )

    @classmethod
    def execute(cls, audio, window_length, hop_length, bucket_count, window_type):
        waveform = audio["waveform"]
        sample_rate = audio["sample_rate"]
        B, C, S = waveform.shape
        n_fft = (bucket_count - 1) * 2
        flat_waveform = waveform.reshape(B * C, S)
        window = windows[window_type](window_length, device=waveform.device)

        stft_out = torch.stft(
            flat_waveform,
            n_fft=n_fft,
            hop_length=hop_length,
            win_length=window_length,
            window=window,
            center=True,
            pad_mode="reflect",
            normalized=False,
            onesided=True,
            return_complex=True,
        )

        F, T = stft_out.shape[1], stft_out.shape[2]
        stft_out = stft_out.reshape(B, C, F, T).reshape(B, C * F, T)
        image = torch.stack([stft_out.real, torch.log1p(torch.abs(stft_out)), stft_out.imag], dim=-1)
        print(image.type())
        return (image, C, sample_rate)
