first = {}
for i in input():
    first[i] = first.get(i, 0) + 1

second = {}
for i in input():
    second[i] = second.get(i, 0) + 1

print("YES" if first == second else "NO" )      # сравниваем словари, они сравниваются по ключам и значениям
