package main

import (
	"fmt"
	"log"
	"os"
	"rpc"
)

var (
	printf := fmt.Printf
	println := fmt.Println
)

func main() {
	host := os.Getenv("MSFHOST")
	user := "msf"
	pass := os.Getenv("MSFPASS")

	if host == "" || pass == "" {
		log.Fatalln("Missing required environment variables: MSFHOST OR MSFPASS")
	}

	msfrpc, err := rpc.New(host, user, pass)
	defer msfrpc.Logout()
	if err != nil {
		log.Panicln(err)
	}

	sessions, err := msfrpc.SessionList()
	if err != nil {
		log.Panicln(err)
	}
	
	println("Metasploit Sessions:")
	for _, session := range sessions {
		printf("Session Id: %d\n", session.Id)
		printf("Session type: %s\n", session.Type)
		printf("Session Payload: %s\n", session.Payload)
		println("[ -------------------------------------------------- ]")
	}
}
