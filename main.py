import random

file = open('asd.txt')
lines = [line.strip() for line in file.readlines() if line.strip()]
print(random.choice(lines))

file.close()
