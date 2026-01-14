def check(num):
    return all(map(lambda x: int(x) and num % int(x) == 0, str(num)))


a = [i for i in range(int(input()), int(input()) + 1)]
print(*list(filter(lambda x: check(x), a)))
