import matplotlib.pyplot as plt

# Wczytanie nazwy pliku od uzytkownika
nazwa_pliku = input('Podaj nazwe pliku do wczytania: ')

# Listy dla wartosci x i y
wartosci_x = []
wartosci_y = [] 

try:
    # Otwarcie pliku w trybie odczytu
    with open(nazwa_pliku, 'r') as plik:

        # Odczytanie wartosci po linii
        for linia in plik:
            elementy = linia.split()

            # Wczytanie wartosci x z pierwszego elementu (elementy[0])
            wartosci_x.append(elementy[0])
            # Wczytanie wartosci y z drugiego elementu (elementy[1])
            wartosci_y.append(elementy[1])

except FileNotFoundError:
    print('Plik o podanej nazwie nie istnieje.')

except IOError:
    print('Wystąpił błąd podczas odczytu pliku.')

# Wyświetlenie wczytanych wartości x i y
print("Wczytane wartości x:", wartosci_x)
print("Wczytane wartości y:", wartosci_y)

# Generowanie wykresu liniowego
plt.plot(wartosci_x,wartosci_y,color='red')
# Nadanie etykiety osi poziomej
plt.xlabel('Oś x')
# Nadanie etykiety osi pionowej
plt.ylabel('Oś y')
# Nadanie nazwy wykresowy na podstawie wczytanego pliku
plt.title(nazwa_pliku)
# Wyświetlenie wykresu liniowego
plt.show()