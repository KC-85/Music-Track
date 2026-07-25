import numpy as np
from numpy.typing import NDArray


def create_empty_track(
    duration_seconds: float,
    sample_rate: int = 44100,
) -> NDArray[np.float32]:
    """Create an empty track of the given duration and sample rate."""
    if duration_seconds <= 0:
        raise ValueError("Duration must be greater than zero.")
    if sample_rate <= 0:
        raise ValueError("Sample rate must be greater than zero.")

    num_samples = int(duration_seconds * sample_rate)
    return np.zeros(num_samples, dtype=np.float32)


def place_audio(
    track: NDArray[np.float32],
    audio: NDArray[np.float32],
    start_time_seconds: float,
    sample_rate: int = 44100,
) -> NDArray[np.float32]:
    """Place an audio clip into the track at the specified start time."""
    if start_time_seconds < 0:
        raise ValueError("Start time must not be negative.")
    if sample_rate <= 0:
        raise ValueError("Sample rate must be greater than zero.")

    start_sample = int(start_time_seconds * sample_rate)
    end_sample = start_sample + audio.size

    if end_sample > track.size:
        raise ValueError("Audio clip exceeds track length.")

    track[start_sample:end_sample] += audio.astype(np.float32, copy=False)
    return track
