# 1
abscissas, ordinates, applicates = (map(float, input().split()) for _ in range(3))
print(all(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= 4, zip(abscissas, ordinates, applicates))))

# 2
abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]

num = list(zip(abscissas, ordinates, applicates))
res = all(x ** 2 + y ** 2 + z ** 2 <= 4 for x, y, z in num)
print(res)
