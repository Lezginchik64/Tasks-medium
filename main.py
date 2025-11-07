n, m = [int(i) for i in input().split()]
matrix = [[int(i) for i in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):                              # i + j - создаёт линейный сдвиг по строкам
        matrix[i][j] = (i + j) % m + 1              # % m - это цикличность, идет по кругу. % m + 1 - добавляем 1, чтобы получить диапазон от 1 до m

for res in matrix:
    print(*[str(i).ljust(3) for i in res])
