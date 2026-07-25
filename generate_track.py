from track.bass.sub_bass import sub_bass
from track.utils.audio import save_wav

sample_rate = 44100
audio = sub_bass(
    frequency=55,
    duration=2.0,
    sample_rate=sample_rate,
    fade_in=0.01,
    fade_out=0.05,
)

save_wav("output/sub_bass_test.wav", audio, sample_rate)
