import socket as skt

ADDRESS = 'localhost'
CLIENT_PORT = 5001
FORMAT = 'utf-8'
DISP_MSG = 'DISP'

serverPort = 5000
serverSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)


while True:
    port = int(input('port: '))
    msg = input("msg: ")
    serverSocket.sendto(msg.encode(FORMAT), (ADDRESS, port))
    print("esperando mensaje del servidor")
    msg, addr = serverSocket.recvfrom(1024)
    print(f"addr del servidor: {addr}")
    print("mensaje del servidor", msg.decode())
