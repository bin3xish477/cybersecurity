package main

import (
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"

	"github.com/gorilla/mux"
)

var (
	hostProxy = make(map[string]string)
	proxies   = make(map[string]*httputil.ReverseProxy)
)

func init() {
	hostProxy["attacker1.com"] = "http://192.168.33.128:10080"
	hostProxy["attacker2.com"] = "http://192.168.33.128:20080"

	for hostname, u := range hostProxy {
		remote, err := url.Parse(u)
		if err != nil {
			log.Fatal("(main) Unable to parse proxy target")
		}
		proxies[hostname] = httputil.NewSingleHostReverseProxy(remote)
	}
}

func main() {
	r := mux.NewRouter()
	for host, proxy := range proxies {
		r.Host(host).Handler(proxy)
	}
	log.Fatal(http.ListenAndServe(":80", r))
}