n = int(input())
a = [int(input()) for _ in range(n)]
target = int(input())
flag = False

for i in range(n):
    for j in range(i + 1, n):
        if a[i] * a[j] == target:
            flag = True

if flag:
    print("ДА")
else:
    print("НЕТ")
