package main

import (
	"flag"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"time"
)

var seededRand *rand.Rand = rand.New(rand.NewSource(time.Now().UnixNano()))

func stringWithCharset(length int, charset string) string {
	b := make([]byte, length)
	for i := range b {
		b[i] = charset[seededRand.Intn(len(charset))]
	}
	return string(b)
}

func generateRandomString(length int) string {
	return stringWithCharset(length, charset)
}

const (
	charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789%&*#!$-="
	length  = 16
)

var (
	dir      string
	port     int
	username = generateRandomString(length)
	password = generateRandomString(length)
)

func auth(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		u, p, ok := r.BasicAuth()
		if ok {
			if u == username && p == password {
				log.Println("INFO: successful login")
				next.ServeHTTP(w, r)
				return
			} else {
				log.Printf("INFO: unsuccessful login with credentials %s:%s", u, p)
			}
		} else {
			log.Println("ERROR: error parsing basic auth")
		}
		w.Header().Set("WWW-Authenticate", `Basic realm="Restricted"`)
		http.Error(w, "Unauthorized", http.StatusUnauthorized)
	})
}

func serveFiles(w http.ResponseWriter, r *http.Request) {
	fs := http.FileServer(http.Dir(dir))
	fs.ServeHTTP(w, r)
}

func main() {
	flag.StringVar(&dir, "dir", ".", "directory to host on web server")
	flag.IntVar(&port, "port", 4443, "port for server to listen on")
	flag.Parse()

	handler := http.HandlerFunc(serveFiles)
	http.Handle("/", auth(handler))

	log.Println(fmt.Sprintf("INFO: server listening on port %d", port))
	log.Println(fmt.Sprintf("INFO: username = %s", username))
	log.Println(fmt.Sprintf("INFO: password = %s", password))
	// TODO: add TLS support to prevent Mitm attacks
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", port), nil))
}
