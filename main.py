n, m = [int(x) for x in input().split()]
matrix = [[i * m + j + 1 for j in range(m)] for i in range(n)]

for i in range(n):
    if i % 2:                       # только для нечётных строк
        matrix[i].reverse()

for row in matrix:
    print(*[str(x).ljust(3) for x in row])
