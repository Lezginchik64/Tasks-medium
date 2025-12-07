import random
from string import *

# 1
letter = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

def generate_password(length):
    while True:
        s = "".join(random.sample(letter, length))
        if not (s.isupper() or s.islower() or s.isdigit() or s.isalpha()):
            return s


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')

# 2
chars1 = [c for c in ascii_uppercase if c not in 'OI']
chars2 = [c for c in ascii_lowercase if c not in 'ol']
chars3 = list(digits[2:])
chars = chars1 + chars2 + chars3


def generate_password(length):
    res = [random.choice(i) for i in (chars1, chars2, chars3)] + [random.choice(chars) for _ in range(3, length)]
    # добавляем в res по одному символу из каждого списка (chars1, chars2, chars3), а оставшиеся заполняем любыми символами из общего списка chars
    random.shuffle(res)
    return "".join(res)


def generate_passwords(count, length):
    res = set()
    while len(res) < count:
        res.add(generate_password(length))
    return list(res)


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')
