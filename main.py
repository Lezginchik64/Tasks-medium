s = input()
first = {i: s.count(i) for i in s}

second = {}
for _ in range(int(input())):
    a, b = input().split(": ")
    second[int(b)] = a

for i in s:
    print(second[first[i]], end="")     # first[i] — узнаём, сколько раз эта буква встречается в слове.
                                        # second[first[i]] — по этой частоте берём настоящую букву.