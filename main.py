import random

# 1
r = list(input())
random.shuffle(r)
print(''.join(r))

# 2
anagram = input()
print(''.join(random.sample(anagram, len(anagram))))
