# -- Тема урока: вложенные словари, генераторы словарей --

# -- Вложенные словари --
# Словари могут содержать другие словари, которые сами, в свою очередь, содержат словари, и так далее на любую глубину. Такие словари называются вложенными словарями
# 1
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

# 2
info = dict(emp1 = {'name': 'Timur', 'job': 'Teacher'},
            emp2 = {'name': 'Ruslan', 'job': 'Developer'},
            emp3 = {'name': 'Rustam', 'job': 'Tester'})

# 3
ids = ['emp1', 'emp2', 'emp3']

emp_info = [{'name': 'Timur', 'job': 'Teacher'},
            {'name': 'Ruslan', 'job': 'Developer'},
            {'name': 'Rustam', 'job': 'Tester'}]

info = dict(zip(ids, emp_info))


# Обращение к элементам вложенного словаря
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

print(info['emp1']['name'])
print(info['emp2']['job'])
print()

# Изменение вложенных словарей
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

info['emp1']['job'] = 'Manager'

print(info['emp1'])
print()

# Итерация по вложенным словарям
# 1
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

for emp in info:
    print('Employee ID:', emp)
    for key in info[emp]:
        print(key + ':', info[emp][key])
print()

# 2 с помощью метода items():
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

for emp, inf in info.items():
    print('Employee ID:', emp)
    for key in inf:
        print(key + ':', inf[key])
print()


# -- Генераторы словарей --
# код без генератора
squares = {}
for i in range(6):
    squares[i] = i**2

# с генератором
squares = {i: i**2 for i in range(6)}   # {ключ: значение for переменная in последовательность}
print(squares)
print()

# Генератор словаря при итерировании по строке.
dct = {c: c * 3 for c in 'ORANGE'}
print(dct)
print()

lst = ['ReD', 'GrEeN', 'BlUe']
dct = {i.lower(): i.upper() for i in lst}
print(dct)
print()

# Извлечение из словаря элементов с определенными ключами.
dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selected_keys = [0, 2, 5]
dct2 = {i: dict1[i] for i in selected_keys}
print(dct2)
print()

# Условия в генераторе словарей
squares = {i: i**2 for i in range(10) if i % 2 == 0}
print(squares)
print()

# Не забываем про возможность указания шага в функции range().
# Предыдущий код можно записать и без условного оператора: squares = {i: i**2 for i in range(0, 10, 2)}


# -- Генераторы вложенных словарей --
squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}
for value in squares.values():
    print(value)
print()

# считать буквы можно способом:
word = input()
d = {letter: word.count(letter) for letter in word}
print(d)