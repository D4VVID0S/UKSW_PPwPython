def dodaj_sekwencje(sekwencja):
    print("Skwencja wejściowa", sekwencja)
    sekwencja_lista = list(sekwencja)
    sekwencja_lista.extend(sekwencja_lista)
    print("Nowa sekwencja jako lista", sekwencja_lista)
    return sekwencja_lista

def listuj_elementy(sekwencja):
    print("Sekwencja wejściowa", sekwencja)
    najdluzszy_ciag_znakow = max(sekwencja)
    przesuniecie = len(str(najdluzszy_ciag_znakow)) + 2
    print("Listowanie elementów sekwencji")
    for indeks, element in enumerate(sekwencja):
        lancuch = f"{{w:>{przesuniecie}}}"
        print(indeks, lancuch.format(w=element))

def main():
    sekwencja = [1,22,333,4444,55555,666666,7777777]
    dodaj_sekwencje(sekwencja)
    listuj_elementy(sekwencja)

if __name__ == "__main__":
    main()