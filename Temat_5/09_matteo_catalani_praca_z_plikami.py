class Pracownik:
    def __init__(self, imie: str, nazwisko: str, miejsce_pracy: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejsce_pracy = miejsce_pracy

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}. Pracuję w {self.miejsce_pracy}")


class Policjant(Pracownik):
    def __init__(self, imie: str, nazwisko: str):
        super().__init__(imie, nazwisko, "komisariacie")

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}. Pracuję na {self.miejsce_pracy}")


class Lekarz(Pracownik):
    def __init__(self, imie: str, nazwisko: str):
        super().__init__(imie, nazwisko, "szpitalu")

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}. Pracuję na {self.miejsce_pracy}")


if __name__ == "__main__":
    wczytano_pracownikow = False
    bledne_linie = []
    
    while not wczytano_pracownikow:
        nazwa_pliku = input("Podaj nazwę pliku: ")
        
        try:
            with open(nazwa_pliku, "r") as plik:
                lista_pracownikow = []
                numer_linii = 0
                
                for linia in plik:
                    numer_linii += 1
                    linia = linia.strip()
                    
                    if linia == "":
                        continue
                    
                    kolumny = linia.split()
                    
                    if len(kolumny) < 3:
                        bledne_linie.append(f"linia nr {numer_linii} ma mniej niż 3 kolumny")
                    elif len(kolumny) > 3:
                        bledne_linie.append(f"linia nr {numer_linii} ma więcej niż 3 kolumny")
                    else:
                        imie = kolumny[0]
                        nazwisko = kolumny[1]
                        miejsce_pracy = kolumny[2]
                        
                        if miejsce_pracy == "komisariat":
                            pracownik = Policjant(imie, nazwisko)
                        elif miejsce_pracy == "szpital":
                            pracownik = Lekarz(imie, nazwisko)
                        else:
                            pracownik = Pracownik(imie, nazwisko, miejsce_pracy)
                        
                        lista_pracownikow.append(pracownik)
                
                for pracownik in lista_pracownikow:
                    pracownik.przedstaw_sie()
                
                wczytano_pracownikow = True
                
        except FileNotFoundError:
            print("Nie ma takiego pliku, podaj poprawną nazwę pliku")
        
        except Exception as e:
            print(e)
        
        finally:
            if 'plik' in locals():
                plik.close()
    
    for blad in bledne_linie:
        print(blad)