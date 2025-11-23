a, b, c = [set(input().split()) for _ in range(3)]
i = a.intersection(b)                               # i - общие элементы a и b
d = sorted(list(i.difference(c)), reverse=True, key=int)     # элементы, которых нет в i, отсортированные в обратном порядке
if i and d:                     # key=int - Перед сортировкой преобразуй каждый элемент в число
    print(*d)
