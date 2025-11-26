d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
text = input().upper()
for letter in text:                              # достаем буквы из введенного текста
    for key, values in d.items():
        if letter in values:                     # проверяем есть ли буква в значениях словаря
            pos = values.index(letter) + 1       # определяем позицию буквы в значениях словаря, +1 - чтобы отсчет был от 1
            print(key * pos, end="")
