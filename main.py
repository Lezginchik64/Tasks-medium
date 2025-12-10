from decimal import *

# 1
num = Decimal(input())
d = num.as_tuple().digits
print(max(d) + min(d) * (abs(num) >= 1))  # abs(num) >= 1 возвращает 1 (true) или 0 (false), это число умножается на min(d)


# 2
num = list(input())
a = [abs(int(i)) for i in num if i in "0123456789"]
print(max(a) + min(a))
