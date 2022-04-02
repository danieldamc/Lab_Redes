import socket as skt

ADDRESS = 'localhost'
SERVER_PORT = 5001
ADDR = (ADDRESS, SERVER_PORT)
FORMAT = 'utf-8'
DISP_MSG = 'DISP'

clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)  # TCP
clientSocket.connect(ADDR)

sel = ''
while sel not in ['1', '2']:
    sel = input("- Seleccione una opcion\n1-Jugar\n2-Salir\n>>")

if sel == "1":
    # solicitar disponibilidad del servidor gato
    clientSocket.send(DISP_MSG.encode(FORMAT))
    response = clientSocket.recv(1024).decode()
    print(f"respuesta de disponibilidad:  {response}")
    if response == "OK":
        # jugador hace primera jugada
        while True:
            # enviar a servidor intermedio
            # recibir resultados
            # (nueva jugada/presentar ganador)
            continue

else:
    # send close message
    pass

clientSocket.close()
