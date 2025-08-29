from antlr4.error import ErrorListener
import torch

def getIndexTensorAlongDim(tensor, dim):
    shape = tensor.shape
    
    # Create values: shape (size of dim)
    values = torch.arange(shape[dim], dtype=torch.float32)

    # Reshape values to align with the target dimension
    view_shape = [1] * len(shape)
    view_shape[dim] = shape[dim]
    values = values.view(*view_shape)

    # Broadcast to full shape
    return values.expand(*shape)

def time_to_freq(audio_dict: torch.Tensor, n_fft: int = 512, hop_length: int = 256) -> torch.Tensor:
    waveform = audio_dict

    # Ensure the waveform is 3D with shape [batch, channels, time]
    if waveform.ndimension() != 3:
        raise ValueError(f"Expected 3D tensor, got {waveform.ndimension()}D tensor")

    # Create Hann window
    window = torch.hann_window(n_fft, device=waveform.device)

    # Initialize the output spectrogram
    spectrogram = torch.zeros(
        waveform.shape[0],
        waveform.shape[1],
        n_fft // 2 + 1,  # Frequency bins
        waveform.shape[2]//hop_length+1,  # Time steps
        dtype=torch.complex64,
        device=waveform.device
    )

    # Compute STFT on the last dimension for each value
    for b in range(waveform.shape[0]):
        for c in range(waveform.shape[1]):
            stft_result = torch.stft(
                waveform[b, c],
                n_fft=n_fft,
                hop_length=hop_length,
                win_length=n_fft,
                window=window,
                center=True,
                return_complex=True
            )
            spectrogram[b, c] = stft_result

    return spectrogram

def freq_to_time(freq_dict: torch.Tensor, n_fft: int = 512, hop_length: int = 256) -> torch.Tensor:
    spectrogram = freq_dict

    # Ensure the spectrogram is 3D with shape [batch, channels, freq, time]
    if spectrogram.ndimension() != 4:
        raise ValueError(f"Expected 4D tensor, got {spectrogram.ndimension()}D tensor")

    # Initialize the output waveform
    waveform = torch.zeros(
        spectrogram.shape[0],
        spectrogram.shape[1],
        spectrogram.shape[3] * hop_length,  # Total time samples
        dtype=torch.float32,
        device=spectrogram.device
    )

    # Create Hann window
    window = torch.hann_window(n_fft, device=spectrogram.device)

    # Compute iSTFT on the last dimension for each value
    for b in range(spectrogram.shape[0]):
        for c in range(spectrogram.shape[1]):
            istft_result = torch.istft(
                spectrogram[b, c],
                n_fft=n_fft,
                hop_length=hop_length,
                win_length=n_fft,
                window=window,
                center=True,
                normalized=False,
                length=spectrogram.shape[3] * hop_length
            )
            waveform[b, c] = istft_result

    return waveform
class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError(f"Syntax error in AudioExpr at line {line}, col {column}: {msg}")
