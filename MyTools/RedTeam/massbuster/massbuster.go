package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"

	"github.com/alexflint/go-arg"
)

var args struct {
	File     string `arg:"-f,--file" help:"specify the path to file containing IPs/hostnames"`
	Wordlist string `arg:"-w,--wordlist" help:"specify the path to wordlist"`
}

var (
	hostFile string
	wordList string
)

func getCommandPath(cmd string) (string, bool) {
	path, err := exec.LookPath(cmd)
	if err != nil {
		return "", false
	}
	return path, true
}

//type Command struct {
//Shell string
//Args  []string
//Cmd   *exec.Cmd
//}

//func (c *Command) exec() {
////fmt.Println(c.Shell, c.Args)
//c.Cmd = exec.Command(c.Shell, c.Args...)
//c.Cmd.Stdin = os.Stdin
//c.Cmd.Stdout = os.Stdout
//c.Cmd.Stderr = os.Stderr
//c.Cmd.Run()
//}

func massBust(host string) {
	if gobusterPath, exists := getCommandPath("gobuster"); exists {
		cmd := exec.Command(gobusterPath,
			"-q", "--no-error", "--useragent", "noleak",
			"-u", hostFile, "-w", wordList,
		)
		cmd.Stdin = os.Stdin
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmd.Run()
	} else {
		fmt.Println("[!] need to install gobuster.. make sure its in your PATH")
		os.Exit(1)
	}

}

func hostStatusCheck() {
	if httpxPath, exists := getCommandPath("httpx"); exists {
		cmd := exec.Command(httpxPath,
			"-silent", "-random-agent", "-no-color",
			"-list", hostFile,
		)

		r, _ := cmd.StdoutPipe()

		done := make(chan bool)

		scanner := bufio.NewScanner(r)

		go func() {
			for scanner.Scan() {
				host := scanner.Text()
				massBust(host)
			}
			done <- true
		}()

		err := cmd.Start()

		if err != nil {
			fmt.Println("[!] an error occured while executing httpx command.. exiting")
			os.Exit(1)
		}

		<-done
		cmd.Wait()

	} else {
		fmt.Println("[!] need to install httpx.. make sure its in your PATH")
		os.Exit(1)
	}
}

func main() {
	arg.MustParse(&args)

	hostFile = args.File
	wordList = args.Wordlist

	hostStatusCheck(ipList)
}
