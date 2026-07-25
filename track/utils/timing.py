


def beats_to_seconds(beats: float, bpm: float) -> float:
    """Convert beats to seconds based on the given BPM (beats per minute).

    Args:
        beats (float): The number of beats to convert.
        bpm (float): The tempo in beats per minute.

    Returns:
        float: The equivalent time in seconds.
    """
    if bpm <= 0:
        raise ValueError("BPM must be greater than zero.")
    return (beats / bpm) * 60.0


def bars_to_seconds(bars: float, bpm: float, beats_per_bar: int = 4) -> float:
    """Convert bars to seconds based on the given BPM and beats per bar.

    Args:
        bars (float): The number of bars to convert.
        bpm (float): The tempo in beats per minute.
        beats_per_bar (int): The number of beats in one bar (default is 4).

    Returns:
        float: The equivalent time in seconds.
    """
    if bpm <= 0:
        raise ValueError("BPM must be greater than zero.")
    if beats_per_bar <= 0:
        raise ValueError("Beats per bar must be greater than zero.")
    total_beats = bars * beats_per_bar
    return beats_to_seconds(total_beats, bpm)


def steps_to_seconds(steps: float, bpm: float, steps_per_beat: int = 4) -> float:
    """Convert steps to seconds based on the given BPM and steps per beat.

    Args:
        steps (float): The number of steps to convert.
        bpm (float): The tempo in beats per minute.
        steps_per_beat (int): The number of steps in one beat (default is 4).

    Returns:
        float: The equivalent time in seconds.
    """
    if bpm <= 0:
        raise ValueError("BPM must be greater than zero.")
    if steps_per_beat <= 0:
        raise ValueError("Steps per beat must be greater than zero.")
    total_beats = steps / steps_per_beat
    return beats_to_seconds(total_beats, bpm)
