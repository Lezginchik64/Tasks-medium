file = open(r'/Users/lezginchik/Downloads/nums.txt')

# 1
lines = file.read().split()
print(sum(map(int, lines)))

# 2
lines = [i.strip() for i in file if i.strip()]
print(sum(map(int, lines)))

file.close()
