"""
Napisati kod koji za kvadratnu jednacinu ax2 + bx + c = 0 ispituje da li ima realna resenja.
"""
import math

a = 4
b = -9
c = 5

def ima_li_realna_resenja(a,b,c):
    if (math.pow(b,2) - 4*a*c)>= 0:
        return True
    else: 
        return False

print(ima_li_realna_resenja(a,b,c))