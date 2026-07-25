from track.synth.oscillators import saw_wave
from track.utils.audio import save_wav

sample_rate = 44100
audio = saw_wave(frequency=110, duration=2.0, sample_rate=sample_rate)

save_wav("output/saw_test.wav", audio, sample_rate)
