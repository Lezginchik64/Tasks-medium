# -- Тема урока: модуль fractions --

# Рациональное число – это число, которое можно представить в виде дроби 5/6 числитель m = 5, а знаменатель n = 6.
# Знаменатель дроби показывает количество равных частей, а числитель дроби показывает, сколько из них взято.

# -- Тип данных Fraction --
# Для работы с рациональными числами в Python используется тип данных Fraction.
# Тип данных Fraction как и Decimal реализован программно, поэтому он в разы медленнее встроенных числовых типов данных int и float.
# Тип данных Fraction неизменяемый. Операции над данными этого типа приводят к созданию новых объектов, при этом старые не меняются.

# Создать Fraction число можно несколькими способами:
    # из целых чисел, передав значения числителя и знаменателя дроби,
    # из строки на основании десятичного представления;
    # из строки на основании обыкновенной дроби;
    # из числа с плавающей точкой (не рекомендуется).

from fractions import Fraction

print(" Создание Fraction")
num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
num2 = Fraction('0.55')
num3 = Fraction('1/9')
print(num1, num2, num3, sep='\n')

# Нужно быть очень внимательным при создании Fraction чисел из чисел с плавающей точкой (float),
# потому что float числа округляются внутри до ближайшего возможного, а Fraction об этом ничего не знает, поэтому копирует содержимое float.
num = Fraction(0.34)    # вместо ожидаемого вывода: 17/50
print(num)              #  код выводит: 6124895493223875/18014398509481984
print()
# Не рекомендуется создавать Fraction числа из float чисел. В Fraction попадет уже неправильно округленное число.
# Создавать Fraction числа нужно из целых чисел, либо из строк!

# Обратите внимание на то, что при создании рационального числа Fraction, автоматически происходит сокращение числителя и знаменателя дроби.
num1 = Fraction(5, 10)
num2 = Fraction('75/100')
num3 = Fraction('0.25')

print(num1, num2, num3, sep='\n')
print()


# -- Сравнение Fraction чисел --
print(" Сравнение Fraction чисел")
num1 = Fraction(1, 2)        # 1/2
num2 = Fraction(15, 30)      # 15/30=1/2
num3 = Fraction(3, 5)        # 3/5
num4 = Fraction(5, 3)        # 5/3
num5 = 1
num6 = 0.8
print(num1 == num2)
print(num1 != num4)
print(num2 > num3)
print(num4 <= num1)
print(num1 < num5)
print(num6 > num4)
print()


# -- Арифметические операции над Fraction числами --
print(" Арифметические операции над Fraction числами")
num1 = Fraction('1/10')
num2 = Fraction('2/3')
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 + 1)     # 1/10 + 1 = 1/10 + 10/10 = 11/10

num1 = Fraction('3/8')
num2 = Fraction('1/2')

print(num1 ** num2)
print()


# -- Математические функции --
# Fraction числа можно передавать как аргументы функций, ожидающих float. Тогда они будут преобразованы во float.
# К примеру, модуль math, оперирующий float числами, может работать и с Fraction числами.
from math import *

print(" Математические функции")
num1 = Fraction('1.44')
num2 = Fraction('0.523')
print(sqrt(num1))
print(sin(num2))
print(log(num1 + num2))
print()
# Важно понимать, что результатом работы функций модуля math являются float числа, а не Fraction.


# -- Свойства numerator и denominator --
# Для получения числителя и знаменателя Fraction числа используются свойства numerator и denominator.
print(" Свойства numerator и denominator")
num = Fraction('5/16')
print('Числитель дроби равен:', num.numerator)
print('Знаменатель дроби равен:', num.denominator)

# Метод as_integer_ratio(), который возвращает кортеж, состоящий из числителя и знаменателя данного Fraction числа.
num = Fraction('-5/16')
print(num.as_integer_ratio())
print()


# -- Метод limit_denominator() --
# Метод limit_denominator() возвращает самую близкую к данному числу рациональную дробь, чей знаменатель не превосходит переданного аргумента.
import math
print(" limit_denominator()")
print('PI =', math.pi)
num = Fraction(str(math.pi))        # Преобразуем π в дробь
print('No limit =', num)
for d in [1, 5,  50, 90, 100, 500, 1000000]:        # Ищем целое число, ближайшее к π:
    limited = num.limit_denominator(d)
    print(limited)
print()
# Метод limit_denominator() позволяет получить очень точные рациональные приближения иррациональных чисел, что очень удобно во многих математических задачах.

# Примечание 3. В Python нельзя совершать арифметические операции (+, -, *, /) между типами Decimal и Fraction.

# Тесты
from fractions import Fraction as F
from decimal import Decimal as D
print(" Тесты")
print('float and int: ', 12.7 + 2, type(12.7 + 2))
print('Fraction and int: ', F(10, 3) + 2, type(F(10, 3) + 2))
print('Fraction and Float:', F(10, 3) + 2.5678, type(F(10, 3) + 2.5678))
print('Decimal and int:', D('3.14') + 2, type(D('3.14') + 2))
#print('Decimal and float:', D('3.14') + 2.2, type(D('3.14') + 2.2))
#print('Decimal and Fraction:', D('3.14') + F(3, 2), type(D('3.14') + F(3, 2)))