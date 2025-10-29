n = int(input())

li = [1]
for _ in range(n):
    for j in range(len(li) - 1):
        li[j] = li[j] + li[j + 1]
    li.insert(0, 1)          # Добавляем 1 в начало

print(li)
