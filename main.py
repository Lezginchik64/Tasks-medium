a = [input().lower() for _ in range(int(input()))]
b = ''.join(a)
print(len(set(b)))