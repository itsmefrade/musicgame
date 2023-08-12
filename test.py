import librosa
import numpy as np
from music21 import stream, note, meter
import sounddevice as sd
import math 
# Ses dosyasını yükle
filename = 'eminem.wav'
y, sr = librosa.load(filename)

# Pitch ve süreleri tespit et
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
mean_pitches = np.mean(pitches, axis=0)
notes = librosa.hz_to_midi(mean_pitches)

# Notaları yazdır
for note in notes:
    if note > 0:
        print(f"MIDI Note: {note:.2f}")

# Notaları notasyona dönüştürme ve kaydetme adımları burada devam edebilir.


def play_sound(frequency, duration, amplitude=1.0, sample_rate=44100):
    # Zaman dizisi oluştur
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Sinüs dalgası oluştur
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Ses çal
    sd.play(wave, sample_rate)
    sd.wait()

# Frekans ve süre belirle
duration = 2.0   # Saniye

# Ses çal
for i in  notes:
    if math.floor(i) > 1:
        print(i)
        frequency = float(i)
        play_sound(frequency, duration)
