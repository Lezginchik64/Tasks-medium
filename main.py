file = open(r'/Users/lezginchik/Downloads/prices.txt')

lines = [line.split('\t') for line in file]
# 1
res = sum(map(lambda x: int(x[1]) * int(x[2]), lines))
# 2
res2 = sum([int(i[1]) * int(i[2]) for i in lines])

print(res)
print(res2)

file.close()
