def pascal(line):
    li = [1]
    for i in range(line):
        for j in range(len(li) - 1):
            li[j] = li[j] + li[j + 1]
        li.insert(0, 1)          # Добавляем 1 в начало
    return li
n = int(input())
for element in range(n):
    print(*pascal(element))