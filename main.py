# Вложенные списки
my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik!']]

print(my_list[0][2])       # индексирование строки 'Python'
print(my_list[1][1])       # индексирование списка [10, 20, 30]
print(my_list[2][-1])      # индексирование списка ['Beegeek', 'Stepik!']
print(my_list[2][-1][-1])  # индексирование строки 'Stepik!'
# ВЫВОД:
# t
# 20
# Stepik!
# !

# Общее количество элементов во вложенном списке
total = 0
my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]

for li in my_list:
    total += len(li)

print(total)