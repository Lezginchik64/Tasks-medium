n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
god = sum(x for x in matrix[0])
flag = True
all_num =[]

for row in matrix:                                  # создаем список всех чисел списка matrix, для дальнейшего сравнения
    all_num.extend(row)

for i in range(len(all_num)):                       # проверяем, что все числа разные и что числа в диапазоне 1..n²
    if all_num[i] < 1 or all_num[i] > n * n:
        flag = False
        break
    for j in range(i + 1, len(all_num)):            # Внутренний цикл j перебирает все элементы после i, сравниваем all_num[i] со всеми оставшимися элементами справа.
        if all_num[i] == all_num[j]:
            flag = False
            break
    if not flag:
        break

for row in matrix[1:]:                              # складываем строки и сравниваем с 1 строкой
    if sum(row) != god:
        flag = False
        break

for i in range(n):                                  # складываем столбцы и сравниваем с 1 строкой
    if sum(matrix[j][i] for j in range(n)) != god:
        flag = False
        break

first_diag_sum, second_diag_sum = 0, 0              # складываем главную и побочную диагонали и сравниваем с 1 строкой
for i in range(n):
    first_diag_sum += matrix[i][i]
    second_diag_sum += matrix[i][n - i - 1]

if first_diag_sum != god or second_diag_sum != god:
    flag = False

if flag:
    print("YES")
else:
    print("NO")
