"""
1. Napisati kod koji za date katete a i b (a>b) pravouglog trougla racuna povrsinu i zapreminu tijela koje se dobija rotacijom trougla 
oko manje katete.
"""
import math 

# rotacijom trougla oko katete b dobija se kupa s poluprecnikom a i visinom b
a = 8
b = 6

# racunamo duzinu hipotenuze jer ce nam biti potrebna pri racunanju povrsine
c = math.sqrt(a*a + b*b)
P = math.pi * math.pow(a,2) + c*a* math.pi
V = (math.pow(a,2)*b* math.pi)/3

print(P)
print(V)