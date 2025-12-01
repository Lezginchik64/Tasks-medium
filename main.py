# 1
d = {}
for _ in range(int(input())):
    key, value = input().split()
    d[key], d[value] = value, key       # словарь заполняется ключами с значениями, затем переворачивает и добавляет еще раз:
print(d[input()])                       # {'Awful': 'Terrible', 'Terrible': 'Awful', 'Beautiful': 'Pretty', 'Pretty': 'Beautiful'}

# 2
d = {}
for _ in range(int(input())):
    key, value = input().split()
    d[key] = value

res = input()
for i in d:
    if i == res:
        print(d[i])
        break
    elif d[i] == res:
        print(i)
        break