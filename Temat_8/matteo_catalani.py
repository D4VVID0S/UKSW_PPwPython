import random
import math

def czy_igla_przecina(x, theta, t, L):
    y1 = x - L/2 * math.cos(theta)
    y2 = x + L/2 * math.cos(theta)
    return (y1 < 0 and y2 > 0) or (y1 < t and y2 > t)

def oszacuj_prawdopodobienstwo(t, L, n):
    przecinajace_igly = 0
    for _ in range(n):
        x = random.uniform(0, t)
        theta = random.uniform(0, 2 * math.pi)
        if czy_igla_przecina(x, theta, t, L):
            przecinajace_igly += 1
    return przecinajace_igly / n

def oblicz_prawdopodobienstwo_teoretyczne(t, L):
    if L > t:
        return 2 / math.pi
    elif L == t:
        return 1 / 2
    else:
        return (2 / math.pi) * (L / t) + (1 - L / t)

# Wczytanie danych od użytkownika
t = float(input("Podaj szerokość pasków (t): "))
L = float(input("Podaj długość igły (L): "))
n = int(input("Podaj liczbę rzutów (n): "))

# Obliczenie prawdopodobieństwa na podstawie symulacji
prawdopodobienstwo_symulacyjne = oszacuj_prawdopodobienstwo(t, L, n)

# Obliczenie teoretycznego prawdopodobieństwa
prawdopodobienstwo_teoretyczne = oblicz_prawdopodobienstwo_teoretyczne(t, L)

# Wypisanie wyników
print("Prawdopodobieństwo przecięcia pasków (symulacja):", prawdopodobienstwo_symulacyjne)
print("Prawdopodobieństwo przecięcia pasków (teoria):", prawdopodobienstwo_teoretyczne)
