package main

import (
	"context"
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/urfave/negroni"
)

type BadAuth struct {
	Username string
	Password string
}

func (b *BadAuth) ServeHTTP(w http.ResponseWriter, r *http.Request, next http.HandlerFunc) {
	username := r.URL.Query().Get("username")
	password := r.URL.Query().Get("password")
	if username == "" || password == "" {
		http.Error(w, "Not Authorized", 401)
		return
	}

	// Adding the ``username`` value to context of r
	ctx := context.WithValue(r.Context(), "username", username)
	// Setting the new context to the one created in the line above
	r = r.WithContext(ctx)
	// Invoking the next middleware in the chain
	next(w, r)
}

func login(w http.ResponseWriter, r *http.Request) {
	username := r.Context().Value("username").(string)
	fmt.Fprintf(w, "Welcome, %s\n!", username)
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/login", login).Methods("GET")
	n := negroni.Classic()
	n.Use(&BadAuth{
		Username: "admin",
		Password: "totally secure password123",
	})
	n.UseHandler(r)
	http.ListenAndServe("127.0.0.1:8080", n)
}
