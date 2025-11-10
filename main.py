# 1
n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrixB = [[int(i) for i in input().split()] for _ in range(n)]
matrixC = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]

for row in matrixC:
    print(*row)

# 2
n, m = [int(i) for i in input().split()]
matrix_1 = [input().split() for i in range(n)]
input()
matrix_2 = [input().split()  for j in range(n)]
matrix_3 = []

for i in range(n):
    row = []
    for j in range(m):
        matrix_3_el = int(matrix_1[i][j]) + int(matrix_2[i][j])
        row.append(matrix_3_el)
    matrix_3.append(row)

for el in matrix_3:
    print(*el)