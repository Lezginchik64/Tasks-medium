# 1
n = int(input())
matrix = [input().split() for _ in range(n)]

for row in reversed(matrix):
    print(*row)

# 2
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
                            # matrix[n - i - 1] - строка снизу (с конца)
for row in matrix:
    print(*row)
