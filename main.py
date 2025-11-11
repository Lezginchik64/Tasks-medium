from copy import deepcopy

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
matrix1 = deepcopy(matrix)  # создаем копию матрицы

for k in range(m - 1):
    matrix2 = [[0 for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                matrix2[i][j] += matrix1[i][r] * matrix[r][j]
    matrix1 = deepcopy(matrix2)

for row in matrix1:
    print(*row)