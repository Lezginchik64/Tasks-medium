# Вариант 1
n, k = int(input()), int(input())
res = 0
for i in range(1, n + 1):
    res = (res + k) % i
print(res + 1)

# Вариант 2
n, k = int(input()), int(input())
res = []
for i in range(1, n + 1):
    res.append(i)
index = 0
while len(res) > 1:
    index = (index + k - 1) % len(res)      # новый_индекс = (текущий_индекс + k - 1) % len(список)
    removed = res.pop(index)            # k - 1 потому что, если мы на 1 человеке, а хотим убить 3, нам нужно сделать 2 шага (3 - 1)
print(*res)
