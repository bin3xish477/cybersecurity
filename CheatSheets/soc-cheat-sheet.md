# SOC Analyst Cheat Sheet

### Tools and References
- [Windows Security Log Events](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx?i=j)
- [VirusTotal](https://www.virustotal.com/gui/)
- [IPQualityScore](https://www.ipqualityscore.com/ip-reputation-check)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [DMARC Check](https://mxtoolbox.com/dmarc.aspx)
- 

### Get Amazon IP Ranges
```
curl https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.prefixes[] | .ip_prefix'
```
### Set Static IP Address on Windows
```powershell
$IP = "10.10.10.10"
$MaskBits = 24
$Gateway = "10.10.10.1"
$Dns = "10.10.10.100"
$IPType = "IPv4"
$adapter = Get-NetAdapter | ? {$_.Status -eq "up"}
If (($adapter | Get-NetIPConfiguration).IPv4Address.IPAddress) {
 $adapter | Remove-NetIPAddress -AddressFamily $IPType -Confirm:$false
}
If (($adapter | Get-NetIPConfiguration).Ipv4DefaultGateway) {
 $adapter | Remove-NetRoute -AddressFamily $IPType -Confirm:$false
}
$adapter | New-NetIPAddress `
 -AddressFamily $IPType `
 -IPAddress $IP `
 -PrefixLength $MaskBits `
 -DefaultGateway $Gateway
$adapter | Set-DnsClientServerAddress -ServerAddresses $DNS
```
### Set an IP address with DCHP
```powershell
$IPType = "IPv4"
$adapter = Get-NetAdapter | ? {$_.Status -eq "up"}
$interface = $adapter | Get-NetIPInterface -AddressFamily $IPType
If ($interface.Dhcp -eq "Disabled") {
 If (($interface | Get-NetIPConfiguration).Ipv4DefaultGateway) {
 $interface | Remove-NetRoute -Confirm:$false
 }
 $interface | Set-NetIPInterface -DHCP Enabled
 $interface | Set-DnsClientServerAddress -ResetServerAddresses
}
```
### RDP Port Forward Through Jump Box
```bash
ssh -N -q -L 3389:10.10.10.2:3389 jump-box
```
### Get Registry Keys and Properties
```powershell
# get reg key
get-item 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\'
# get specific property from reg key
get-itemproperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\' | select userinit
```
