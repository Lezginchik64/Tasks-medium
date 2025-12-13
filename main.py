from fractions import Fraction as F
from math import gcd

n = int(input())
a = n // 2  # числитель
b = n - a  # знаменатель  a + b = n, поэтому b = n - a
while gcd(a, b) != 1:       # gcd - наибольший общий делитель
    a -= 1
    b += 1
print(F(a, b))
