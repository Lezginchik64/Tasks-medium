# 1
sets = [set(input()) for i in range(int(input()))]      # делаем каждую введенную строку множеством и кладем в список sets
general = sets[0]                       # берем первый элемент списка sets, для дальнейшего сравнения с ним
for i in range(1, len(sets)):
    general = general & sets[i]
print(*sorted(general))

# 2
n = int(input())
numbers = [input() for _ in range(n)]

num_set = set(numbers[0]).intersection(*numbers)        # Метод .intersection() преобразует каждую строку в множество символов. Каждый аргумент автоматически превращается во множество.
print(*sorted(num_set))                                     # Пересечение множества самого с собой не меняет ничего. A ∩ A = A