"""
Napisati kod koji izracunava vrijednost funkcije y.
"""
import math

x = int(input('Unesite vrijednost promjenljive x: '))

if x<= 0:
    y = -2* x**2 + 7/2
else:
    y = math.sin(math.radians(2*x + 5))
    

print(y)