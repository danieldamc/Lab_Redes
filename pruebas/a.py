import socket as skt

ADDRESS = 'localhost'
SERVER_PORT = 5001
ADDR = (ADDRESS, SERVER_PORT)
FORMAT = 'utf-8'

clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)  # TCP
clientSocket.connect(ADDR)

msg_to_send = input('Mensaje: ')
clientSocket.send(msg_to_send.encode(FORMAT))

response = clientSocket.recv(1024).decode()
print("respuesta del servidor", response)

clientSocket.close()
