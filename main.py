n, m = [int(x) for x in input().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]
count = 1
                                    # самая маленькая сумма индексов — когда (i = 0, j = 0) → 0
for s in range(n + m - 1):          # самая большая — когда (i = n − 1, j = m − 1) → (n − 1) + (m − 1) = n + m − 2
    for i in range(n):              # Значит, диагонали имеют номера от 0 до n + m − 2.
        for j in range(m):          # кол-во диагоналей = (n + m - 2) - 0 + 1 = n + m - 1
            if i + j == s:           # +1 нужен, чтобы включить первую диагональ с индексом 0.
                matrix[i][j] = count         # А всего их n + m - 1.  Поэтому в коде for s in range(n + m - 1).
                count += 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])
