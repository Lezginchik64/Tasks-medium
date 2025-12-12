from fractions import Fraction

n, m = input(), input()
n1, m1 = Fraction(n), Fraction(m)
print(f"{n} + {m} = {n1 + m1}")
print(f"{n} - {m} = {n1 - m1}")
print(f"{n} * {m} = {n1 * m1}")
print(f"{n} / {m} = {n1 / m1}")
