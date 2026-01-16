file = open(r'/Users/lezginchik/Downloads/numbers.txt')
# 1
print(sum(map(int, file)))
# 2
lines = file.readlines()
print(int(lines[0]) + int(lines[1]))

file.close()
