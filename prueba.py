import numpy as np


def create_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)
    return np.array(board)


def win(board, player):
    # rows
    for x in range(3):
        win = True
        for y in range(3):
            if board[x, y] != player:
                win = False
                continue
        if win:
            return win

    # columns
    for x in range(3):
        win = True
        for y in range(3):
            if board[y][x] != player:
                win = False
                continue
        if win:
            return win

    # diagonals
    win = True
    if board[0][0] != player or board[1][1] != player or board[2][2] != player:
        win = False
    if win:
        return win

    win = True
    if board[0][2] != player or board[1][1] != player or board[2][0] != player:
        win = False
    return win


def msg_to_array(msg):
    arr = np.array(list(msg))
    return np.reshape(arr, (3, 3))


def display_board(arr):
    table = ". 0| 1 | 2 \n0  |   |   \n---+---+---\n1  |   |   \n---+---+---\n2  |   |   "
    pos = [14, 17, 21, 38, 41, 45, 62, 65, 69]
    tmp = list(table)
    index = 0
    for x in range(3):
        for y in range(3):
            if arr[x][y] != '-':
                tmp[pos[index]] = arr[x][y]
            else:
                tmp[pos[index]] = ' '
            index += 1
    table = "".join(tmp)
    print(table)


def results(board):
    winner = 0
    for player in ['o', 'x']:
        if win(board, player):
            winner = player
    if np.all(board != '-') and winner == 0:
        winner = -1
    return winner


def election(board):
    display_board(board)
    cord = input("Ingrese su jugada (x,y): ")
    cord = list(map(int, cord.split(',')))
    while board[cord[0]][cord[1]] != '-':
        cord = input("Jugada no valida ingrese su jugada nuevamente (x,y): ")
        cord = list(map(int, cord.split(',')))
    board[cord[0]][cord[1]] = 'o'


def array_to_msg(board):
    msg = ''
    for x in board:
        for y in x:
            msg += y
    return msg

# menu_1 = """- Seleccione una opcion\n1-Jugar\n2-Salir"""
# print(results(msg_to_array("---------")))


array_to_msg(msg_to_array("xx-------"))
