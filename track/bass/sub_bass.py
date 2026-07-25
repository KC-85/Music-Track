import numpy as np
from numpy.typing import NDArray

from track.synth.envelopes import apply_fade
from track.synth.oscillators import triangle_wave


def sub_bass(
    frequency: float,
    duration: float,
    sample_rate: int = 44100,
    fade_in: float = 0.1,
    fade_out: float = 0.1,
) -> NDArray[np.float32]:
    """
    Generate a sub-bass sound using a triangle wave oscillator.

    Args:
        frequency (float): Frequency of the sub-bass in Hz.
        duration (float): Duration of the sound in seconds.
        sample_rate (int, optional): Sample rate in Hz. Defaults to 44100.
        fade_in (float, optional): Duration of the fade-in in seconds. Defaults to 0.1.
        fade_out (float, optional): Duration of the fade-out in seconds. Defaults to 0.1.

    Returns:
        NDArray[np.float32]: The generated sub-bass sound as a NumPy array.
    """
    # Generate the triangle wave for the specified duration and frequency
    samples = triangle_wave(frequency, duration, sample_rate)

    # Apply fade-in and fade-out to the generated sound
    samples = apply_fade(
        samples,
        fade_in_seconds=fade_in,
        fade_out_seconds=fade_out,
        sample_rate=sample_rate,
    )

    return samples.astype(np.float32)
