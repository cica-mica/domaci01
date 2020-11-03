"""
Dat je cetvorocifren broj ABCD. Stampati poruku "Super" ako vazi a  b=c  d.
"""

uneseni_broj = input('Unesite cetvorocifren broj: ')

print(uneseni_broj)
while True:
   if int(uneseni_broj[1]) == int(uneseni_broj[2]):
      print('Super!')
      break
   else:
       print('Vrati se na pocetak.')
       uneseni_broj = int(input('Unesite sledeci broj: '))
       uneseni_broj = str(uneseni_broj)

