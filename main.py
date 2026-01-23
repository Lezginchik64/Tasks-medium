import random

with open('output.txt', 'w', encoding='utf-8') as f:
    for i in range(25):
        f.write(str(random.randrange(111, 778)) + '\n')