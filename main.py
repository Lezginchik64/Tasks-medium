def add3(x):
    return x + 3


def mul7(x):
    return x * 7


# 1
def func_apply(func, items):
    return [func(item) for item in items]


# 2
def func_apply(func, items):
    res = []
    for item in items:
        res.append(func(item))
    return res


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))
