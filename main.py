n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]         # Переворачивает строки сверху вниз
                            # matrix[n - i - 1] - строка снизу (с конца)
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=" ")                # Транспонирование - меняет местами строки и столбцы.
    print()                                         # То есть matrix[j][i] вместо matrix[i][j].
