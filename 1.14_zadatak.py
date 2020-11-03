"""
Dat je cetvorocifreni prirodan broj. Ako su mu cifra jedinica i cifra hiljada jednake, stampati kvadrat dvocifrenog broja 
koji se dobije kada se uklone cifra jedinica i cifra hiljada. Ako te dvije cifre nisu jednake, stampati zbir kvadrata svih cifara.
"""

uneseni_broj = input('Unesite cetvorocifren broj: ')

while True:
    if uneseni_broj[0] == uneseni_broj[3]:
        rezultat = (int(uneseni_broj[1])*10 + int(uneseni_broj[2]))**2
        print(rezultat)
        break
    else:
        rezultat = int(uneseni_broj[0])**2 + int(uneseni_broj[1])**2 + int(uneseni_broj[2])**2 + int(uneseni_broj[3])**2
        print(rezultat)
        uneseni_broj = input('Unesite sledeci cetvorocifreni broj: ')