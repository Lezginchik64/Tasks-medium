set1, set2 = {int(x) for x in input().split()}, {int(x) for x in input().split()}
print(* sorted(set1 - set2))
# выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.