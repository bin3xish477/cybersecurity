package main

import (
	"fmt"
	"net/http"
)

type router struct{}

// ServeHTTP is a receiver function that needs to be implemented
// for a type that wants to be a ``http.Handler``
func (r *router) ServeHTTP(rw http.ResponseWriter, req *http.Request) {
	switch req.URL.Path {
	case "/hello":
		fmt.Fprintf(rw, "Hello from /hello")
	case "/welcome":
		fmt.Fprintf(rw, "welcome from /welcome")
	case "/bye":
		fmt.Fprintf(rw, "Bye from /bye")
	default:
		http.Error(rw, "Not found", 404)
	}
}

func main() {
	var r router
	// Passing in the ``http.Hanlder`` type router
	// as second paramter to ```http.ListenAndServer```
	http.ListenAndServe("127.0.0.1:8080", &r)
}
