class KontoBankowe:

  def __init__(self, numer_konta, saldo, wlasciciel_konta):
    self.numer_konta = numer_konta
    self.saldo = saldo
    self.wlasciciel_konta = wlasciciel_konta
    self.dziennik = DziennikOperacji()

  def depozyt(self, kwota):
    self.saldo += kwota
    self.dziennik.dodaj_operacje('depozyt', kwota,)
    return self.saldo

  def wyplata(self, kwota):
    self.saldo -= kwota
    return self.saldo

  def przelew(self, kwota, konto_docelowe):
    if kwota <= self.saldo:
      self.saldo -= kwota
      konto_docelowe.depozyt(kwota)
    return self.saldo

class KontoOszczednosciowe(KontoBankowe):
    def oblicz_odsetki(self, oprocentowanie):
        odsetki = self.saldo*oprocentowanie
        self.saldo += odsetki
        return self.saldo

class KontoWalutowe(KontoBankowe):
    def __init__(self, numer_konta, saldo, wlasciciel_konta, waluta, kurs_waluty):
        self.waluta = waluta
        self.kurs_waluty = kurs_waluty 
        super().__init__(numer_konta, saldo, wlasciciel_konta)

    def przelicznik(self):
        if self.waluta != 'PLN':
            self.saldo = self.saldo * self.kurs_waluty
        return self.saldo

    def przelew_walutowy(self, kwota, konto_docelowe):
        kwota_w_walucie = kwota * self.kurs_waluty
        self.przelicznik()
        super().przelew(kwota_w_walucie, konto_docelowe)
        return self.saldo

class kontoVIP(KontoBankowe):
    def __init__(self, numer_konta, saldo, wlasciciel_konta, limit_wypłat):
       super().__init__(numer_konta, saldo, wlasciciel_konta)
       self.limit_wypłat = limit_wypłat
    
    def wyplata(self, kwota_wyplaty):
        if kwota_wyplaty > self.limit_wypłat:
            return 'Kwota wyplaty zbyt duza'
        else:
            self.saldo -= kwota_wyplaty
        return self.saldo

class DziennikOperacji:
    def __init__(self):
        self.operacje=[]

    def dodaj_operacje(self,rodzaj,kwota):
        operacja = {
            'rodzaj': rodzaj,
            'kwota': kwota,
        }
        self.operacje.append(operacja)
       


Uzytkownik1 = KontoBankowe('123456789', 1000, 'Jan Kowalski')
Uzytkownik2 = KontoOszczednosciowe('987654321', 400, 'Anna Nowak')
Uzytkownik3 = KontoWalutowe('098765432', 5000, 'Fedor Fedorowicz', 'EUR', 4.72)
Uzytkownik4 = kontoVIP('765432098', 2500, 'Ziomek Ziomkowy', 1000)

print(f'{Uzytkownik1.przelew(600, Uzytkownik2)} - saldo po wyslaniu przelewu')
print(f'{Uzytkownik2.saldo} - saldo po otrzymaniu przelewu')
print(f'{Uzytkownik2.oblicz_odsetki(0.04)} - saldo po roku odsetek')
print(f'{Uzytkownik3.przelew_walutowy(300, Uzytkownik1)} - saldo w {Uzytkownik3.waluta} po przelewie' )
print(f'{Uzytkownik1.saldo} - saldo po otrzymaniu przelewu w {Uzytkownik3.waluta}')
print(f'{Uzytkownik4.wyplata(999)} - saldo po wyplacie')
print(Uzytkownik1.dziennik.operacje)