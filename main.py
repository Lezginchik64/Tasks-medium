# 1
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i]     # if i - Если i не пустое, не ноль и т.д

print(non_empty_tuples)

# 2
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = []
for i in tuples:
    if len(i) != 0:
        non_empty_tuples.append(i)
print(non_empty_tuples)
