a, b, c = [set(input().split()) for _ in range(3)]
d = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
print(*sorted(list(d - (a | b | c)), key=int))
