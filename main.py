from math import sin, sqrt


# 1
def f1(p):
    def f2(n):
        return n ** p

    return f2


n = int(input())
commands = {'квадрат': f1(2), 'куб': f1(3), 'корень': f1(0.5), 'модуль': abs, 'синус': sin}
print(commands[input()](n))  # эквивалент этой записи - f1(2)(n)


# 2
def func(n, p):
    return {'квадрат': n ** 2, 'куб': n ** 3, 'корень': n ** 0.5, 'модуль': abs(n), 'синус': sin(n)}[p]  # print(func(5, "квадрат"))

print(func(int(input()), input()))


# 3
def f1(num):
    return num ** 2


def f2(num):
    return num ** 3


def f3(num):
    return sqrt(num)


def f4(num):
    return abs(num)


def f5(num):
    return sin(num)


n = int(input())
commands = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5}
s = input()
if s in commands:
    print(commands[s](n))
