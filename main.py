n, m = [int(x) for x in input().split()]
matrix = [['*'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            matrix[i][j] = '.'

for row in matrix:
    print(*row)
