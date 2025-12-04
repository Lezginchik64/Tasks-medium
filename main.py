import random

# 1
length = int(input())
for _ in range(length):
    if random.randint(0,1):    # if random.randint(0,1) - если выпадает 1, то это True и выполняется условие if, если 0, то False и выполняется else.
        print(chr(random.randint(65, 90)), end="")
    else:
        print(chr(random.randint(97, 122)), end="")
print()

# 2
length = int(input())
password = ''
for _ in range(length):
    password += [chr(random.randint(65, 90)), chr(random.randint(97, 122))][random.randint(0, 1)]
print(password)     # выбираются 2 буквы, потом рандомно выпадает 0 или 1 - это позиция в списке, 0 - первый элемент списка (1 буква), 1 - второй элемент списка (2 буква).