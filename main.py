result = []
for _ in range(int(input())):
    res = []
    for _ in range(int(input())):
        res.append(any(map(lambda x: x == "5", input().split())))   # есть ли ученики с 5 вообще
    result.append(any(res))     # в каждом ли классе есть ученики с 5
print("YES" if all(result) else "NO")   # если во все классах есть ученики с 5, выводим YES
