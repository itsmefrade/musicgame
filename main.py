# Example file showing a circle moving on screen
import pygame
import pygame.mixer
import mido


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    try:
            pygame.mixer.init()
    except:
            print("Failed to initialize sound mixer")
            
    
    NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    import librosa
    import numpy as np

    # Müzik dosyasını yükle
    filename = "eminem.wav"
    y, sr = librosa.load(filename)

    # Spektral özellikleri al
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)

    # Notalara dönüştürme için bir nota haritası oluştur
    note_map = {
        0: "C",
        1: "C#",
        2: "D",
        3: "D#",
        4: "E",
        5: "F",
        6: "F#",
        7: "G",
        8: "G#",
        9: "A",
        10: "A#",
        11: "B"
        # ... diğer notaları ekleyin
    }

    # Basit notaları saklamak için bir liste oluştur
    simple_notes = []
    timestamps = []

    # Spektral özellikleri dolaşarak notalara dönüştür ve zamanları kaydet
    hop_length = 512  # Örnekleme aralığı
    for i, frame in enumerate(chroma.T):
        note_index = np.argmax(frame)  # En yüksek enerjili nota
        simple_notes.append(note_map[note_index])
        
        # Zamanı hesapla
        timestamp = librosa.frames_to_time(i, sr=sr, hop_length=hop_length)
        timestamps.append(timestamp)

    # Basit notaları ve zamanları yazdır veya dosyaya kaydet
    output_filename = "output_with_timestamps.txt"
    with open(output_filename, "w") as f:
        for timestamp, note in zip(timestamps, simple_notes):
            f.write(f"{timestamp:.2f} - {note}\n")

    print("Basit notalar ve zamanlar dosyaya kaydedildi:", output_filename)

    
    import sounddevice as sd

    # C notasının frekansı
    frequency = 261.63  # C4 notasının frekansı (Hz)

    # Süre ve örnekleme hızı
    duration = 1.39  # Çalma süresi (saniye)
    sample_rate = 22100  # Örnekleme hızı

    # Ses oluşturma
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    signal = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Sesi çal
    sd.play(signal, sample_rate)
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 277.183 * np.linspace(0, 0.3, int(sample_rate * 0.3), False)), sample_rate) # C# note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 466.164 * np.linspace(0, 0.2, int(sample_rate * 0.2), False)), sample_rate) # A# note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 329.628 * np.linspace(0, 0.2, int(sample_rate * 0.2), False)), sample_rate) # E note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 493.883 * np.linspace(0, 0.42, int(sample_rate * 0.42), False)), sample_rate) # B note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 391.995 * np.linspace(0, 0.93, int(sample_rate * 0.93), False)), sample_rate) # G note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 440 * np.linspace(0, 0.18, int(sample_rate * 0.18), False)), sample_rate) # A note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 391.995 * np.linspace(0, 0.32, int(sample_rate * 0.32), False)), sample_rate) # G note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 369.994 * np.linspace(0, 1.44, int(sample_rate * 1.44), False)), sample_rate) # F# note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 440 * np.linspace(0, 0.32, int(sample_rate * 0.32), False)), sample_rate) # A note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 293.665 * np.linspace(0, 0.35, int(sample_rate * 0.35), False)), sample_rate) # D note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 293.665 * np.linspace(0, 0.35, int(sample_rate * 0.35), False)), sample_rate) # D note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 493.883 * np.linspace(0, 0.11, int(sample_rate * 0.11), False)), sample_rate) # B note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 329.628 * np.linspace(0, 2.02, int(sample_rate * 2.02), False)), sample_rate) # E note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 440 * np.linspace(0, 0.3, int(sample_rate * 0.3), False)), sample_rate) # A note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * frequency * np.linspace(0, 1.67, int(sample_rate * 1.67), False)), sample_rate) #c note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 440 * np.linspace(0, 0.75, int(sample_rate * 0.75), False)), sample_rate) # A note
    sd.wait() 
    sd.play(0.5 * np.sin(2 * np.pi * 293.665 * np.linspace(0, 0.33, int(sample_rate * 0.33), False)), sample_rate) # D note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 391.995 * np.linspace(0, 1.74, int(sample_rate * 1.74), False)), sample_rate) # G note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 493.883 * np.linspace(0, 0.65, int(sample_rate * 0.65), False)), sample_rate) # B note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 329.628 * np.linspace(0, 0.7, int(sample_rate * 0.7), False)), sample_rate) # E note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 493.883 * np.linspace(0, 0.14, int(sample_rate * 0.14), False)), sample_rate) # B note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 440 * np.linspace(0, 0.18, int(sample_rate * 0.18), False)), sample_rate) # A note
    sd.wait() 
    sd.play(0.5 * np.sin(2 * np.pi * 391.995 * np.linspace(0, 0.27, int(sample_rate * 0.27), False)), sample_rate) # G note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 369.994 * np.linspace(0, 0.53, int(sample_rate * 0.53), False)), sample_rate) # F# note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * frequency * np.linspace(0, 0.55, int(sample_rate * 0.55), False)), sample_rate) #c note
    sd.wait()
    sd.play(0.5 * np.sin(2 * np.pi * 369.994 * np.linspace(0, 0.7, int(sample_rate * 0.53), False)), sample_rate) # F# note
    sd.wait()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt 
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()