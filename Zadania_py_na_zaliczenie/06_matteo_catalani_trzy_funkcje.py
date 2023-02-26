def funckja_1():
    lista = []
    n = int(input("Podaj ilosc elementow do dodania do listy:"))
    # Dodawanie elementow do listy jako int
    for i in range(n):
        lista.append(int(input()))

    # liczniki sprawdzajace ile razy dana wartosc znajduje sie w liscie
    licznik_20 = 0
    licznik_7 = 0

    # inkrementacja licznika jezeli liczba 20 lub 7 jest w liscie
    for i in range(len(lista)):
        if lista[i] == 20:
            licznik_20 = licznik_20 + 1
        if lista[i] == 7:
            licznik_7 = licznik_7 + 1

    # zwraca True jeśli lista ma dokładnie dwa elementy o wartości 20 i co najmniej trzy elementy o wartości 7.
    if (licznik_20 == 2 and licznik_7 >= 3):
        return True
    else:
        return False
    
def funkcja_2():
    n_stosow = int(input("Podaj ile stosow kamieni nosisz w plecaku:"))
    n_kamieni = [n_stosow] * n_stosow

    if n_stosow % 2 == 0:
        print("Wszystkie stosy są parzyste")
    else:
        print("Wszystkie stosy są nieparzyste")
        
    licznik = 0
    for i in range(n_stosow * 2):
        if i % 2 == 0:
            n_kamieni[licznik] = n_kamieni[licznik] + i
            licznik = licznik + 1
    print(n_kamieni)

def funkcja_3():
    zdanie = input("Podaj zdanie:")
    print(zdanie)
    lista_separatorow = []
    lista_slow = []
    koniec = 0

    for i, c in enumerate(zdanie):
        if c == " " or c == "," or c == ".":
            lista_separatorow.append(c)

    lista_slow = zdanie.replace(",", " ")
    
    print(lista_separatorow)
    print(lista_slow.split())


# ========== MAIN ==========
print("Funkcja 1:", funckja_1())
print("Funkcja 2:", funkcja_2())
print("Funkcja 3:", funkcja_3())