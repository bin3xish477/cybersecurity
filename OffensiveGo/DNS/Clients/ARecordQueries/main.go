package main

import (
	"fmt"

	"github.com/miekg/dns"
)

func main() {
	cloudFlare := "1.1.1.1:53"
	var msg dns.Msg
	fqdn := dns.Fqdn("binexishatt.site")
	msg.SetQuestion(fqdn, dns.TypeA)
	resp, err := dns.Exchange(&msg, cloudFlare)
	if err != nil {
		panic(err)
	}

	if len(resp.Answer) < 1 {
		fmt.Println("No records returned...")
		return
	}

	fmt.Println("(A):")
	for _, answer := range resp.Answer {
		if a, ok := answer.(*dns.A); ok {
			fmt.Printf("\t%s\n", a.A)
		}
	}
}