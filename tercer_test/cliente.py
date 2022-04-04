import socket as skt
import numpy as np

ADDRESS = 'localhost'
SERVER_PORT = 5001
FORMAT = 'utf-8'
DISP_MSG = 'DISP'
CLOSE_MSG = 'CLOSE'
CLOSING_MSG = 'CLOSING'


def create_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)
    return np.array(board)


def msg_to_array(msg):
    arr = np.array(list(msg))
    return np.reshape(arr, (3, 3))


def array_to_msg(board):
    msg = ''
    for x in board:
        for y in x:
            msg += y
    return msg


def election(board):
    display_board(board)
    cord = input("Ingrese su jugada (x,y): ")
    cord = list(map(int, cord.split(',')))
    while board[cord[0]][cord[1]] != '-':
        cord = input("Jugada no valida ingrese su jugada nuevamente (x,y): ")
        cord = list(map(int, cord.split(',')))
    board[cord[0]][cord[1]] = 'o'


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


serverSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
serverSocket.connect((ADDRESS, SERVER_PORT))

while True:
    print("--------Bienvenido al Juego--------")
    sel = ''
    while sel not in ['1', '2']:
        sel = input("- Seleccione una opcion\n1-Jugar\n2-Salir\n>>")

    if sel == "1":
        serverSocket.send(DISP_MSG.encode(FORMAT))
        response = serverSocket.recv(1024).decode(FORMAT)
        print(f"respuesta de disponibilidad:  {response}")
        if response == "OK":
            print("--------Comienza el Juego--------")
            board = create_board()
            while True:
                election(board)
                print("==============================")
                serverSocket.send(array_to_msg(board).encode(FORMAT))
                msg = serverSocket.recv(1024).decode(FORMAT)
                if len(msg) > 9:
                    winner = msg[9]
                    msg = msg[:-1]
                    board = msg_to_array(msg)
                    display_board(board)
                    if winner == 'o':
                        print('Felicidades Ganeste!')
                    else:
                        print('Has Perdido')
                    break
                board = msg_to_array(msg)

    else:
        serverSocket.send(CLOSE_MSG.encode(FORMAT))
        response = serverSocket.recv(1024).decode(FORMAT)
        if response == CLOSING_MSG:
            # se ha cerrado el servido intermedio y el servidor gato
            print("Adios")
        break
