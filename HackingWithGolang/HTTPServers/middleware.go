package main

import (
	"fmt"
	"log"
	"net/http"
)

type Logger struct {
	Inner http.Handler
}

// ServerHTTP is a wrapper to the Logger.Inner ``http.Handle``
func (l *Logger) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	log.Println("Starting ...")
	l.Inner.ServeHTTP(w, r)
	log.Println("Ending ...")
}

// welcome is a callback functions for any request made
// to our server
func welcome(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome!\n")
}

func main() {
	// Handler function is return an ``http.Handler``
	f := http.HandlerFunc(welcome)
	// Instantiating a new Logger instance and assigning
	// the Inner variable to be f
	l := Logger{Inner: f}
	// Starting server
	http.ListenAndServe("127.0.0.1:8080", &l)
}
