
""" Compile to exe cmd: python -OO -m PyInstaller --onefile --icon=_icon.ico main.py"""

import pigpio
from socket import gethostbyname
from dot_mode import buttons as dmb
from letter_mode import active_buttons as lmb
from number_mode import active_buttons as nmb
cb = []
G = [18, 27, 22, 17, 25, 26, 12, 13, 16]

while True:
    try:
        ip = gethostbyname('brailler')
        print("IP: ", ip)
        break
    except:
        print("Brailler not found in network")
        while True:
            choice = input('Try again?(y/n)')
            if choice == "y" or choice == "Y":
                break
            elif choice == "n" or choice == "N":
                quit()
            else:
                print("Incorrect input")
                continue

while True:
    pi = pigpio.pi(str(ip))
    print("1. Dot Mode\n2. Letter Mode\n3. Number Mode")
    choice = input("Choose Mode 1, 2, 3 or q to quit:\n")
    if choice == "1":
        for g in G:
            cb.append(pi.callback(g, pigpio.EITHER_EDGE, dmb))
        input('Press any key to exit\n')
        for c in cb:
            c.cancel()
        pi.stop()
    elif choice == "2":
        for g in G:
            cb.append(pi.callback(g, pigpio.EITHER_EDGE, lmb))
        input('Press any key to exit\n')
        for c in cb:
            c.cancel()
        pi.stop()
    elif choice == "3":
        for g in G:
            cb.append(pi.callback(g, pigpio.EITHER_EDGE, nmb))
        input('Press any key to exit\n')
        for c in cb:
            c.cancel()
        pi.stop()
    elif choice == "q" or choice == "Q":
        break
    else:
        print("Incorrect input")
        continue
