package main

import (
	"fmt"
	"net/http"
)

func hello(w http.ResponseWriter, r *http.Request) {
	// Writing query supplied data into ``http.ResponseWriter``
	// which is an ``io.Writer``
	fname := r.URL.Query().Get("fname")
	lname := r.URL.Query().Get("lname")
	fmt.Fprintf(w, "Hello, %s %s!", fname, lname)
}

func main() {
	http.HandleFunc("/hello", hello)
	http.ListenAndServe("127.0.0.1:8080", nil)
}
