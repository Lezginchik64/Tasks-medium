# 1
with open("asd.txt", encoding='utf-8') as file:
    print(*file.readlines()[::-1], sep=" ")

# 2
with open("asd.txt") as file:
    for line in file.readlines()[::-1]:
        print(line.strip())
