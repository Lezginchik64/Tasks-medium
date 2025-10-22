#Вариант 1
n = [int(x) for x in input().split()]

for i in range(1, len(n)):
    n[0], n[i] = n[i], n[0]
print(*n)

#Вариант 2
n = [int(x) for x in input().split()]

for i in range(len(n) - 1, 0, -1 ):
    n[i], n[i - 1] = n[i - 1], n[i]
print(*n)

#Вариант 3
seq = input().split()
new_seq = [seq[-1]] + seq[:-1]

print(*new_seq)