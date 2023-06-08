import numpy as np

K = 3 # Wymiary
J = 4 # Wiersze
I = 8 # Kolumny

a = np.random.randint(0, 10, size=(K, J, I))

while True:
    try:        
        # Wczytanie tablicy tidx od użytkownika
        tidx_str = input("Podaj indeksy dla tidx oddzielone spacjami: ")
        tidx = [int(idx) for idx in tidx_str.split()]

        # Sprawdzenie poprawności danych
        if len(tidx) != J:
            raise ValueError("Niepoprawna liczba indeksów. Podaj dokładnie 4 indeksy.")
        if not all(0 <= idx < K for idx in tidx):
            raise ValueError("Niepoprawny indeks. Indeksy muszą być liczbami całkowitymi od 0 do", K-1)

        # Wyście z pętli, jeśli dane są poprawne
        break

    except ValueError as e:
        print("Błąd:", str(e))
        print("Spróbuj ponownie.")

print("Originalna tablica:\n", a)
print("\nKształt:", a.shape)

tablica_wybranych_wierszy = np.random.randint(0, 10, size=(J, I))
for i in range(4):
    tablica_wybranych_wierszy[i, :] = a[: ,tidx, :]

print("\nTablica wybranych wierszy:\n", tablica_wybranych_wierszy)
print("\n", "Rozmiar tablicy wybranych wierszy:", tablica_wybranych_wierszy.shape, "\n")