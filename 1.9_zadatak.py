"""
Napisati kod koji ucitava brojeve x, a i b i provjerava da li x pripada intervalu [a,b] i stampa odgovarajucu poruku ("Pripada"
ili "Ne pripada")
"""

x = int(input('Unesite proizvoljan broj: '))
a = -32
b = 6

def da_li_broj_pripada_intervalu(a,b,c):
    if a>=b and a<=c:
        return True
    else:
        return False

da_li_broj_pripada_intervalu(x,a,b)
print(da_li_broj_pripada_intervalu(x,a,b))