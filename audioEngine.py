import simpleaudio as sa

buffer = sa.WaveObject.from_wave_file("audio_samples/silence.wav")
play = buffer.play()


def player(path):
    global buffer
    global play
    buffer = sa.WaveObject.from_wave_file(path)

    if not play.is_playing():
        play = buffer.play()