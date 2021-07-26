# SOC Analyst Cheat Sheet

### Tools and References
- [Windows Security Log Events](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx?i=j)
- [VirusTotal](https://www.virustotal.com/gui/)
- [IPQualityScore](https://www.ipqualityscore.com/ip-reputation-check)
- [CyberChef](https://gchq.github.io/CyberChef/)

### Get Amazon IP Ranges
```
curl https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.prefixes[] | .ip_prefix'
```
