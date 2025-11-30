# 1
d = {}
for _ in range(int(input())):
    key, value = input().split(": ")    # деление строк по двоеточию
    d[key.lower()] = value              # добавление ключей и элементов в словарь, с уменьшением регистра ключей

s = [input().lower() for _ in range(int(input()))]

for i in s:             # проверка и вывод элементов из словаря
    if i in d:
        print(d[i])
    else:
        print("Не найдено")

# 2
d = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    d[key.lower()] = value

for _ in range(int(input())):
    print(d.get(input().lower(), 'Не найдено'))   # dict.get(key, default) возвращает:
                                                    # Если key есть в словаре - возвращает значение
                                                    # Если key нет - 'Не найдено'
