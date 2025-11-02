n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
    average = sum(temp) / len(temp)                     # sum(temp) - сумма всех элементов строки, len(temp) - количество элементов в строке
    count = 0
    for j in temp:
        if j > average:
            count += 1
    print(count)



