import random

# 1
n = int(input())    # количество попыток
for _ in range(n):
    r = random.randint(0, 1)
    if r == 0:
        print("Орел")
    else:
        print("Решка")

# 2
Coin = ["Орел", "Решка"]
for _ in range(int(input())):
    print(Coin[random.randint(0, 1)])



