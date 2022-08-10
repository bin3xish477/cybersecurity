package main

// localhost:8081/?arg1=<script>alert('xss')</script>

import (
        "fmt"
        "net/http"
        "text/template"
)

func handler(w http.ResponseWriter, r *http.Request) {
        arg1 := r.URL.Query().Get("arg1")

        tmpl, err := template.New("params").Parse(
                `{{ define "home" }}
                        {{ . }}
                {{ end }}`,
        )
        if err != nil {
                fmt.Printf("%s\n", err.Error())
        }
        tmpl.ExecuteTemplate(w, "home", arg1)
}

func main() {
        http.HandleFunc("/", handler)
        fmt.Println("listening on :8081 ...")
        http.ListenAndServe(":8081", nil)
}
