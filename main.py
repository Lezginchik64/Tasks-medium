n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

largest = matrix[0][0]
for i in range(n):
    for j in range(n):
        if i >= j and matrix[i][j] > largest:      # сравниваем элементы главной диагоналии всего нижнего левого угла, начиная с largest
            largest = matrix[i][j]
print(largest)