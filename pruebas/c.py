import socket as skt
from random import randint

CLIENT_PORT = 5000
FORMAT = 'utf-8'
DISP_MSG = 'DISP'
END_MSG = 'END'


clientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
clientSocket.bind(('localhost', CLIENT_PORT))
while True:
    print("Esperando mensaje cliente")
    clientData, clientAddr = clientSocket.recvfrom(1024)
    msg = clientData.decode(FORMAT)
    print('Mensaje del servidor intemedio', msg)
    if msg == DISP_MSG:
        rand_disp = randint(0, 99)
        if rand_disp <= 19:
            disp = "NO"
        else:
            disp = "OK"

    new_port = randint(8000, 65535)
    print(new_port)
    newClientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
    newClientSocket.bind(('localhost', new_port))
    newClientSocket.sendto(disp.encode(FORMAT), clientAddr)
    if disp == "OK":
        while True:
            print("Esperando mensaje cliente2")
            clientData, clientAddr = newClientSocket.recvfrom(1024)
            msg = clientData.decode(FORMAT)
            newClientSocket.close()
            new_port = randint(8000, 65535)
            print(f"nuevo puerto {new_port}")
            newClientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
            newClientSocket.bind(('localhost', new_port))

            if msg == END_MSG:
                print('algien ha ganado el juego')
            else:
                print('table')
                newClientSocket.sendto('table'.encode(FORMAT), clientAddr)

    newClientSocket.close()
