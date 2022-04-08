import socket as skt
import numpy as np
from random import randint

CLIENT_PORT = 5000
FORMAT = 'utf-8'
CLOSE_MSG = 'CLOSE'
DISP_MSG = 'DISP'
END_MSG = 'END'


def random_bot_nazi(board):
    # quizas hacerlo mas nazi???
    randx = randint(0, 2)
    randy = randint(0, 2)
    while board[randx][randy] != '-':
        randx = randint(0, 2)
        randy = randint(0, 2)
    board[randx][randy] = 'x'
    return board


def array_to_msg(board):
    msg = ''
    for x in board:
        for y in x:
            msg += y
    return msg


def msg_to_array(msg):
    arr = np.array(list(msg))
    return np.reshape(arr, (3, 3))


clientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
clientSocket.bind(('localhost', CLIENT_PORT))
while True:
    print("Esperando mensaje servidor intermedio")
    clientData, clientAddr = clientSocket.recvfrom(1024)
    msg = clientData.decode(FORMAT)
    print('Mensaje del servidor intermedio', msg)

    if msg == CLOSE_MSG:
        print('El servidor gato esta cerrando')
        break

    if msg == DISP_MSG:
        rand_disp = randint(0, 99)
        if rand_disp <= 19:
            disp = "NO"
        else:
            disp = "OK"

    print(f"Disponibilidad servidor gato: {disp}")

    new_port = randint(8000, 65535)
    print(f"Nuevo puerto: {new_port}")
    newClientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
    newClientSocket.bind(('localhost', new_port))
    newClientSocket.sendto(disp.encode(FORMAT), clientAddr)
    if disp == "OK":
        # cerrar puerto 5000
        clientSocket.close()
        while True:
            print("Esperando Tabla")
            clientData, clientAddr = newClientSocket.recvfrom(1024)
            msg = clientData.decode(FORMAT)
            print(f"Tabla recivida: {msg}")
            print(f"Cerrando puerto: {new_port}")
            newClientSocket.close()
            new_port = randint(8000, 65535)
            print(f"Nuevo puerto {new_port}")
            newClientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
            newClientSocket.bind(('localhost', new_port))

            if msg == END_MSG:
                print('A terminado el juego')
                newClientSocket.sendto('WIN'.encode(FORMAT), clientAddr)
                break
            else:
                board = msg_to_array(msg)
                board = random_bot_nazi(board)
                response = array_to_msg(board)
                print(f"Tabla respueta : {response}")
                newClientSocket.sendto(response.encode(FORMAT), clientAddr)

        # abrir nuevo puerto 5000
        clientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
        clientSocket.bind(('localhost', CLIENT_PORT))
    print(f"Cerrando puerto: {new_port}")
    newClientSocket.close()

clientSocket.sendto('CLOSING'.encode(FORMAT), clientAddr)
clientSocket.close()
print("El servidor gato se ha cerrado exitosamente")
