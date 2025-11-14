n = int(input())
students = [tuple(input().split()) for _ in range(n)]
for res in students:
    print(*res)
print()
for name, grade in students:
    if int(grade) > 3:
        print(name, grade)
