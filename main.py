import random

# 1
numbers = random.sample([i for i in range(1, 76)], 25)
bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
bingo[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3), end=' ')
    print()
print()

# 2
l = [i for i in range(1, 76)]  # создаем список для заполнения матрицы
sample = random.sample(l, 24)  # перемешиваем список, и выбираем 24 случайных уникальных числа
matrix = [[0] * 5 for row in range(5)]  # создаем матрицу и заполняем нулями
index = 0  # счетчик для перебора по списку sample

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == 2 and j == 2:  # центральное значение == 0
            matrix[i][j] == 0
        else:
            matrix[i][j] = sample[index]
            index += 1

for res in matrix:
    print(*[str(i).ljust(3) for i in res])
