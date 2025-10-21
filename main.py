n = int(input())
count = [0, 0, 0, 0]
names = ['Первая четверть:', 'Вторая четверть:',
         'Третья четверть:', 'Четвертая четверть:']

for _ in range(n):
    x, y = [int(num) for num in input().split()]
    if x > 0 and y > 0:
        count[0] += 1
    elif x < 0 and y > 0:
        count[1] += 1
    elif x < 0 and y < 0:
        count[2] += 1
    elif x > 0 and y < 0:
        count[3] += 1

for i in range(4):
    print(names[i], count[i])