# 1
with open("asd.txt") as file:
    max_len, res = 0, []
    for line in file:
        if len(line) > max_len:
            max_len, res = len(line), [line]    # res = [line] создает новый список, содержащий только одну строку line.
        elif len(line) == max_len:
            res.append(line)
print(''.join(res))

# 2
with open("asd.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    maxline = len(max(lines, key=len))
    print(*filter(lambda x: len(x) == maxline, lines), sep="\n")

# 3
with open("lines.txt") as file:
    mline = len(max(file.readlines(), key=len))
    file.seek(0)  # курсор на начало
    for line in file.readlines():
        if len(line) == mline:
            print(line.strip())
