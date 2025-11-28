lst = [word.strip('.,!?:;-') for word in input().lower().split()]
d = {lst.count(i): i for i in (sorted(lst, reverse=True))}
print(d[min(d)])        # d[min(d)] — берёт значение словаря с этим ключом: d[1] → 'world'
