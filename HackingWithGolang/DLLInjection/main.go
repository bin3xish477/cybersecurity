package main

import (
	"syscall"
)

var (
	kern32 = syscall.NewLazyDLL("Kernel32.dll")

	// imported functions from kernel32.dll
	openProcess        = kern32.NewProc("OpenProcess")
	getProcAddress     = kern32.NewProc("GetProcAddress")
	virtualAllocEx     = kern32.NewProc("VirtualAllocEx")
	createRemoteThread = kern32.NewProc("CreateRemoteThread")
	writeProcessMemory = kern32.NewProc("WriteProcessMemory")
	resumeThread       = kern32.NewProc("ResumeThread")
	closeHandle        = kern32.NewProc("CloseHandle")
)

func main() {
}
