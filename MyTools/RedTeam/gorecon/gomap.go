package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"os/exec"
	"strings"
)

type Command struct {
	Prog string
	Args []string
	Cmd  *exec.Cmd
}

func (c *Command) exec() {
	fmt.Println(strings.Join(c.Args, " "))
	c.Cmd = exec.Command(c.Prog, c.Args...)
	c.Cmd.Stdin = os.Stdin
	c.Cmd.Stdout = os.Stdout
	c.Cmd.Stderr = os.Stderr
	c.Cmd.Run()
}

func commandExists(cmd string) (string, bool) {
	path, err := exec.LookPath(cmd)
	if err != nil {
		return "", false
	}
	return path, true
}

func main() {
	var mode string
	var args string
	var ipfile string
	flag.StringVar(&mode, "mode", "", "specify gomap mode (nmap-allports|nmap-service) [required]")
	flag.StringVar(&args, "args", "", "specify additional program arguments [optional]")
	flag.StringVar(&ipfile, "ipfile", "", "file with ip/host's to scan [required]")
	flag.Parse()

	if mode == "" {
		flag.PrintDefaults()
		return
	}

	nmap := Command{}

	if nmappPath, exists := commandExists("nmap"); exists {
		nmap.Prog = nmappPath
	} else {
		log.Println("Nmap is not installed")
		return
	}

	switch mode {
	case "nmap-allports":
		if args != "" {
			nmap.Args = []string{
				"--open", "-Pn", "-p-", "-vv", fmt.Sprintf("%s", args), "-iL", ipfile,
			}
		} else {
			nmap.Args = []string{
				"--open", "-Pn", "-p-", "-vv", "-iL", ipfile,
			}
		}
		nmap.exec()
	case "nmap-service":
		if args != "" {
			nmap.Args = []string{
				"--open", "-Pn", "-sV", "-sC", "-vv", fmt.Sprintf("%s", args), "-iL", ipfile,
			}
		} else {
			nmap.Args = []string{
				"--open", "-Pn", "-sV", "-sC", "-vv", "-iL", ipfile,
			}
		}
		nmap.exec()
	default:
		log.Printf("Invalid mode specified: %s", mode)
		return
	}

}
