"""
Napisati kod koji ucitava dva cijela broja m i n i stampa poruku "x je djeljiv sa y" ili "x nije djeljiv sa y". 
Npr. "15 je djeljiv sa 3" ili "15 nije djeljiv sa 4".
"""

m = 25
n = 5

def x_je_djeljiv_sa_y(x,y):
    if x%y == 0:
        print(x, 'je djeljiv sa', y)
    else:
        print(x, 'nije djeljiv sa', y)

x_je_djeljiv_sa_y(m,n)