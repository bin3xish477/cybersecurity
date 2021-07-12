package main

import (
	crand "crypto/rand"
	"crypto/rsa"
	"crypto/x509"
	"crypto/x509/pkix"
	"encoding/pem"
	"flag"
	"fmt"
	"log"
	"math/big"
	"math/rand"
	"net/http"
	"os"
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

func createCertificateAuthority() *x509.Certificate {
	ca := &x509.Certificate{
		SerialNumber: big.NewInt(1653),
		Subject: pkix.Name{
			Organization: []string{generateRandomString(length)},
			Country:      []string{"US"},
		},
		NotBefore:             time.Now(),
		NotAfter:              time.Now().AddDate(1, 0, 0),
		IsCA:                  true,
		ExtKeyUsage:           []x509.ExtKeyUsage{x509.ExtKeyUsageClientAuth, x509.ExtKeyUsageServerAuth},
		KeyUsage:              x509.KeyUsageDigitalSignature | x509.KeyUsageCertSign,
		BasicConstraintsValid: true,
	}
	return ca
}

func generateSelfSignedCert() {
	ca := createCertificateAuthority()
	priv, _ := rsa.GenerateKey(crand.Reader, 2048)
	pub := &priv.PublicKey
	ca_b, err := x509.CreateCertificate(crand.Reader, ca, ca, pub, priv)
	if err != nil {
		log.Println("ERROR: error creating certificate")
		os.Exit(1)
	}

	certOut, err := os.Create("server.crt")
	pem.Encode(certOut, &pem.Block{Type: "CERTIFICATE", Bytes: ca_b})
	certOut.Close()
	log.Println("INFO: writing public key to `server.crt`")

	keyOut, err := os.OpenFile("server.key", os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0600)
	pem.Encode(keyOut, &pem.Block{Type: "RSA PRIVATE KEY", Bytes: x509.MarshalPKCS1PrivateKey(priv)})
	keyOut.Close()
	log.Println("INFO: writing private key to `server.key`")
}

var (
	dir      string
	port     int
	username string = generateRandomString(length)
	password string = generateRandomString(length)
)

const (
	charset string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789%&*#!$-="
	length  int    = 16
)

func auth(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		u, p, ok := r.BasicAuth()
		if ok {
			if u == username && p == password {
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

	// generate cert every time the program is ran
	generateSelfSignedCert()
	log.Fatal(http.ListenAndServeTLS(fmt.Sprintf(":%d", port), "server.crt", "server.key", nil))
}
