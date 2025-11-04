n = int(input())
matrix = [input().split() for _ in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break
    if not flag:
        break

if flag:
    print("YES")
else:
    print("NO")
