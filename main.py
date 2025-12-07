import random
from string import *

letter = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
# преобразуем в set для возможности сложения и вычитания набора символов. | - сложение


def generate_password(length):
    return "".join(random.sample(letter, length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

# def generate_passwords(count, length):
#     passwords = []
#     for i in range(count):
#         password = "".join(random.sample(letter, length))
#         passwords.append(password)
#     return "\n".join(passwords)


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')
