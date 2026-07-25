import numpy as np
from numpy.typing import NDArray
from scipy import signal


def sine_wave(
    frequency: float,
    duration: float,
    sample_rate: int = 44100,
) -> NDArray[np.float32]:
    """
    Generate a sine wave.

    Args:
        frequency (float): Frequency of the sine wave in Hz.
        duration (float): Duration of the sine wave in seconds.
        sample_rate (int, optional): Sample rate in Hz. Defaults to 44100.

    Returns:
        NDArray[np.float32]: Array containing the generated sine wave.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t).astype(np.float32)


def saw_wave(
    frequency: float,
    duration: float,
    sample_rate: int = 44100,
) -> NDArray[np.float32]:
    """
    Generate a sawtooth wave.

    Args:
        frequency (float): Frequency of the sawtooth wave in Hz.
        duration (float): Duration of the sawtooth wave in seconds.
        sample_rate (int, optional): Sample rate in Hz. Defaults to 44100.

    Returns:
        NDArray[np.float32]: Array containing the generated sawtooth wave.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return signal.sawtooth(2 * np.pi * frequency * t).astype(np.float32)


def square_wave(
    frequency: float,
    duration: float,
    sample_rate: int = 44100,
) -> NDArray[np.float32]:
    """
    Generate a square wave.

    Args:
        frequency (float): Frequency of the square wave in Hz.
        duration (float): Duration of the square wave in seconds.
        sample_rate (int, optional): Sample rate in Hz. Defaults to 44100.

    Returns:
        NDArray[np.float32]: Array containing the generated square wave.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return signal.square(2 * np.pi * frequency * t).astype(np.float32)


def triangle_wave(
    frequency: float,
    duration: float,
    sample_rate: int = 44100,
) -> NDArray[np.float32]:
    """
    Generate a triangle wave.

    Args:
        frequency (float): Frequency of the triangle wave in Hz.
        duration (float): Duration of the triangle wave in seconds.
        sample_rate (int, optional): Sample rate in Hz. Defaults to 44100.

    Returns:
        NDArray[np.float32]: Array containing the generated triangle wave.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return signal.sawtooth(2 * np.pi * frequency * t, width=0.5).astype(np.float32)
