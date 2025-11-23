a, b, c = [set(input().split()) for _ in range(3)]
print(*sorted(list((a | b | c) - (a & b & c)), key=int))
# a | b | c - cумма всех сетов
# a & b & c - элементы, которые есть во всех 3 сетах