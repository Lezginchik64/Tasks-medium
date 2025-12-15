# 1
def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    res = [[value]*m for _ in range(n)]
    return res

# 2
def matrix2(n=1, m=None, value=0):
    if m is None:
        m = n
    res = [[value for _ in range(m)] for _ in range(n)]
    return res

print(matrix(3, 4, 4))
print(matrix2(3, 4, 4))
