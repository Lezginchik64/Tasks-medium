# Вариант 1
s = input()
a = []
for i in range(len(s), 0, -3):
    a.append(s[max(0, i - 3):i])
a.reverse()
res = ",".join(a)
print(res)

# Вариант 2
num = input()
for idx in range(len(num) - 3, 0, -3):
    num = num[:idx] + ',' + num[idx:]
print(num)

# Вариант 3
print("{:,}".format(int(input())))
