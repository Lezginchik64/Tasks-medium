# 1
def anagramm(word):
    d = {}
    for i in word.lower():
        if i.isalpha():
            d[i] = d.get(i, 0) + 1
    return d

print("YES" if anagramm(input()) == anagramm(input()) else "NO")


# 2
first = {}
for i in input().lower():
    if i in ".,!?:;- ":
        continue
    else:
        first[i] = first.get(i, 0) + 1

second = {}
for i in input().lower():
    if i in ".,!?:;- ":
        continue
    else:
        second[i] = second.get(i, 0) + 1

print("YES" if first == second else "NO")
