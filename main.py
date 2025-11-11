def square_matrix_mult(matrixA, matrixB, size):
    matrixC = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for q in range(size):
                matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
    return matrixC


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
powered_matrix = matrix.copy()

for _ in range(m - 1):
    powered_matrix = square_matrix_mult(matrix, powered_matrix, n)

for row in powered_matrix:
    print(*row)