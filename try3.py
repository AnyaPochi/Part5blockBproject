# Задаю размер игрового поля
ROWS = 3
COLS = 3


# Создаю функцию прорисоки игрового поля с координатами
def board(matrix):
    print(" ", "0", "1", "2")
    for i in range(ROWS):
        for j in range(COLS):
            if j == 0:
                print(i, matrix[i][j], end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()


# Создаю функцию для хода с проверками правильности введенных координат
def enter(matrix, mark):
    while True:
        print('Ходит', mark, '. Введите координаты')
        index_1 = input('СТРОКА ')
        index_2 = input('КОЛОНКА ')
        if index_1 not in '012' or index_2 not in '012':
            print('Вы ввели неверные координаты, попробуйте еще раз')
            continue
        else:
            index_1, index_2 = int(index_1), int(index_2)
            if matrix[index_1][index_2] == '-':
                matrix[index_1][index_2] = mark
                break
            else:
                print('Ячейка занята, попробуйте еще раз')
                continue


# Создаю функцию проверки победителя
def win(matrix):
    w = ''
    g, g_1, g_2 = [], [], []
    v, v_1, v_2 = [], [], []
    d_1, d_2 = [], []
    for row in matrix:
        v.append(row[0])
        v_1.append(row[1])
        v_2.append(row[2])

    g = matrix[0][:]
    g_1 = matrix[1][:]
    g_2 = matrix[2][:]
    d_1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    d_2 = [matrix[2][0], matrix[1][1], matrix[0][2]]
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


# Даю входные параметры и начинаем игру
matrix_ex = [
    ['-', '-', '-']
    , ['-', '-', '-']
    , ['-', '-', '-']]

mark = 'X'
winner = None
step = 0
board(matrix_ex)
while True:
    step += 1
    if step % 2 == 0:
        player = 'O'
    else:
        player = 'X'
    enter(matrix_ex, player)
    board(matrix_ex)
    winner = win(matrix_ex)

    if winner:
        print('Выйграл', winner, '! Игра окончена!')
        break
    if step == 9:
        print('Ничья!')
        break

# Ниже неудачная попытка реализовать поиск победителя через индексы выйгрышных комбинаций.Прошу помочь найти ошибку.
# Оставила свой в самой программе свой изначальный способ, потому что работает и не громоздко выглядит)

# wincomb = [(matrix_ex[0][0],matrix_ex[0][1],matrix_ex[0][2])
#            ,(matrix_ex[1][0],matrix_ex[1][1],matrix_ex[1][2])
#            ,(matrix_ex[2][0],matrix_ex[2][1],matrix_ex[2][2])
#            ,(matrix_ex[0][0], matrix_ex[1][1], matrix_ex[2][2])
#            ,(matrix_ex[2][0], matrix_ex[1][1], matrix_ex[0][2])
#            ,(matrix_ex[0][0],matrix_ex[1][0],matrix_ex[2][0])
#            ,(matrix_ex[0][1],matrix_ex[1][1],matrix_ex[2][1])
#            ,(matrix_ex[0][2],matrix_ex[1][2],matrix_ex[2][2])]
#
# def win():
#     for i in range(len(wincomb)):
#         if wincomb[i][0] !='-' and wincomb[i][0]==wincomb[i][1]==wincomb[i][2]:
#             return wincomb[i][0]
#     else:
#         return False
