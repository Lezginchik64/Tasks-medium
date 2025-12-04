import random

# 1
s = set()
while len(s) < 7:
    s.add(random.randint(1, 49))
print(*sorted(s))

# 2
# random.sample гарантирует уникальные элементы
s = random.sample(range(1, 50), 7)

print(*sorted(s))