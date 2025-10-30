# Способ 1
char_list = []
a = []
for char in input().split():
    if not char_list:               # проверяем пустой ли char_list
        char_list.append(char)      # если пустой, кладем в него первый введенный нами символ (char)
    else:
        if char_list[-1] == char:
            char_list.append(char)     # если символ из a равен следующему введенному символу, добавляем его в список char_list
        else:
            a.append(char_list)        # если символ не равен, добавляем группу одинаковых символов (char_list) в список a
            char_list = [char]       # обнуляем список char_list, создаем новый список с новой буквой
a.append(char_list)                 # оставшуюся последнюю букву (или несколько повторяющихся) кладем в список a
print(a)


# Способ 2
res = []
for el in input().split():
    if res and el in res[-1]:       # если список не пустой и элемент el есть в последнем списке элементов (res[-1])
        res[-1].append(el)              # добавляем этот элемент el в список (res[-1])
    else:
        res.append([el])            # если элемента нет в списке, создаем новый список элементов (res[-1]) с новыми буквами

print(res)