from pathlib import Path

from track.synth.oscillators import saw_wave
import soundfile as sf
from numpy.typing import NDArray


def save_wav(
        path: str,
        audio: NDArray,
        sample_rate: int = 44100,
) -> None:
    """Save audio to a WAV file.

    Args:
        path (str): Path to save the WAV file.
        audio (NDArray): Audio data to save.
        sample_rate (int, optional): Sample rate of the audio. Defaults to 44100.
    """
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(path, audio, sample_rate)
