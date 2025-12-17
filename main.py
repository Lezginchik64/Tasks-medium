def print_products(*args):
    r = [i for i in args if type(i) is str and len(i) > 0]
    if len(r) > 0:
        count = 0
        for i in r:
            count += 1
            print(f'{count}) {i}')
    else:
        print("Нет продуктов")


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
