n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[i][n - i - 1] = 1
    for j in range(n - i, n):           # n - i - это значит правее побочной диагонали, пишем без -1, чтобы сама диагональ не изменялась
        matrix[i][j] = 2

for row in matrix:
    print(*row)
