xy = input()
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])
matrix = [["."]*8 for i in range(8)]
matrix[y][x] = 'N'
                                          # (y-i) — разница по вертикали между клеткой коня (y) и текущей клеткой (i) на доске.
for i in range(8):                          # (x-j) — разница по горизонтали между клеткой коня (x) и текущей клеткой (j).
    for j in range(8):                      # (y-i)**2 + (x-j)**2 — это квадрат расстояния по теореме Пифагора.
        if (y-i)**2 + (x-j)**2 == 5:
            matrix[i][j] = "*"

for row in matrix:
    print(*row)
