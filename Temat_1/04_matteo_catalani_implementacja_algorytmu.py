import math

# Zakres liczb podany od uzytkownika
ile_liczb = int(input("Podaj ile liczb jest do sprawdzenia: "))
# Tworzenie listy o rozmiarze ile_liczb i wartosciami True
lista_liczb = [True] * ile_liczb

# Sprawdzenie czy w danym zakresie sa liczby pierwsze - sito Eratostenesa
if ile_liczb < 2:
    print("Brak liczb pierwszych w podanym zakresie.")
else:
    for i in range(2, math.ceil(math.sqrt(ile_liczb))):
        if lista_liczb[i] == True:
            for j in range(i * i, ile_liczb, i):
                lista_liczb[j] = False

# Wyswietlenie, ktore liczby sa pierwsze
for i in range(2, ile_liczb):
        if lista_liczb[i] == True:
            print("Liczba", i, "jest pierwsza.")