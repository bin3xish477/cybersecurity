package main

import (
	"fmt"
	"io"
	"log"
	"net"
)

func echo(conn net.Conn) {
	defer conn.Close()

	data := make([]byte, 512)

	for {
		i, err := conn.Read(data[0:])
		if err == io.EOF {
			log.Println("[-] Connection has been terminated")
			break
		}
		if err != nil {
			log.Fatalln("[-] An error occured while reading from connection")
			break
		}

		fmt.Printf("Received %d bytes:\n%s", i, string(data))

		if _, err = conn.Write(data[0:i]); err != nil {
			log.Fatalln("[-] An error occured writing to connection")
		}
	}
}

func main() {
	listener, err := net.Listen("tcp", "127.0.0.1:1337")
	if err != nil {
		log.Fatalln("Unable to create listener on port 127.0.0.1:1337")
	}
	fmt.Println("[+] Listening on 127.0.0.1:1337")

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatalln("Unable to receive connection from client")
		}
		go echo(conn)
	}
}
