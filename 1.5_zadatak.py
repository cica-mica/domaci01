"""
Napisati kod koji za date osnovice a i be i krake c i d (c<d) pravouglog trapeza racuna povrsinu i zapreminu tijela koje se dobija 
rotacijom trapeza oko manjeg kraka.
"""

import math

a = 4
b = 2
c = 3
d = 7

P = math.pi * (math.pow(a,2) + math.pow(b,2) + (a+b)*d)


V = (c * math.pi * (math.pow(a,2) + a*b + math.pow(b,2)))/3

print(P)
print(V)