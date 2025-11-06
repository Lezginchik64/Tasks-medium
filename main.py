# 1
n, m = [int(x) for x in input().split()]
matrix = [[int(i) for i in range(m)] for _ in range(n)]
count = 1

for j in range(m):
    for i in range(n):
        matrix[i][j] = count
        count += 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])

# 2
n, m = [int(x) for x in input().split()]
matrix = [[j * n + i + 1 for j in range(m)] for i in range(n)]          # j * n + i + 1 — формула, номер = (сколько элементов в предыдущих столбцах) + (позиция внутри текущего столбца) + 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])