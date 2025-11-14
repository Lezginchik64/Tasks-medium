n = int(input())
f1 = f2 = f3 = 1
for _ in range(n):
    print(f1, end=' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3
