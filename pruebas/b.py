import socket as skt

ADDRESS = 'localhost'
CLIENT_PORT = 5001
FORMAT = 'utf-8'

serverPort = 5000
serverSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)


clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
clientSocket.bind(('localhost', CLIENT_PORT))
clientSocket.listen(1)

print('Esperando mensaje del cliente')
playerSocket, playerAddr = clientSocket.accept()
msg = playerSocket.recv(1024).decode(FORMAT)
print('Mensaje del cliente', msg)


serverSocket.sendto(msg.encode(FORMAT), (ADDRESS, serverPort))

print("esperando mensaje del servidor")
msg, addr = serverSocket.recvfrom(1024)

print("mensaje del servidor", msg.decode())
playerSocket.send(msg)
