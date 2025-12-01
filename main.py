# 1
d = {}
for _ in range(int(input())):
    country, *cities = input().split()
    d.update(dict.fromkeys(cities, country))    # update - Он объединяет ключи и значения одного словаря с ключами и значениями другого.
for _ in range(int(input())):                   # dict.fromkeys(cities, country) - создает новый словарь,
    print(d[input()])                           # где cities — ключи, а country — значение, которое будет присвоено ВСЕМ ключам.


# 2
d = {}
for _ in range(int(input())):
    a, *b = input().split()         # a, *b - первый элемент присваивается "а", остальное "b"
    d[a] = b

res = [input() for i in range(int(input()))]
for i in res:
    for j in d:
        if i in d[j]:
            print(j)
            break