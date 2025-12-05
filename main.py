# -- Методы модуля random --
import random


# -- Метод shuffle() --
# Метод shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.
# Следующий код перемешивает список numbers случайным образом, а затем выводит его содержимое:
print("Метод shuffle")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)
print()


# -- Метод choice() --
# Метод choice() принимает список (строку, кортеж) в качестве обязательного аргумента и возвращает один случайный элемент.
# Элементы могут повторяться!
# Следующий код выводит по одному случайному элементу из строки 'BEEGEEK', списка [1, 2, 3, 4] и кортежа ('a', 'b', 'c', 'd'):
print("Метод choice")
print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(('a', 'b', 'c', 'd')))
print()


# -- Метод sample() --
# Метод sample() принимает два обязательных аргумента:
# первый – коллекция (последовательность), которая поддерживает индексацию (список, строка, кортеж), второй – количество случайных элементов.
# Возвращает список из указанного количества УНИКАЛЬНЫХ (имеющих разные индексы) случайных элементов.
print("Метод sample")
numbers = [2, 5, 8, 9, 12]
print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))
print()
# Количество случайных элементов не должно превышать длину исходного списка (строки)


# -- Модуль string --
# Встроенный модуль string раньше использовался для расширения стандартных возможностей (функционала) строкового типа данных str.
# На текущий момент все функции из модуля string переехали в методы строкового типа данных str, однако в модуле string остались удобные константные строки, которые можно использовать при решении задач.
import string

print("Модуль string")
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)