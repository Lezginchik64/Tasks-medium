# 1
a = [input().lower() for i in range(int(input()))]
for i in a:
    print(len(set(i)))

# 2
for i in range(int(input())):
    print(len(set(input().lower())))