import re

words = re.sub(r'[.,;:-?-!]', '', input().lower())
print(len(set(words.split())))
