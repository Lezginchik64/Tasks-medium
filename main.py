lst = input().split()
result = {}
for i in lst:
    if i in result:               # если слово есть в словаре, добавляю a_1
        print(f'{i}_{result[i]}', end=" ")
    else:
        print(i, end=" ")       # если нету, добавляю само слово
    result[i] = result.get(i, 0) + 1    # получаем количество каждой буквы/слова, если встречаем одинаковое, увеличиваем на 1
