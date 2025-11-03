n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

up, right, down, left = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            up += matrix[i][j]
        elif i < j and i > n - 1 - j:
            right += matrix[i][j]
        elif i > j and i > n - 1 - j:
            down += matrix[i][j]
        elif i > j and i < n - 1 - j:
            left += matrix[i][j]

print("Верхняя четверть:", up)
print("Правая четверть:", right)
print("Нижняя четверть:", down)
print("Левая четверть:", left)
