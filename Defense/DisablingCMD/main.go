package main

import (
	"fmt"

	"golang.org/x/sys/windows"
	"golang.org/x/sys/windows/registry"
)

func main() {
	regKey := `Software\Policies\Microsoft\Windows`
	var sid *windows.SID

	err := windows.AllocateAndInitializeSid(
		&windows.SECURITY_NT_AUTHORITY,
		2,
		windows.SECURITY_BUILTIN_DOMAIN_RID,
		windows.DOMAIN_ALIAS_RID_ADMINS,
		0, 0, 0, 0, 0, 0,
		&sid)

	if err != nil {
		fmt.Printf("SID Error: %s\n", err)
		panic(err)
	}

	t := windows.Token(0)
	isAdmin, err := t.IsMember(sid)

	if !isAdmin {
		fmt.Println("[-] Modifying registry requires administratives privilegees...")
		fmt.Println("[!] Please run program as administrator...")
		panic(err)
	}

	key, err := registry.OpenKey(registry.CURRENT_USER, regKey, registry.ALL_ACCESS)
	if err != nil {
		fmt.Printf("An error occured opening registry key ➜ %s", "HKEY_CURRENT_USER\\"+regKey)
		panic(err)
	}

	fmt.Printf("\n[+] Setting value 'DisableCMD' to DWORD,1 in registry key ➜ %s\n", "HKEY_CURRENT_USER\\"+regKey)
	err = key.SetDWordValue("DisableCMD", uint32(1))
	if err != nil {
		fmt.Printf("An error occured modifying registry key ➜ %s\n", "HKEY_CURRENT_USER\\"+regKey)
		panic(err)
	}
	fmt.Println("[+] Command Prompt has been disabled...")
	fmt.Println("[?] Try running cmd.exe \\c \"whoami\" in PowerShell window...")
	fmt.Println()
}
