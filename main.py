from random import shuffle

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

flat = [x for row in matrix for x in row]       # Делаем список из всех элементов
shuffle(flat)                                   # перемешиваем список

new_matrix = [flat[i:i+4] for i in range(0, 16, 4)]    # собираем обратно в матрицу 4×4
print(new_matrix)       # range(0, 16, 4) - индексы начала строк: 0, 4, 8, 12
                        # flat[i:i+4]   -  flat[0:4],
#                                          flat[4:8],
#                                          flat[8:12],
#                                          flat[12:16]