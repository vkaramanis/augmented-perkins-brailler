from audioEngine import player

buttons = [0, 0, 0, 0, 0, 0]
gate = 0
number_mode = False

braille_dict = {
    # Symbols
    "NUMBER": [1, 0, 0, 1, 1, 1],
    "LETTER": [0, 0, 0, 0, 1, 1],
    "SPACE":  [0, 0, 0, 0, 0, 0],
    # Letters
    "A": [0, 0, 1, 0, 0, 0],
    "B": [0, 1, 1, 0, 0, 0],
    "C": [0, 0, 1, 1, 0, 0],
    "D": [0, 0, 1, 1, 1, 0],
    "E": [0, 0, 1, 0, 1, 0],
    "F": [0, 1, 1, 1, 0, 0],
    "G": [0, 1, 1, 1, 1, 0],
    "H": [0, 1, 1, 0, 1, 0],
    "I": [0, 1, 0, 1, 0, 0],
    "J": [0, 1, 0, 1, 1, 0],
    "K": [1, 0, 1, 0, 0, 0],
    "L": [1, 1, 1, 0, 0, 0],
    "M": [1, 0, 1, 1, 0, 0],
    "N": [1, 0, 1, 1, 1, 0],
    "O": [1, 0, 1, 0, 1, 0],
    "P": [1, 1, 1, 1, 0, 0],
    "Q": [1, 1, 1, 1, 1, 0],
    "R": [1, 1, 1, 0, 1, 0],
    "S": [1, 1, 0, 1, 0, 0],
    "T": [1, 1, 0, 1, 1, 0],
    "U": [1, 0, 1, 0, 0, 1],
    "V": [1, 1, 1, 0, 0, 1],
    "W": [0, 1, 0, 1, 1, 1],
    "X": [1, 0, 1, 1, 0, 1],
    "Y": [1, 0, 1, 1, 1, 1],
    "Z": [1, 0, 1, 0, 1, 1],

}


def mapping(button):
    global number_mode
    path = ""

    # NUMBERS
    if number_mode:
        if button == braille_dict["LETTER"]:  # go back
            number_mode = False
            path = "audio_samples/letter_mode/letter.wav"
        elif button == braille_dict["A"]:  # say one
            path = "audio_samples/letter_mode/numbers/01.wav"
        elif button == braille_dict["B"]:  # say two
            path = "audio_samples/letter_mode/numbers/02.wav"
        elif button == braille_dict["C"]:  # say three
            path = "audio_samples/letter_mode/numbers/03.wav"
        elif button == braille_dict["D"]:  # say four
            path = "audio_samples/letter_mode/numbers/04.wav"
        elif button == braille_dict["E"]:  # say five
            path = "audio_samples/letter_mode/numbers/05.wav"
        elif button == braille_dict["F"]:  # say six
            path = "audio_samples/letter_mode/numbers/06.wav"
        elif button == braille_dict["G"]:  # say seven
            path = "audio_samples/letter_mode/numbers/07.wav"
        elif button == braille_dict["H"]:  # say eight
            path = "audio_samples/letter_mode/numbers/08.wav"
        elif button == braille_dict["I"]:  # say nine
            path = "audio_samples/letter_mode/numbers/09.wav"
        elif button == braille_dict["J"]:  # say zero
            path = "audio_samples/letter_mode/numbers/00.wav"
        elif button == braille_dict["SPACE"]:
            path = "audio_samples/spacebar.wav"
            number_mode = False

    # LETTERS
    else:
        if button == braille_dict["NUMBER"]:
            number_mode = True
            path = "audio_samples/letter_mode/number.wav"
        elif button == braille_dict["A"]:  # say A
            path = "audio_samples/letter_mode/letters/a.wav"
        elif button == braille_dict["B"]:  # say B
            path = "audio_samples/letter_mode/letters/b.wav"
        elif button == braille_dict["C"]:  # say C
            path = "audio_samples/letter_mode/letters/c.wav"
        elif button == braille_dict["D"]:  # say D
            path = "audio_samples/letter_mode/letters/d.wav"
        elif button == braille_dict["E"]:  # say E
            path = "audio_samples/letter_mode/letters/e.wav"
        elif button == braille_dict["F"]:  # say F
            path = "audio_samples/letter_mode/letters/f.wav"
        elif button == braille_dict["G"]:  # say G
            path = "audio_samples/letter_mode/letters/g.wav"
        elif button == braille_dict["H"]:  # say H
            path = "audio_samples/letter_mode/letters/h.wav"
        elif button == braille_dict["I"]:  # say I
            path = "audio_samples/letter_mode/letters/i.wav"
        elif button == braille_dict["J"]:  # say J
            path = "audio_samples/letter_mode/letters/j.wav"
        elif button == braille_dict["K"]:  # say K
            path = "audio_samples/letter_mode/letters/k.wav"
        elif button == braille_dict["L"]:  # say L
            path = "audio_samples/letter_mode/letters/l.wav"
        elif button == braille_dict["M"]:  # say M
            path = "audio_samples/letter_mode/letters/m.wav"
        elif button == braille_dict["N"]:  # say N
            path = "audio_samples/letter_mode/letters/n.wav"
        elif button == braille_dict["O"]:  # say O
            path = "audio_samples/letter_mode/letters/o.wav"
        elif button == braille_dict["P"]:  # say P
            path = "audio_samples/letter_mode/letters/p.wav"
        elif button == braille_dict["Q"]:  # say Q
            path = "audio_samples/letter_mode/letters/q.wav"
        elif button == braille_dict["R"]:  # say R
            path = "audio_samples/letter_mode/letters/r.wav"
        elif button == braille_dict["S"]:  # say S
            path = "audio_samples/letter_mode/letters/s.wav"
        elif button == braille_dict["T"]:  # say T
            path = "audio_samples/letter_mode/letters/t.wav"
        elif button == braille_dict["U"]:  # say U
            path = "audio_samples/letter_mode/letters/u.wav"
        elif button == braille_dict["V"]:  # say V
            path = "audio_samples/letter_mode/letters/v.wav"
        elif button == braille_dict["W"]:  # say W
            path = "audio_samples/letter_mode/letters/w.wav"
        elif button == braille_dict["X"]:  # say X
            path = "audio_samples/letter_mode/letters/x.wav"
        elif button == braille_dict["Y"]:  # say Y
            path = "audio_samples/letter_mode/letters/y.wav"
        elif button == braille_dict["Z"]:  # say Z
            path = "audio_samples/letter_mode/letters/z.wav"
        elif button == braille_dict["SPACE"]:
            path = "audio_samples/spacebar.wav"

    if path != "":
        player(path)


def active_buttons(GPIO, level, tick):
    global buttons
    global gate
    if level == 1:
        gate += 1
    else:
        gate -= 1

    if GPIO == 27:
        buttons[0] = 1
    elif GPIO == 22:
        buttons[1] = 1
    elif GPIO == 17:
        buttons[2] = 1
    elif GPIO == 25:
        buttons = [0, 0, 0, 0, 0, 0]
    elif GPIO == 26:
        buttons[3] = 1
    elif GPIO == 12:
        buttons[4] = 1
    elif GPIO == 13:
        buttons[5] = 1

    if gate == 0:
        mapping(buttons)
        buttons = [0, 0, 0, 0, 0, 0]
