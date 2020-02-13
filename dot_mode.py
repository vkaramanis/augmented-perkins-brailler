from audioEngine import player


def buttons(GPIO, level, tick):

    sam = ""

    if GPIO == 18:
        pass
    elif GPIO == 27:
        sam = "audio_samples/dot_mode/dot_three.wav"
    elif GPIO == 22:
        sam = "audio_samples/dot_mode/dot_two.wav"
    elif GPIO == 17:
        sam = "audio_samples/dot_mode/dot_one.wav"
    elif GPIO == 25:
        sam = "audio_samples/spacebar.wav"
    elif GPIO == 26:
        sam = "audio_samples/dot_mode/dot_four.wav"
    elif GPIO == 12:
        sam = "audio_samples/dot_mode/dot_five.wav"
    elif GPIO == 13:
        sam = "audio_samples/dot_mode/dot_six.wav"
    elif GPIO == 16:
        pass

    if sam != "":
        player(sam)