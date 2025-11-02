# 1
n = int(input())
matrix = []
count = 0
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
    count += matrix[i][i]
print(count)


# 2
res = 0
for i in range(int(input())):
    res += int(input().split()[i])
print(res)