# 1
with open('population.txt') as f:
    for line in f:
        n, p = line.split('\t')
        if n[0] == ('G') and int(p) > 500_000:
            print(n)

# 2
with open('population.txt') as f:
    lines = [line.strip().split('\t') for line in f if line[0][0].lower() == 'g']
    res = list(filter(lambda x: int(x[-1]) > 500_000, lines))
    for i in res:
        print(i[0])
