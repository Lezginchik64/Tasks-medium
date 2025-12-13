from fractions import Fraction as F

res = set()
for i in range(2, int(input()) + 1):    # Знаменатель i начинается с 2, потому что дробь должна быть между 0 и 1 (не включая 0 и 1)
    for j in range(1, i):       # j начинается с 1, потому что по условию дробь должна быть меньше единицы, значит, j должен быть меньше i
        res.add(F(j, i))
print(*sorted(res), sep='\n')
