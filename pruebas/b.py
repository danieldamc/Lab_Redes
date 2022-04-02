import socket as skt

ADDRESS = 'localhost'
CLIENT_PORT = 5001
FORMAT = 'utf-8'
DISP_MSG = 'DISP'

serverPort = 5000
serverSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)


clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
clientSocket.bind(('localhost', CLIENT_PORT))


while True:
    print('Esperando mensaje del cliente')
    clientSocket.listen(1)
    clientData, clientAddr = clientSocket.accept()
    msg = clientData.recv(1024).decode(FORMAT)
    print('Mensaje del cliente', msg)
    print(msg == DISP_MSG)
    if msg == DISP_MSG:
        serverSocket.sendto(msg.encode(FORMAT), (ADDRESS, serverPort))
        print("esperando mensaje del servidor")
        msg, addr = serverSocket.recvfrom(1024)
        print(f"addr del servidor: {addr}")
        print("mensaje del servidor", msg.decode())
        clientData.send(msg)
    break
