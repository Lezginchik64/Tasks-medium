# 1
n, m = [int(x) for x in input().split()]
matrix = [[int(i) for i in range(m)] for _ in range(n)]
count = 1

for i in range(n):
    for j in range(m):
        matrix[i][j] = count
        count += 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])

# 2
n, m = [int(x) for x in input().split()]
matrix = [[i * m + j + 1 for j in range(m)] for i in range(n)]          # i * m + j + 1 — формула, чтобы считать элементы подряд

for row in matrix:
    print(*[str(x).ljust(3) for x in row])