n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrixB = [[int(i) for i in input().split()] for _ in range(m)]
matrixC = [[0] * k for _ in range(n)]

for i in range(n):              # идём по строкам первой матрицы, n - количество строк в первой матрице A.
    for j in range(k):          # идём по столбцам второй матрицы, количество столбцов второй матрицы B.
        for r in range(m):      # идём по элементам строки/столбца, m — это количество пар элементов, которые мы перемножаем. Количество столбцов A и строк B.
            matrixC[i][j] += matrixA[i][r] * matrixB[r][j]

for row in matrixC:
    print(*row)