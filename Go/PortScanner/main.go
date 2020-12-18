package main

import (
	"fmt"
	"net"
	"sort"
)

func worker(ports, results chan int) {
	for p := range ports {
		addr := fmt.Sprintf("scanme.nmap.org:%d", p)
		conn, err := net.Dial("tcp", addr)
		if err != nil {
			continue
		}
		conn.Close()
		results <- p
	}
}

func main() {
	ports, results := make(chan int, 100), make(chan int)
	var openPorts []int

	for i := 0; i < cap(ports); i++ {
		go worker(ports, results)
	}

	go func() {
		for i := 1; i <= 1024; i++ {
			ports <- i
		}
	}()

	for range results {
		port := <-results
		openPorts = append(openPorts, port)
	}

	close(ports)
	close(results)

	sort.Ints(openPorts)
	for _, port := range openPorts {
		fmt.Printf("%d [open]\n", port)
	}
}
