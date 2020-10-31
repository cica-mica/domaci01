"""
Napisati program koji ucitava 6 realnih brojeva x1, y1, x2, y2, x3, y3 koji redom predstavljaju kooordinate tacaka A(x1, y1),
B(x2, y2) i C(x3, y3) i stampa povrsinu i obim trougla ABC.
"""
import math

A = (5,2)
B = (4,-1)
C = (-6, 3)

x1 = A[0]
x2 = B[0]
x3 = C[0]
y1 = A[1]
y2 = B[1]
y3 = C[1]

P = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2

AB = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
BC = math.sqrt(math.pow(x3-x2, 2) + math.pow(y3-y2, 2))
AC = math.sqrt(math.pow(x3-x1, 2) + math.pow(y3-y1, 2))

O = AB + BC + AC
print(O)
print(P)