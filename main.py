# Перебор элементов матрицы
rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов

matrix  = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
print()

# Методы ljust()
# Строковый метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста.
print('a'.ljust(5, '*'))
print('ab'.ljust(5, '$'))
print('abc'.ljust(5, '#'))
print()

# Метод rjust()
# Строковый метод rjust() выравнивает текст по ширине, добавляя пробелы в начало текста.
print('a'.rjust(5, '*'))
print('ab'.rjust(5, '$'))
print('abc'.rjust(5, '#'))
print()

rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()
print()


# Квадратные матрицы
# Матрица с одинаковым количеством строк и столбцов называется квадратной. У квадратной матрицы есть две диагонали:
# главная: проходит из верхнего левого в правый нижний угол матрицы;
# побочная: проходит из нижнего левого в правый верхний угол матрицы.

n = 8
matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8

for i in range(n):                    # заполняем главную диагональ единицами, а побочную двойками
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2

for r in range(n):                    # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
print()

# Примечания

# Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:
def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

# Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)