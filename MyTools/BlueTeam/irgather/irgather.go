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
func getLocalUsersWin() {
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
		fmt.Printf("\u001b[31mUserName\u001b[0m=%s, \u001b[32mSID\u001b[0m=%s\n", userName, sid)
	}
	fmt.Println()
}

func getLocalGroupsWin() {
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
}

func getProcessesWin() {
	out, err := exec.Command(
		"powershell.exe", "-NoProfile", "-NonInteractive", "-c", "Get-Process", "|", "Select", "Name", ",", "Id",
	).Output()
	if err != nil {
		log.Printf("error running system command: %s", err)
		return
	}
	processes := strings.Split(strings.ReplaceAll(string(out), `\r\n`, `\n`), "\n")
	fmt.Println("-----------------------------------------")
	for _, process := range processes[3 : len(processes)-3] {
		s := space.ReplaceAllString(process, " ")
		trimmed := strings.Trim(s, " ")
		line := strings.Split(trimmed, " ")
		lineLen := len(line)
		if lineLen == 0 {
			continue
		}
		procName, pid := line[0:lineLen-1], line[lineLen-1]
		fmt.Printf("\u001b[31mProcessName\u001b[0m=%s, \u001b[32mProcessID\u001b[0m=%s\n", strings.Join(procName, " "), pid)
	}
	fmt.Println()
}

func getServicesWin() {
	out, err := exec.Command(
		"powershell.exe", "-NoProfile", "-NonInteractive", "-c", "Get-Service", "|", "Select", "Name", ",", "Status",
	).Output()
	if err != nil {
		log.Printf("error running system command: %s", err)
		return
	}
	services := strings.Split(strings.ReplaceAll(string(out), `\r\n`, `\n`), "\n")
	fmt.Println("-----------------------------------------")
	for _, service := range services[3 : len(services)-3] {
		s := space.ReplaceAllString(service, " ")
		trimmed := strings.Trim(s, " ")
		line := strings.Split(trimmed, " ")
		lineLen := len(line)
		if lineLen == 0 {
			continue
		}
		serviceName, status := line[0:lineLen-1], line[lineLen-1]
		fmt.Printf("\u001b[31mServiceName\u001b[0m=%s, \u001b[32mStatus\u001b[0m=%s\n", strings.Join(serviceName, " "), status)
	}
	fmt.Println()
}
func getOpenPortsWin() {
	out, err := exec.Command(
		"powershell.exe", "-NoProfile", "-NonInteractive", "-c",
		"Get-NetTCPConnection", "-State", "Listen", "|", "Select", "OwningProcess", ",", "LocalAddress", ",", "LocalPort",
	).Output()
	if err != nil {
		log.Printf("error running system command: %s", err)
		return
	}
	listeningPorts := strings.Split(strings.ReplaceAll(string(out), `\r\n`, `\n`), "\n")
	fmt.Println("-----------------------------------------")
	for _, port := range listeningPorts[3 : len(listeningPorts)-3] {
		s := space.ReplaceAllString(port, " ")
		trimmed := strings.Trim(s, " ")
		line := strings.Split(trimmed, " ")
		lineLen := len(line)
		if lineLen == 0 {
			continue
		}
		pid, localAddr, localPort := line[0], line[1], line[2]
		fmt.Printf(
			"\u001b[31mProcessId\u001b[0m=%s, \u001b[32mLocalAddr\u001b[0m=%s, \u001b[33mLocalPort\u001b[0m=%s\n",
			pid, localAddr, localPort)
	}
	fmt.Println()
}

func main() {
	prompt := createPrompt()
	if runtime.GOOS == "windows" {
		for {
			_, selected, err := prompt.Run()
			if err != nil {
				log.Printf("an error occured: %s", err)
				return
			}
			switch selected {
			case "List Users":
				getLocalUsersWin()
			case "List Groups":
				getLocalGroupsWin()
			case "List Processes":
				getProcessesWin()
			case "List Services":
				getServicesWin()
			case "List Open Ports":
				getOpenPortsWin()
			default:
				return
			}
		}
	} else {
		fmt.Println("\u001b[31mThis tool was written for Windows information gathering\u001b[0m")
	}
}
