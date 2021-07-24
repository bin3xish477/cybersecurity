package main

import (
	"fmt"
	"log"
	"os/exec"
	"regexp"
	"runtime"
	"strings"

	"github.com/manifoldco/promptui"
)

var (
	space = regexp.MustCompile(`\s+`)
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
					"powershell.exe", "-NoProfile", "-NonInteractive", "-c", "Get-LocalUser", "|", "Select", "Name", ",", "SID",
				).Output()
				if err != nil {
					log.Printf("error running system command: %s", err)
					return
				}
				users := strings.Split(strings.ReplaceAll(string(out), `\r\n`, `\n`), "\n")
				fmt.Println("-----------------------------------------")
				for _, user := range users[3 : len(users)-3] {
					s := space.ReplaceAllString(user, " ")
					trimmed := strings.Trim(s, " ")
					line := strings.Split(trimmed, " ")
					userName, sid := line[0], line[1]
					fmt.Printf(
						"\u001b[31mUserName\u001b[0m=%s, \u001b[32mSID\u001b[0m=%s\n", userName, sid,
					)
				}
				fmt.Println()
			case "List Groups":
				out, err := exec.Command(
					"powershell.exe", "-NoProfile", "-NonInteractive", "-c", "Get-LocalGroup", "|", "Select", "Name", ",", "SID",
				).Output()
				if err != nil {
					log.Printf("error running system command: %s", err)
					return
				}
				groups := strings.Split(strings.ReplaceAll(string(out), `\r\n`, `\n`), "\n")
				fmt.Println("-----------------------------------------")
				for _, group := range groups[3 : len(groups)-3] {
					s := space.ReplaceAllString(group, " ")
					trimmed := strings.Trim(s, " ")
					line := strings.Split(trimmed, " ")
					if len(line) == 0 {
						continue
					}
					lineLen := len(line)
					groupName, sid := line[0:lineLen-1], line[lineLen-1]
					fmt.Printf("\u001b[31mGroupName\u001b[0m='%s', \u001b[32mSID\u001b[0m=%s\n", strings.Join(groupName, " "), sid)
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
					userName, shell := line[0], line[len(line)-1]
					if userName == "" && shell == "" {
						continue
					}
					fmt.Printf(
						"\u001b[31mUserName\u001b[0m=%s, \u001b[32mShell\u001b[0m=%s\n", userName, shell,
					)
				}
				fmt.Println()
			case "List Groups":
				catPath, _ := commandExists("cat")
				out, err := exec.Command(catPath, "/etc/group").Output()
				if err != nil {
					log.Printf("error running system command: %s", err)
					return
				}
				groups := strings.Split(string(out), "\n")
				fmt.Println("-----------------------------------------")
				for _, group := range groups {
					trimmed := strings.Trim(group, " ")
					columnsByColon := strings.Split(trimmed, ":")
					groupName, groupMembers := columnsByColon[0], columnsByColon[len(columnsByColon)-1]
					fmt.Printf(
						"\u001b[31mGroupName\u001b[0m=%s, \u001b[32mMembers\u001b[0m='%s'\n", groupName, groupMembers,
					)
				}

			}
		}
	}
}
