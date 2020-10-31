"""
Dati su realni brojevi x, y, m, n, a i b. Napisati kod koji izracunava izraze.
"""
import math 
x = 3
y = 1
m = math.ceil(math.degrees(math.pi/12))
n = math.ceil(math.degrees(math.pi/6))
a = 3
b = 13
print(m)
print(n)

A = math.pow(x,3)/3 - 3* math.pow(y,2) + (x + 1)/(2*y + 3)
print(A)

B = - 5 * math.sqrt(x + math.sqrt(y))
print(B)

C = 1 + 1/(2 + 1/(3+ 1/4))
print (C)

D = 3* math.sin(2*math.radians(m))* math.cos(2*math.radians(n)) - 5* math.pow(math.tan(math.radians(m + n)),2)
print(D)

E = math.sqrt(math.pow(a,2) + math.pow(b,2) - 2*a*b* math.sin(math.radians(m)))
print(E)