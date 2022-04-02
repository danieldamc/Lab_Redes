import socket as skt
from random import randint

CLIENT_PORT = 5000
FORMAT = 'utf-8'
CLOSE_MSG = 'CLOSE'
DISP_MSG = 'DISP'
END_MSG = 'END'


clientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
clientSocket.bind(('localhost', CLIENT_PORT))
while True:
    print("Esperando mensaje cliente")
    clientData, clientAddr = clientSocket.recvfrom(1024)
    msg = clientData.decode(FORMAT)
    print('Mensaje del cliente', msg)

    if msg == CLOSE_MSG:
        print('El servidor gato esta cerrando')
        break

    if msg == DISP_MSG:
        rand_disp = randint(0, 99)
        if rand_disp <= 99:
            disp = "NO"
        else:
            disp = "OK"

    new_port = randint(8000, 65535)
    print(f"Nuevo puerto: {new_port}")
    newClientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
    newClientSocket.bind(('localhost', new_port))
    newClientSocket.sendto(disp.encode(FORMAT), clientAddr)
    if disp == "OK":
        # se cierrra port 5000

        while True:
            print("Esperando mensaje modo juego")
            clientData, clientAddr = newClientSocket.recvfrom(1024)
            msg = clientData.decode(FORMAT)
            newClientSocket.close()
            new_port = randint(8000, 65535)
            print(f"nuevo puerto {new_port}")
            newClientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
            newClientSocket.bind(('localhost', new_port))

            if msg == END_MSG:
                print('algien ha ganado el juego')
                newClientSocket.sendto('WIN'.encode(FORMAT), clientAddr)
                break
            else:
                print('table')
                newClientSocket.sendto('table'.encode(FORMAT), clientAddr)


clientSocket.sendto('CLOSING'.encode(FORMAT), clientAddr)
clientSocket.close()
print("El servidor gato se ha cerrado exitosamente")
