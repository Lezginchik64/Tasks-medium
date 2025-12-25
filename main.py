# 1
num = [int(i) for i in input().split()]  # на входе список чисел


def func(n):
    return sum([int(i) for i in str(n)])  # распаковываем число: число 12 делаем строкой, чтобы разделить. Затем каждую строку обратно в число и суммируем.


num.sort(key=func)
print(*num)

# 2
l = input().split()  # на входе строка


def func2(n):
    return sum([int(i) for i in n])  # sum() на вход получает любой объект, по которому можно итерировать (список, кортеж, множество, словарь и т.д.)


l.sort(key=func2)
print(*l)
