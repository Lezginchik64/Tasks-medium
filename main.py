# 1
def mean(*args):
    n = [i for i in args if type(i) == int or type(i) == float]
    return sum(n) / len(n) if n else 0.0


# 2
def mean(*args):
    args = [float(i) for i in args if type(i) in (int, float)]
    if len(args) > 0:
        return sum(args) / len(args)
    else:
        return 0.0


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
