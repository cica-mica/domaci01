"""
Napisati kod koji za datu osnovicu a i krak b jednokrakog trougla racuna povrsinu i zapreminu tijela koje se dobija rotacijom trougla
oko visine spustene na osnovicu.
"""
import math

a = 6
b = 5

ha = math.sqrt(math.pow(b,2) - math.pow((a/2),2))

P = a/2 * math.pi * (a/2 + b)

V = math.pow((a/2),2) * math.pi * ha

print(P)
print(V)