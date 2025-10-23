n = [int(x) for x in input().split()]
count = 1
for i in range(1, len(n)):
    if n[i] != n[i - 1]:
        count += 1
print(count)
