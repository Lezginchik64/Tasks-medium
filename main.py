# 1
dct = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    dct.setdefault(name, []).append(phone)

for _ in range(int(input())):
    print(*dct.get(input().lower(), ['абонент не найден']))

# 2
d = {}
for _ in range(int(input())):
    a, b = input().lower().split()
    d.setdefault(b, []).append(a)

for _ in range(int(input())):
    i = input().lower()
    if i in d:
        print(*d[i])
    else:
        print("абонент не найден")