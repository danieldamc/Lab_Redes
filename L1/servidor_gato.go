package main

import (
	"fmt"
	"log"
	"math/rand"
	"net"
	"strconv"
	"time"
)

const (
	CLOSE_MSG   = "CLOSE"
	DISP_MSG    = "DISP"
	END_MSG     = "END"
	SERVER_HOST = "localhost"
	SERVER_PORT = ":5000"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	// Maybe delete this
	disp := "OK"
	addr := &net.UDPAddr{} // (?)
	n := 0

	s, err := net.ResolveUDPAddr("udp4", SERVER_PORT)
	checkErr(err)
	connection, err := net.ListenUDP("udp4", s)
	checkErr(err)

	for {
		fmt.Println("Esperando mensaje servidor intermedio")
		clientData := make([]byte, 1024)
		n, addr, _ = connection.ReadFromUDP(clientData)
		msg := string(clientData[:n])

		fmt.Println("Mensaje del servidor intermedio: ", msg)

		if msg == CLOSE_MSG {
			fmt.Println("El servidor gato esta cerrando.")
			// Deberia cerrar la conexion(?)
			break
		} else if msg == DISP_MSG {

			rand_disp := randInt(0, 99)

			if rand_disp <= 19 {
				disp = "NO"
			} else {
				disp = "OK"
			}
		}

		fmt.Println("Disponibilidad servidor gato: " + disp)

		new_port := randInt(8000, 65535)
		fmt.Println("Nuevo puerto: ", new_port)

		s, err := net.ResolveUDPAddr("udp4", ":"+strconv.Itoa(new_port))
		checkErr(err)

		new_connection, err := net.ListenUDP("udp4", s)
		checkErr(err)

		_, _ = new_connection.WriteToUDP([]byte(disp), addr)

		if disp == "OK" {
			// Close port 5000
			connection.Close()
			for {
				fmt.Println("Esperando Tabla")
				clientData := make([]byte, 1024)
				n, addr, _ = new_connection.ReadFromUDP(clientData)
				msg := string(clientData[:n])

				fmt.Println("Tabla recibida: ", msg)

				fmt.Println("Cerrando puerto: ", new_port)
				new_connection.Close()

				new_port = randInt(8000, 65535)
				fmt.Println("Nuevo puerto: ", new_port)

				// new connection
				s, err := net.ResolveUDPAddr("udp4", ":"+strconv.Itoa(new_port))
				checkErr(err)
				new_connection, err = net.ListenUDP("udp4", s) // add :
				checkErr(err)

				if msg == END_MSG {
					fmt.Println("A terminado el juego.")
					_, _ = new_connection.WriteToUDP([]byte("WIN"), addr)
					break
				} else {
					// bot plays

					board := msg_to_array(msg)
					board = random_play_bot(board)

					response := array_to_msg(board)
					fmt.Println("Tabla respuesta: ", response)
					new_connection.WriteToUDP([]byte(response), addr)
				}
			}
			// Open new port 5000
			s, err := net.ResolveUDPAddr("udp4", SERVER_PORT)
			checkErr(err)
			connection, err = net.ListenUDP("udp4", s)
			checkErr(err)
		}

		fmt.Println("Cerrando puerto: ", new_port)
		new_connection.Close()

	}
	connection.WriteToUDP([]byte("CLOSING"), addr)
	connection.Close()
	fmt.Println("El servidor gato se ha cerrado exitosamente.")

}

//retorna un numero aleatorio entre min y max.
func randInt(min, max int) int {
	return rand.Intn(max-min) + min
}

//revisa si hay errores.
func checkErr(err error) {

	if err != nil {

		log.Fatal(err)
	}
}

// bot que juega posicionando su simbolo en algun punto del la tabla.
func random_play_bot(board [3][3]string) [3][3]string {
	randx := randInt(0, 3)
	randy := randInt(0, 3)

	for board[randx][randy] != "-" {
		randx = randInt(0, 3)
		randy = randInt(0, 3)
	}

	board[randx][randy] = "x"
	return board
}

// convierte la matriz de la tabla a el mensaje que sera enviado.
func array_to_msg(board [3][3]string) string {
	msg := ""
	for _, x := range board {
		for _, y := range x {
			msg += y
		}
	}
	return msg
}

//retorna el caracter que se encuentra el un indice (index) de un string (str).
func atIndex(str string, index int) string {
	return str[index : index+1]
}

// convierte un mensaje recibido a una matriz que representa la tabla.
func msg_to_array(msg string) [3][3]string {
	board := [3][3]string{
		{atIndex(msg, 0), atIndex(msg, 1), atIndex(msg, 2)},
		{atIndex(msg, 3), atIndex(msg, 4), atIndex(msg, 5)},
		{atIndex(msg, 6), atIndex(msg, 7), atIndex(msg, 8)}}

	return board
}
