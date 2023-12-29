matrix_ex = [
      [' ', 0, 1, 2]
    , [0, '-', '-', '-']
    , [1, '-', '-', '-']
    , [2, '-', '-', '-']]
ROWS = 4
COLS = 4

def win(matrix):
    w = ''
    g, g_1, g_2 = [], [], []
    v, v_1, v_2 = [], [], []
    d_1, d_2 = [], []
    for row in matrix:
        v.append(row[1])
        v_1.append(row[2])
        v_2.append(row[3])

    g = matrix[1][:]
    g_1 = matrix[2][:]
    g_2 = matrix[3][:]

    d_1 = [matrix[1][1], matrix[2][2], matrix[3][3]]
    d_2 = [matrix[-2][-2], matrix[-3][-3], matrix[-4][-4]]
    x = ['X', 'X', 'X']
    n = ['O', 'O', 'O']
    if any([g == x,
            g_1 == x,
            g_2 == x,
            d_1 == x,
            d_2 == x,
            v == x,
            v_1 == x,
            v_2 == x]):
        w = 'X'
    elif g == n or g_1 == n or g_2 == n or d_1 == n or d_2 == n or v == n or v_1 == n or v_2 == n:
        w = 'O'
    return w


cnt = 1
while win(matrix_ex) == '':

    if cnt % 2 == 0:
        print('Ходит 0. Введите ячейку')
        index_1 = int(input('СТРОКА'))
        index_2 = int(input('КОЛОНКА'))
        matrix_ex[index_1+1][index_2+1] = 'O'
        cnt += 1
    else:
        print('Ходит X. Введите ячейку')
        index_1 = int(input('СТРОКА'))
        index_2 = int(input('КОЛОНКА'))
        matrix_ex[index_1+1][index_2+1] = 'X'
        cnt += 1  # print(f'игра окончена,{w} победил')
    if cnt == 10:
        break
    for i in range(ROWS):
        for j in range(COLS):
            print(matrix_ex[i][j], end=' ')
        print()
if win(matrix_ex) != '':
    print(f'Игра окончена,{win(matrix_ex)} победил')
else:
    print('Ничья')
for i in range(ROWS):
    for j in range(COLS):
        print(matrix_ex[i][j], end=' ')
    print()