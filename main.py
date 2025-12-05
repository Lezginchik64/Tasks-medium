import random

s = set()
while len(s) < 100:
    tickets = random.randint(1000000, 9999999)  # 1.000.000 — самое маленькое 7-значное число, 9.999.999 — самое большое 7-значное число
    s.add(tickets)

for i in s:
    print(i)
