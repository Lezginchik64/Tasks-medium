#1
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

average_values = [sum(tup) / len(tup) for tup in numbers]
print(average_values)

# 2
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
list_num = []
for i in numbers:
    i = list(i)
    average = sum(i) / len(i)
    list_num.append(average)
print(list_num)
