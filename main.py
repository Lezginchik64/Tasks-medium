from fractions import Fraction

res = 0
for i in range(1, int(input()) + 1):
    res += Fraction(1, i ** 2)
print(res)