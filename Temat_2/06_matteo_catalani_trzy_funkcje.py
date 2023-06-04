def funkcja_1():
    lista = []
    n = int(input("Podaj ilosc elementow do dodania do listy:"))
    # Dodawanie elementow do listy jako int
    print("Podaj elementy:")
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
        print("Lista zawiera dwa elementy 20 i co najmniej trzy elementy 7")
        return True
    else:
        print("Lista nie zawiera dwóch elementów 20 i co najmniej trzech elementów 7")
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
    print("Liczba kamieni", n_kamieni)
    return n_kamieni

def funkcja_3():
    zdanie = input("Podaj zdanie:")
    print("Wprowadzone zdanie", zdanie)
    lista_separatorow = []

    for c in zdanie:
        if c == " " or c == "," or c == ".":
            lista_separatorow.append(c)

    zdanie_bez_przecinkow = zdanie.replace(",", " ")
    lista_slow = zdanie_bez_przecinkow.split()
    
    print("Lista separatorów", lista_separatorow)
    print("Lista słów ", lista_slow)
    return lista_separatorow, lista_slow

def main():
    print("Funkcja 1:", funkcja_1())
    print("Funkcja 2:", funkcja_2())
    print("Funkcja 3:", funkcja_3())

if __name__ == "__main__":
    main()