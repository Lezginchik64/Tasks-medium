with open('text.txt', encoding='utf-8') as file:
    print(file.read()[::-1])