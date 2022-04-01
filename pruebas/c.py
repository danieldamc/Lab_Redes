import socket as skt

CLIENT_PORT = 5000

clientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
clientSocket.bind(('localhost', CLIENT_PORT))
FORMAT = 'utf-8'

print('esperando mensaje servidor intermedio')
playerSocket, playerAddr = clientSocket.recvfrom(1024)
msg = playerSocket.decode(FORMAT)
print('Mensaje del servidor intemedio', msg)

clientSocket.sendto("recivido".encode(FORMAT), playerAddr)
