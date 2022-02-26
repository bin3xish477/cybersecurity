package main

import (
	"encoding/hex"
	"fmt"
	"net"
)

var (
	Domain  = "bin3xish477.com"
	DataLen = 60
)

func main() {
	ip, _ := net.LookupIP(Domain)
	d := []byte("1$@$%afLqaQWafljzfpqaffa$!#^%")
	hd := hex.EncodeToString(d)
	fmt.Println(ip[0])
	fmt.Printf("%s.%s\n", hd, Domain)
}
