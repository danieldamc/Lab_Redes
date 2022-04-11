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
    """
    win  revisa si el jugador gano o no.

    input:
    board   : (ndarray) matriz de la tabla de juego.
    player  : (string) simbolo que representa un jugador.

    output:
    win     : (bool) retorna True si el jugador (player) gana la partida, False si no.
    """
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


def results(board):
    winner = 0
    for player in ['o', 'x']:
        if win(board, player):
            winner = player
    if np.all(board != '-') and winner == 0:
        winner = '1'
    return winner


def array_to_msg(board):
    """
    array_to_msg convierte un ndarray len(board) en un string de largo len(board)**2.

    input:
    board   : (ndarray) matrix que representa la tabla de juego

    output:
    msg     : (string) string que representa la tabla de juego
    """
    msg = ''
    for x in board:
        for y in x:
            msg += y
    return msg


def msg_to_array(msg):
    """
    msg_to_array convierte un string en un arreglo de numpy

    input:
    msg     : (string) representa la tabla de juego.

    output:
    matrix  : (ndarray) matriz la cual representa la tabla de juego.
    """
    arr = np.array(list(msg))
    matrix = np.reshape(arr, (3, 3))
    return matrix


serverPort = 5000
serverSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
clientSocket.bind((ADDRESS, CLIENT_PORT))
clientSocket.listen()
print("Esperando mensaje del cliente")
clientConn, clientAddr = clientSocket.accept()

while True:
    msg = clientConn.recv(1024).decode(FORMAT)
    print(f"Mensaje del cliente: {msg}")
    if msg == CLOSE_MSG:
        # enviar mensaje de apagado a servidor gato
        serverSocket.sendto(msg.encode(FORMAT), (ADDRESS, serverPort))
        msg, addr = serverSocket.recvfrom(1024)
        if msg.decode(FORMAT) == CLOSING_MSG:
            print("El servidor gato ha cerrado")
        print("El servidor intermedio esta cerrando")
        break

    if msg == DISP_MSG:
        serverSocket.sendto(msg.encode(FORMAT), (ADDRESS, serverPort))
        msg, addr = serverSocket.recvfrom(1024)
        msg = msg.decode(FORMAT)

        if msg == 'OK':
            clientConn.send('OK'.encode(FORMAT))
            while True:
                print(f"nueva addr servidor gato: {addr}")
                print('Esperando mensaje del cliente')
                msg = clientConn.recv(1024).decode(FORMAT)
                # check if client win
                print(f"Tabla recibida del cliente: {msg}")
                board = msg_to_array(msg)
                winners = results(board)
                if winners in ['1', 'o', 'x']:
                    serverSocket.sendto(END_MSG.encode(FORMAT), addr)
                    clientConn.send(
                        (array_to_msg(board)+winners).encode(FORMAT))
                    msg, addr = serverSocket.recvfrom(1024)
                    print('Juego Finalizado')
                    break
                print('No hay ganador')
                serverSocket.sendto(msg.encode(FORMAT), addr)

                # check if server win
                msg, addr = serverSocket.recvfrom(1024)
                msg = msg.decode(FORMAT)
                print(f"Tabla recibida del servidor gato: {msg}")
                board = msg_to_array(msg)
                winners = results(board)
                if winners in ['1', 'o', 'x']:
                    serverSocket.sendto(END_MSG.encode(FORMAT), addr)
                    clientConn.send(
                        (array_to_msg(board)+winners).encode(FORMAT))
                    msg, addr = serverSocket.recvfrom(1024)
                    print("Juego Finalizado")
                    break
                print('No hay ganador')
                clientConn.send(msg.encode(FORMAT))

        else:
            clientConn.send('NO'.encode(FORMAT))

serverSocket.close()
clientConn.send(CLOSING_MSG.encode(FORMAT))
clientConn.close()
print('El servidor intermedio se ha cerrado exitosamente')
