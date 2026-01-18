# 1
with open("asd.txt") as file:
    row = ''.join(i if i.isdigit() else " " for i in file.read())
    print(sum(map(int, row.split())))

# 2
with open("asd.txt") as file:
    lines = file.read()
    for i in filter(lambda x: not x.isdigit(), lines):
        lines = lines.replace(i, " ")
    print(sum(map(int, lines.split())))
