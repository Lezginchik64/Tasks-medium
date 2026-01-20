import random

with open('first_names.txt') as names, open('last_names.txt') as surnames:
    name = [line.strip() for line in names]
    surname = [line.strip() for line in surnames]
    print(random.choice(name), random.choice(surname))
    print(random.choice(name), random.choice(surname))
    print(random.choice(name), random.choice(surname))
