"""
Napisati kod koji za datu osnovicu a i krak b jednakokrakog trougla racuna povrsinu i zapreminu tijala koje se dobija rotacijom trougla
oko osnovice.
"""

import math

a = 8
b = 5

P = a * math.pi * (a/2 + b)

ha = math.sqrt(math.pow(b,2) - math.pow(a/2 , 2))
print(ha)
V = (math.pow(a, 2 ) * math.pi * ha)/6

print(P)
print(V)