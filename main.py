n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]   # matrix[n - i - 1][i] - обмен главной и диагонали, отражённой относительно горизонтальной оси.
                                # matrix[i][n - i - 1] - обмен главной и диагонали, отражённой относительно вертикальной оси.
for row in matrix:
    print(*row)
