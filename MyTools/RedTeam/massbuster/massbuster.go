package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"strconv"
	"strings"

	"github.com/alexflint/go-arg"
)

var args struct {
	HostFile string `arg:"-f,--file" help:"specify the path to file containing IPs/hostnames"`
	Wordlist string `arg:"-w,--wordlist" help:"specify the path to wordlist"`
	Threads  int    `arg:"-t,--threads" help:"number of threads to use" default:"10"`
}

type Config struct {
	GobusterArgs string `json:"gobuster"`
	HttpxArgs    string `json:"httpx"`
}

var (
	hostFile string
	wordList string
	threads  int
	config   *Config
)

const (
	red    = "\u001b[31m"
	end    = "\u001b[0m"
	underL = "\u001b[4m"
)

func getCommandPath(cmd string) (string, bool) {
	path, err := exec.LookPath(cmd)
	if err != nil {
		return "", false
	}
	return path, true
}

func parseConfig() {
	jsonFile, err := os.Open("config.json")
	if err != nil {
		fmt.Println("[-] unable to read `config.json` file")
		os.Exit(1)
	}
	defer jsonFile.Close()

	jsonBytes, _ := ioutil.ReadAll(jsonFile)
	json.Unmarshal(jsonBytes, &config)
}

func gobust(host string) {
	fmt.Printf(
		"URL: %s%s%s%s\n\n", red, underL, host, end,
	)

	mainArgs := fmt.Sprintf("-t %s -u %s -w %s", strconv.Itoa(threads), host, wordList)
	allArgs := fmt.Sprintf("%s %s", mainArgs, config.GobusterArgs)

	if gobusterPath, exists := getCommandPath("gobuster"); exists {
		cmd := exec.Command(gobusterPath, strings.Split(allArgs, " ")...)

		cmd.Stdin = os.Stdin
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmd.Run()
	} else {
		fmt.Println("[!] need to install gobuster.. make sure its in your PATH")
		os.Exit(1)
	}
	fmt.Println()
}

func start() {
	if httpxPath, exists := getCommandPath("httpx"); exists {
		mainArgs := fmt.Sprintf("-threads %s -list %s", strconv.Itoa(threads), hostFile)
		allArgs := fmt.Sprintf("%s %s", mainArgs, config.HttpxArgs)

		cmd := exec.Command(httpxPath, strings.Split(allArgs, " ")...)
		r, _ := cmd.StdoutPipe()

		done := make(chan bool)
		scanner := bufio.NewScanner(r)

		go func() {
			for scanner.Scan() {
				host := scanner.Text()
				gobust(host)
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

	hostFile = args.HostFile
	wordList = args.Wordlist
	threads = args.Threads

	if hostFile == "" || wordList == "" {
		fmt.Println("error: must `-f` and `-w` arguments")
		return
	}

	parseConfig()
	start()
}
