"""
Napisati kod koji izracunava vrijednost funkcije y.
"""
import math

y = 0

def jednacina_u_zavisnosti_od_x(x):
    if x<= -7:
        y = -2*x + 7/2
    elif x> -7 and x< 1:
        y = (x**2 - 3*x +5)/(x**2 +2)
    elif x>=1 and x<=8:
        y = math.sqrt(x**2 + 2*x + 2) + math.sqrt(abs(3/2 *x - 4/7))
    else:
        y = abs(3/(x**2) - 11*x)
    return y

print(jednacina_u_zavisnosti_od_x(9))
