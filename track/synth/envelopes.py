import numpy as np
from numpy.typing import NDArray


def apply_fade(
    audio: NDArray[np.float32],
    fade_in_seconds: float,
    fade_out_seconds: float,
    sample_rate: int = 44100,
) -> NDArray[np.float32]:
    """Apply fade in and fade out to an audio signal."""
    faded_audio = audio.astype(np.float32, copy=True)

    fade_in_samples = int(fade_in_seconds * sample_rate)
    fade_out_samples = int(fade_out_seconds * sample_rate)

    if fade_in_samples < 0 or fade_out_samples < 0:
        raise ValueError("Fade durations must not be negative.")

    if fade_in_samples + fade_out_samples > faded_audio.size:
        raise ValueError("Combined fade duration is longer than the audio.")

    if fade_in_samples > 0:
        fade_in_envelope = np.linspace(
            0.0,
            1.0,
            fade_in_samples,
            endpoint=True,
            dtype=np.float32,
        )
        faded_audio[:fade_in_samples] *= fade_in_envelope

    if fade_out_samples > 0:
        fade_out_envelope = np.linspace(
            1.0,
            0.0,
            fade_out_samples,
            endpoint=True,
            dtype=np.float32,
        )
        faded_audio[-fade_out_samples:] *= fade_out_envelope

    return faded_audio
