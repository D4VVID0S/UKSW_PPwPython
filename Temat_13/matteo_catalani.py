#!/usr/bin/env python
import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

time = 10  # czas symulacji
L = 5  # dlugosc boku obrazka
N = L * L  # liczba neuronow
n = 2  # liczba wzorcow do nauczenia
one = np.identity(N, dtype=np.int8)
w = np.zeros((N, N), dtype=np.int8)
x = np.array([1,-1,1,1,-1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1])
print(x.reshape(L, L))
pattern = []
pattern.append(np.array([-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,1]))  # A
# print(pattern[-1].reshape(L,L))
pattern.append(np.array([1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1]))  # Z
# print(pattern[-1].reshape(L,L))

# Etap uczenia
for mu in range(n):
    w += np.outer(pattern[mu], pattern[mu]) - one
    # print(w)

# Etap symulacji (rozpoznawania wzorca)
for t in range(time):
    if t % 1 == 0:
        print(t * 100 / time, "%")

        # Wczytanie obrazka i przycięcie do 5x5
        img = Image.open('image.png')
        img = img.convert('L')  # Konwersja do skali szarości

        width, height = img.size
        if width < L or height < L:
            sys.exit("Błąd: Obrazek jest za mały. Ma mieć rozmiar 5x5 pikseli (minimum)")

        img = img.crop((0, 0, L, L))  # Przycięcie do 5x5 pikseli

        # Konwersja z formatu zero-jeden (0-255) na (-1, 1)
        img = np.array(img)
        img = np.where(img > 0, 1, -1)

        x = img.reshape(-1)

        plt.imshow(x.reshape(L, L), cmap=plt.cm.Greys_r, interpolation='none')
        plt.savefig(str('letter%03d' % t) + ".png", format="png")

    x = np.sign(np.dot(w, x))

    for i in range(N):
        if x[i] == 0:
            x[i] = 1
