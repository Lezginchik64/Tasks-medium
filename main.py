is_non_negative_num = lambda x: x.replace('.', '', 1).isdigit()        # isdigit - будет всегда возвращать False если число отрицательное.
print(is_non_negative_num('10.34ab'))                           # x.replace('.', '', 1) - заменяет точку на пустое один раз
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))