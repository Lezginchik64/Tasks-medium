# 1
with open('file.txt') as f:
    txt = f.read()
    print('Input file contains:')
    print(sum(map(str.isalpha, txt)), 'letters')  # letters
    print(len(txt.split()), 'words')  # words
    print(txt.count('\n') + 1, 'lines')  # lines

# 2
with open("file.txt") as file:
    letters, words, lines = 0, 0, 0
    for line in file:
        lines += 1  # lines
        chars = list(line.strip())
        letters_list = list(filter(lambda x: x.isalpha(), chars))
        letters += len(letters_list)  # letters
        words += len(line.strip().split())  # words

print(f"Input file contains:\n{letters} letters\n{words} words\n{lines} lines ")
