package main

import (
	"fmt"
	"log"
	"os"
	"rpc"
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

	for _, session := range sessions {
		fmt.Print("Session Id: %d\n", session.Id)
		fmt.Print("Session type: %s\n", session.Type)
		fmt.Print("Session Payload: %s\n", session.Payload)
	}
}
