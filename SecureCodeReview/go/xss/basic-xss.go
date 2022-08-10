package main

// http://127.0.0.1:8080/?arg=<script>alert('xss')</script>

import (
        "fmt"
        "io"
        "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
        io.WriteString(w, r.URL.Query().Get("arg"))
}

func main() {
        http.HandleFunc("/", handler)
        fmt.Println("listening on :8080 ...")
        http.ListenAndServe(":8080", nil)
}
