# Detection Engineering Cheat Sheet

### Malware Analysis Tools

- [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon)
- [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)
- [Process Hacker](https://processhacker.sourceforge.io/)
- [Autoruns](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [TCPView](https://docs.microsoft.com/en-us/sysinternals/downloads/tcpview)
- [Strings](https://docs.microsoft.com/en-us/sysinternals/downloads/strings)
- [CFF Explorer](https://ntcore.com/?page_id=388)
- [Fiddler](https://www.telerik.com/download/fiddler)
- [WireShark](https://www.wireshark.org/download.html)
- [BurpSuite](https://portswigger.net/burp/communitydownload)

### Yara Rules

> Example Rule

```yara
rule silent_banker : banker
{
    meta:
        description = "This is just an example"
        threat_level = 3
        in_the_wild = true
    strings:
        $a = {6A 40 68 00 30 00 00 6A 14 8D 91}
        $b = {8D 4D B0 2B C1 83 C0 27 99 6A 4E 59 F7 F9}
        $c = "UVODFRYSIHLNWPEJXQZAKCBGMT"
    condition:
        1 of ($*)
}
```

- The rule above contains all the basics elements that make up a Yara rule definition:
    - `silent_banker`: the rule name
    - `banker`: a rule tag
    - `meta`: key-value pairs that define metadata about the rule
    - `strings`: the detection strings
    - `condition`: the conditions that must be met for the rule to trigger

### Iptables Rule to Redirect All HTTPS to Burp Suite

```console
sudo iptables -t nat -A PREROUTING -i ens3 -p tcp -–dport 443 -j -REDIRECT --to-port 8080
```
