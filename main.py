# Способ 1
n, m = int(input()), int(input())
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        word = input()
        row.append(word)
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# Способ 2
n, m = int(input()), int(input())

[print(*[input() for i in range(m)]) for i in range(n)]

