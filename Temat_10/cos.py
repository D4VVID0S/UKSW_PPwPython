import numpy as np

# Tworzenie tablicy a o wymiarach (3, 4, 8)
a = np.array([[[3, 2, 2, 7, 7, 7, 0, 3],
               [5, 8, 4, 2, 9, 9, 3, 9],
               [6, 8, 2, 8, 5, 7, 8, 7],
               [5, 2, 4, 0, 4, 9, 2, 5]],

              [[4, 3, 1, 8, 2, 5, 2, 0],
               [9, 1, 5, 8, 8, 5, 6, 5],
               [3, 2, 2, 0, 1, 5, 6, 1],
               [5, 1, 9, 4, 2, 6, 9, 2]],

              [[4, 6, 6, 3, 8, 6, 8, 8],
               [3, 9, 2, 6, 3, 3, 1, 0],
               [5, 4, 0, 6, 0, 2, 7, 8],
               [6, 3, 1, 8, 8, 1, 5, 7]]])

print("Originalna tablica:")
print(a)
print("\nKształt:", a.shape)

# Wczytanie tablicy tidx od użytkownika
tidx_str = input("Podaj indeksy dla tidx oddzielone spacjami: ")
tidx = [int(idx) for idx in tidx_str.split()]

# Wybór danych z pierwszego wymiaru (K) na podstawie tidx
selected_data = a[:, tidx, :]

# Wypisanie wybranej tablicy
print("\nWybrana tablica:")
print(selected_data)
print("\nKształt:", selected_data.shape)
