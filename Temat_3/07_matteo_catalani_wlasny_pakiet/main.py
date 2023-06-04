from pakiet.modul_katalog.funkcje import dodaj_sekwencje, listuj_elementy
from pakiet.trzy_funkcje import funkcja_1, funkcja_2, funkcja_3

def main():
    print("===============")
    dodaj_sekwencje([123,3456,67893])
    print("===============")
    listuj_elementy([1,4444,341,22,5304293])
    print("===============")
    funkcja_1()
    print("===============")
    funkcja_2()
    print("===============")
    funkcja_3()
    print("===============")
    print("Koniec")

if __name__ == "__main__":
    main()