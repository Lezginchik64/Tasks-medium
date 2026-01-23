# 1
with open('output.txt', 'w', encoding='utf-8') as f, open('input.txt', 'r', encoding='utf-8') as line:
    for ind, val in enumerate(line):
        f.writelines(f"{ind + 1}) {val}")

# 2
with open('output.txt', 'w', encoding='utf-8') as f, open('input.txt', 'r', encoding='utf-8') as line:
    for ind, val in enumerate(line, start=1):
        print(f"{ind + 1}) {val}", end="", file=f)