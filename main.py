n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

largest = matrix[0][0]                              # i >= j → значит под главной диагональю (включая её)
                                                    # i + j + 1 <= n → значит над побочной диагональю (включая её)
for i in range(n):                                  # i <= j → значит над главной диагональю (включая её).
    for j in range(n):                              # i + j + 1 >= n → значит под побочной диагональю (включая её).
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
print(largest)
