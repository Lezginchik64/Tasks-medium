n = [int(i) for i in input().split()]
s = set()
for i in n:
    if i in s:
        print("YES")
    else:
        print("NO")
        s.add(i)
