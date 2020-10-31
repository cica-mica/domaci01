"""
Napisati kod koji proverava da li je zbir cifara datog trocifrenog broja dvocifren broj.
"""


uneseni_broj = 251
a = uneseni_broj//100
b = (uneseni_broj//10)%10
c = uneseni_broj%10

def zbir_cifara_trocifrenog_broja(a,b,c):
    if (a+b+c)> 9:
        return True
    else:
        return False

zbir_cifara_trocifrenog_broja(a, b, c)
print('It is', zbir_cifara_trocifrenog_broja(a, b, c), 'that', uneseni_broj, 'has two digits.')