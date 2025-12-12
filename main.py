from fractions import Fraction
from math import factorial as f

# 1
print(sum([Fraction(1, f(i)) for i in range(1, int(input()) + 1)]))

# 2
res = 0
for i in range(1, int(input()) + 1):
    res += Fraction(1, f(i))
print(res)
