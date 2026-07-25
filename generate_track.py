from track.synth.oscillators import triangle_wave
from track.utils.audio import save_wav

sample_rate = 44100
audio = triangle_wave(frequency=110, duration=2.0, sample_rate=sample_rate)

save_wav("output/triangle_test.wav", audio, sample_rate)
