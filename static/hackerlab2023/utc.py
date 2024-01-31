import random
import os
import time


tresor = "CTF_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

t = int(time.time())
random.seed(t)


def encrypt(data):
    assert isinstance(data, bytes)

    cipher = []
    for b in data:
        r = random.randint(0, 255)
        c = (b+r) % 256
        cipher.append(c)
    return cipher


def intro():
    print("[+] U.T.C [+]")
    print("Choisir (e) pour récupérer le trésor et (q) pour quitter")


def main():
    intro()

    while True:
        try:
            choice = input()
        except:
            exit()

        if choice == "e":
            tresor_enc = encrypt(tresor.encode())
            print("-".join(map(str, tresor_enc)))
        if choice == "q":
            print("Byeeeeeeeeeee !!!")
            exit()


main()
