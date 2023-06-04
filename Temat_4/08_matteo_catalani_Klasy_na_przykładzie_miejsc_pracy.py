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
        print(f"Nazywam się {self.imie} {self.nazwisko}. Pracuje na {self.miejsce_pracy}")


class Lekarz(Pracownik):
    def __init__(self, imie: str, nazwisko: str):
        super().__init__(imie, nazwisko, "szpitalu")

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}. Pracuje w {self.miejsce_pracy}")


### MAIN ###

policjant = Policjant("Jan", "Kowalski")  # Tworzenie instancji klasy Policjant
policjant.przedstaw_sie()  # Wywołanie metody przedstaw_sie() dla obiektu policjant

lekarz = Lekarz("Jan", "Kowalski")  # Tworzenie instancji klasy Lekarz
lekarz.przedstaw_sie()  # Wywołanie metody przedstaw_sie() dla obiektu lekarz
