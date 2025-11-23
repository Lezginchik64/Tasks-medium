# 1
a, b, c = [set(input().split()) for _ in range(3)]
print(*sorted(list(c - (a | b)), key=int, reverse=True))

# 2
a, b, c = [set(input().split()) for _ in range(3)]
print(*sorted(list(c - b - a), key=int, reverse=True))