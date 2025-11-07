# 1
n = int(input())
matrix = [[0] * n for _ in range(n)]                # i <= j — значит над или на главной диагонали
                                                    # i >= j — значит под или на главной диагонали
for i in range(n):                                  # На побочной диагонали всегда i + j + 1 == n.
    for j in range(n):                              # Если меньше (< n) → это верхняя часть над побочной диагональю.
        if (i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n):      # Если больше (> n) → это нижняя часть под ней.
            matrix[i][j] = 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])

# 2
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):                                              # Побочная диагональ: i == n - 1 - j -> i + 1 + j == n
    for j in range(n):
        if i == j or i == n - 1 - j or (i < j and i < n - 1 - j) or (i > j and i > n - 1 - j):
            matrix[i][j] = 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])