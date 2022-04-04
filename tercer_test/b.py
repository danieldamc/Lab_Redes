import socket as skt
import numpy as np

ADDRESS = 'localhost'
CLIENT_PORT = 5001
FORMAT = 'utf-8'
DISP_MSG = 'DISP'
END_MSG = 'END'
CLOSING_MSG = 'CLOSING'
CLOSE_MSG = 'CLOSE'


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


def results(board):
    winner = 0
    for player in ['o', 'x']:
        if win(board, player):
            winner = player
    if np.all(board != '-') and winner == 0:
        winner = '-1'
    return winner


def array_to_msg(board):
    msg = ''
    for x in board:
        for y in x:
            msg += y
    return msg


serverPort = 5000
serverSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
clientSocket.bind((ADDRESS, CLIENT_PORT))
clientSocket.listen()
clientConn, clientAddr = clientSocket.accept()

while True:
    print("Esperando mensaje del cliente")
    msg = clientConn.recv(1024).decode(FORMAT)
    print(f"Mensaje del cliente: {msg}")
    if msg == CLOSE_MSG:
        # enviar mensaje de apagado a servidor gato
        serverSocket.sendto(msg.encode(FORMAT), (ADDRESS, serverPort))
        msg, addr = serverSocket.recvfrom(1024)
        if msg.decode(FORMAT) == CLOSING_MSG:
            print("El servidor gato ha cerrado")
        print("Cerrando servidor intermedio")
        break

    if msg == DISP_MSG:
        serverSocket.sendto(msg.encode(FORMAT), (ADDRESS, serverPort))
        msg, addr = serverSocket.recvfrom(1024)
        msg = msg.decode(FORMAT)

        if msg == 'OK':
            clientConn.send('OK'.encode(FORMAT))
            while True:
                print(f"ADDR {addr}")
                print('esperando board')
                msg = clientConn.recv(1024).decode(FORMAT)
                # check if client win
                print(msg)
                board = msg_to_array(msg)
                winners = results(board)
                if winners in ['-1', 'o', 'x']:
                    serverSocket.sendto(END_MSG.encode(FORMAT), addr)
                    clientConn.send(
                        (array_to_msg(board)+winners).encode(FORMAT))
                    msg, addr = serverSocket.recvfrom(1024)
                    break
                serverSocket.sendto(msg.encode(FORMAT), addr)

                # check if server win
                msg, addr = serverSocket.recvfrom(1024)
                msg = msg.decode(FORMAT)
                print(msg)
                board = msg_to_array(msg)
                winners = results(board)
                if winners in ['-1', 'o', 'x']:
                    serverSocket.sendto(END_MSG.encode(FORMAT), addr)
                    clientConn.send(
                        (array_to_msg(board)+winners).encode(FORMAT))
                    msg, addr = serverSocket.recvfrom(1024)
                    break

                clientConn.send(msg.encode(FORMAT))

        else:
            clientConn.send('NO'.encode(FORMAT))


clientConn.send(CLOSING_MSG.encode(FORMAT))
clientConn.close()
print('El servidor intermedio se ha cerrado exitosamente')
