s = input()
zap = "запретил"
buk = "букву"
world = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for i in world:                             # i - буква из словаря world
    if i in s or i in buk or i in zap :     # если буква встречается в s, zap, buk
        parts = [s, zap, buk, i]
        print(' '.join(p for p in parts if p))      # Он перебирает все элементы из parts
                                                    # и берёт только те элементы, которые не пустые — то есть if p проверяет, что строка не "".
        s = s.replace(i, "")
        zap = zap.replace(i, "")
        buk = buk.replace(i, "")
