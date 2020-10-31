"""
Napisati kod koji za date katete a i b (a<b) pravouglog trougla racuna povrsinu i zapreminu tijela koje se dobija rotacijom trougla oko
hipotenuze.
"""
import math

a = 3
b = 4
c = math.sqrt(math.pow(a,2) + math.pow(b,2))
hc = a*b/c

P1 = hc* math.pi * (hc + b)
P2 = hc * math.pi * (hc + a)
P = P1 + P2

V = (math.pow(hc,2)* math.pi * c)/3

print(P)
print(V)