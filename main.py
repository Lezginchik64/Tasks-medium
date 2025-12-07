import random

friends = [input() for i in range(int(input()))]
random.shuffle(friends)

for i in range(len(friends)):
    print(f"{friends[i]} - {friends[i - 1]}")
