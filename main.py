# Сортировка кортежей

# С помощью встроенной функции sorted() (не путать со списочным методом sort()) мы можем сортировать значения в кортежах.
not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
print(not_sorted_tuple)

sorted_tuple = tuple(sorted(not_sorted_tuple))
print(sorted_tuple)
# Обратите внимание, что функция sorted() возвращает список, но с помощью функции tuple() мы приводим результат сортировки к кортежу.
# Для сортировки кортежа можно воспользоваться явным преобразованием в список и использовать метод sort():
not_sorted_tuple = ('cc', 'aa', 'dd', 'bb')
tmp = list(not_sorted_tuple)
tmp.sort()

sorted_tuple = tuple(tmp)
print(sorted_tuple)

# Строку можно преобразовать в кортеж с помощью функции tuple().
letters = 'abcdefghijkl'
tpl = tuple(letters)
print(tpl)

# Если вам нужно преобразовать строку в кортеж но не поэлементно, а целиком как 1 элемент используйте (,)
letters = 'abcdefghijkl'
tpl = (letters,)
print(tpl)