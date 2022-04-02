sel = ''
while sel not in ['1', '2']:
    sel = input("- Seleccione una opcion\n1-Jugar\n2-Salir\n>>")

if sel == "1":
    # solicitar disponibilidad del servidor gato
    # enviar mensaje
    # recibir mensaje
    msg = "NO"
    print(f"respuesta de disponibilidad:  {msg}")
    if msg == "OK":
        # jugador hace primera jugada
        while True:
            # enviar a servidor intermedio
            # recibir resultados
            # (nueva jugada/presentar ganador)
            continue

else:
    # send close message
    pass
