"""
Napisati kod koji za 3 data cijela broja x, y, z stampa najveci od njih.
"""

x = int(input('Upisite cijeli broj: '))
y = int(input('Upisite cijeli broj: '))
z = int(input('Upisite cijeli broj: '))

niz_brojeva = [x, y, z]

"""
def najveci_od_tri_broja(a, b, c):
    if a>b and a>c:
        print(a)
    elif b>=a and b>c:
        print(b)
    elif c>=a and c>=b:
        print(c)

najveci_od_tri_broja(x, y, z)
"""

niz_brojeva.sort()
rezultat = niz_brojeva[2]
print(rezultat)