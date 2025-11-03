n, m = int(input()), int(input())
mult = [print(*[str(i*j).ljust(3) for j in range(m)]) for i in range(n)]
