# 1
with open("asd.txt") as file:
    for line in file:
        print(sum(map(int, line.split())))

# 2
with open("asd.txt") as file:
    for line in file:
        line = [int(i) for i in line.strip().split()]
        print(sum(line))
