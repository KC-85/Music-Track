from track.arrangement.sequencer import create_empty_track, place_audio
from track.bass.sub_bass import sub_bass
from track.utils.audio import save_wav
from track.utils.timing import bars_to_seconds, steps_to_seconds

SAMPLE_RATE = 44100
BPM = 174
STEPS_PER_BEAT = 4

BASS_PATTERN = [
    (0, 2, 55.00),
    (4, 2, 55.00),
    (7, 1, 65.41),
    (10, 2, 49.00),
    (14, 2, 55.00),
]

track_duration = bars_to_seconds(1, BPM)
track = create_empty_track(track_duration, SAMPLE_RATE)

for start_step, duration_steps, frequency in BASS_PATTERN:
    start_time = steps_to_seconds(start_step, BPM, STEPS_PER_BEAT)
    note_duration = steps_to_seconds(duration_steps, BPM, STEPS_PER_BEAT)
    note = sub_bass(
        frequency=frequency,
        duration=note_duration,
        sample_rate=SAMPLE_RATE,
        fade_in=0.01,
        fade_out=0.02,
    )

    track = place_audio(track, note, start_time, SAMPLE_RATE)

track *= 0.6

save_wav("output/sub_bass_loop.wav", track, SAMPLE_RATE)
