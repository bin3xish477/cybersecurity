package main

import (
	"fmt"
	"log"
	"os/exec"
	"runtime"
	"strings"

	"github.com/manifoldco/promptui"
)

func commandExists(cmd string) (string, bool) {
	path, err := exec.LookPath(cmd)
	if err != nil {
		return "", false
	}
	return path, true
}

func createPrompt() promptui.Select {
	template := promptui.SelectTemplates{
		Label: "{{ . }}:",
	}

	prompt := promptui.Select{
		Label: "Menu",
		Items: []string{
			"List Users",
			"List Groups",
			"List Processes",
			"List Services",
			"List Open Ports",
		},
		Size:      7,
		Templates: &template,
	}
	return prompt
}

func main() {
	prompt := createPrompt()
	// determining os and shell to use
	if runtime.GOOS == "windows" {
		for {
			_, selected, err := prompt.Run()
			if err != nil {
				log.Printf("an error occured: %s", err)
				return
			}
			switch selected {
			case "List Users":
				out, err := exec.Command(
					"powershell.exe", "-NoProfile", "-NonInteractive", "-c", "Get-LocalUser", "|", "Select", "Name",
				).Output()
				if err != nil {
					log.Printf("error running system command: %s", err)
					return
				}
				users := strings.Split(strings.ReplaceAll(string(out), `\r\n`, `\n`), "\n")
				for _, user := range users[3 : len(users)-3] {
					if user == "" {
						continue
					}
					fmt.Printf(
						"\u001b[31mUserName\u001b[0m=%s\n", user,
					)
				}
				fmt.Println()
			default:
				return
			}
		}
	} else {
		for {
			_, selected, err := prompt.Run()
			if err != nil {
				log.Printf("an error occured: %s", err)
				return
			}
			switch selected {
			case "List Users":
				catPath, _ := commandExists("cat")
				out, err := exec.Command(catPath, "/etc/passwd").Output()
				if err != nil {
					log.Printf("error running system command: %s", err)
					return
				}
				users := strings.Split(string(out), "\n")
				fmt.Println("-----------------------------------------")
				for _, user := range users {
					line := strings.Split(user, ":")
					username, shell := line[0], line[len(line)-1]
					if username == "" && shell == "" {
						continue
					}
					fmt.Printf(
						"\u001b[31mUserName\u001b[0m=%s, \u001b[32mShell\u001b[0m=%s\n", username, shell,
					)
				}
				fmt.Println()
			}
		}
	}
}
