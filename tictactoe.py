# Задаю размер игрового поля. I set the size of the playing field
ROWS = 3
COLS = 3


# Создаю функцию прорисовки игрового поля с координатами. I create a function for drawing a playing field with coordinates
def board(matrix):
    print(" ", "0", "1", "2")
    for i in range(ROWS):
        for j in range(COLS):
            if j == 0:
                print(i, matrix[i][j], end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()


# Создаю функцию для хода с проверками правильности введенных координат. I create a function for the move with checks for the correctness of the entered coordinates
def enter(matrix, mark):
    while True:
        print('Ходит', mark, '. Введите координаты')
        index_1 = input('СТРОКА ')
        index_2 = input('КОЛОНКА ')
        if index_1 not in ("0", "1", "2") or index_2 not in ("0", "1", "2"):
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

# Создаю функцию проверки победителя. I am creating a function to check the winner
def win(matrix_ex):
    wincomb = [(matrix_ex[0][0],matrix_ex[0][1],matrix_ex[0][2]),
               (matrix_ex[1][0],matrix_ex[1][1],matrix_ex[1][2]),
               (matrix_ex[2][0],matrix_ex[2][1],matrix_ex[2][2]),
               (matrix_ex[0][0], matrix_ex[1][1], matrix_ex[2][2]),
               (matrix_ex[2][0], matrix_ex[1][1], matrix_ex[0][2]),
               (matrix_ex[0][0],matrix_ex[1][0],matrix_ex[2][0]),
               (matrix_ex[0][1],matrix_ex[1][1],matrix_ex[2][1]),
               (matrix_ex[0][2],matrix_ex[1][2],matrix_ex[2][2])]

    for i in range(len(wincomb)):
        if wincomb[i][0] !='-' and wincomb[i][0]==wincomb[i][1]==wincomb[i][2]:
            return wincomb[i][0]
    else:
        return False

# Даю входные параметры. I give the input parameters
matrix_ex = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']]

mark = 'X'
winner = None
step = 0
board(matrix_ex)

#Начинаем игру 
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


