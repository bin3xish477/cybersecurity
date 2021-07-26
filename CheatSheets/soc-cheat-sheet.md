# SOC Analyst Cheat Sheet

### Links
- [Windows Security Log Events](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx?i=j)

### Get Amazon IP Ranges
```
curl https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.prefixes[] | select(.service=="S3") | .ip_prefix'
```
