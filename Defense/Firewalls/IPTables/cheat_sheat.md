# Iptables Cheat Sheet

### A -> appends a rule at the end of the CHAIN
```sudo iptables -A OUTPUT -p tcp --dport 443 -j DROP```
 
### I -> inserts a rule on top (1st position) of the CHAIN
```sudo iptables -I OUTPUT -p tcp --dport 443 -d www.linux.com -j ACCEPT```
 
### F -> flushes the CHAIN
```sudo iptables -t filter -F OUTPUT```
 
### Z -> zeros the packet and byte counters
```sudo iptables -t filter -Z```
 
### D -> deletes a rule
```sudo iptables -D OUTPUT 2```
 
### P -> sets the default POLICY
```sudo iptables -P INPUT ACCEPT```
 
### N -> creates a user-defined CHAIN
```sudo iptables -N TCP_TRAFFIC```
 
### X -> delete a user-defined CHAIN
```sudo iptables -X TCP_TRAFFIC```

### Default Tables
filter: default table provided by iptables; handles the INPUT, OUTPUT, and FORWARD chains
nat: specialized for DNAT/SNAT
mangles: specialized for packet alteration
raw: used to set a mark on packets that should not be tracked by the connection tracking system
Flushing Iptables
```
sudo iptables -t filter -F 
sudo iptables -t nat -F
sudo iptables -t mangle -F
sudo iptables -t raw -F
```

### Flushing user-defined chains
```sudo iptables -X```
### show all chain and corresponding rule number
```sudo iptables -L --line-numbers```

### remove rule from chain
```sudo iptables -D [CHAIN] <rule_number>```
### Stop Incoming/Outgoing Echo Request (ping)
#### incoming
```sudo iptables -t filter -A INPUT -p icmp -j DROP```

#### outgoing
```sudo iptables -t filter -A OUTPUT -p icmp -j DROP```

### Stop Any Outbound Request to netfilter.org
```sudo iptables -t filter -A OUTPUT -d netfilter.org -j DROP```
### Iptables SSH Traffic
```sudo iptables -A INPUT -p tcp --dport 22 -s 192.168.33.138 -j ACCEPT```

iptables will evaluate rules in the order they were created so
after running the command above
and then the one below, the one above is checked first. 
Therefore, these two rules combined say: allow ssh traffic from 
192.168.33.138 but deny all other ssh traffic from any other IP address.
```sudo iptables -A INPUT -p tcp --dport 22 -j DROP```

### Listing Firewall Rules
```
sudo iptables -t filter -L
sudo iptables -vnL
sudo iptables -vnL INPUT
sudo iptables -t nat -vnL
sudo iptables -t nat -vnL POSTROUTING
```
### Changing Chain Default Policies
```
sudo iptables -P FORWARD DROP
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT DROP
```
### Applying Rules to IP ranges
```
sudo iptables -t filter -A OUTPUT -p icmp -m iprange --dst-ip 192.168.0.1-192.168.0.150 -j DROP
sudo iptables -t filter -A OUTPUT -p tcp --dport 25 -m iprange 10.10.10.1-10.10.10.254 -j DROP
```
### Applying Rules to Address Type
```
sudo iptables -t filter -A INPUT -m addrtype --src-type UNICAST -j DROP
sudo iptables -t filter -A OUPUT -m addrtype --dst-type BROADCAST -j ACCEPT
```
### Filtering by single port
```
sudo iptables -A INPUT --sport 22 -j DROP
sudo iptables -A OUTPUT --dport 445 -j DROP
```
### Filtering by multiple ports
```sudo iptables -A OUTPUT -m multiport --dport 80,443 -j DROP```

### Accepting Traffic From A Specific Interface
#### -i: incoming interface
```sudo iptables -A [chain] -i [interface] -j [target]```

#### -o: outgoing interface
```sudo iptables -A [chain] -o [interface] -j [target]```

#### Example: Accepting Lookback Interface Traffic
```
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT
```
### Negation Match Options
#### drop all ssh traffic from all ip addresses except 192.168.30.150
```sudo iptables -A INPUT ! -s 192.168.30.150 -p tcp --dport 22 -j DROP```

### dropping all from communcation from all devices that do not have a matching mac address of aa:bb:cc:dd:ee:ff
```iptables -A INPUT -m mac ! --mac-source aa:bb:cc:dd:ee:ff -j DROP```
Filter Packets by TCP Flags
### drop all packets to port 22 (ssh) that contain a tcp syn flag
```sudo iptables -A INPUT -p tcp --dport 22 --syn -j DROP```

### accept all packets that have SYN ACK tcp flags
```iptables -A OUTPUT -p tcp --tcp-flags syn,ack,rst,fin syn,ack -j ACCEPT```

Stateful Firewalls: Connection Tracking
Packet States:

NEW > the first packet from a connection
ESTABLISHED > packets that are part of an existing connection
RELATED > packets that are requesting a new connection and are already part of an existing connection
INVALID > packets that are not part of an any existing connection
UNTRACKED > packets marked within the raw table with a NOTRACK target

accept all inbound packets that are part of an existing connection
or that are part of an existing connection and would like to
establish a new connection
```sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT```

### Configuring a Stateful Firewall: Bash Script
```
#!/bin/bash

iptables_version = $(iptables -V)
is_installed = $?

state_firewall() {
    if [[ "$is_installed" -ne "0" ]]
    then
        iptables -F

        iptables -A INPUT -i lo -j ACCEPT
        iptables -A OUTPUT -o lo -j ACCEPT

        iptables -A INPUT -m state --state INVALID -j DROP
        iptables -A OUTPUT -m state --state INVALID -j DROP

        iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
        iptables -A OUTPUT -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT

        iptables -P INPUT DROP
        iptables -P OUTPUT DROP
    else
        echo "Iptables must be installed in order to set up a statefull firewall"
}

state_firewall
```

### Filter Packets By MAC Address
 filter incoming traffic on wlan0 from a particular MAC address
```sudo iptables -A INPUT -i wlan0 -m mac --mac-source [mac] -j DROP```
Filter Packets by Date And Time
### accept ssh packets from 10am to 2pm
```sudo iptables -A INPUT -p tcp -m time --timestart 10:00 --timestop 14:00 -j ACCEPT```

### drop all packets that fail to meet the requirement in the rule above
sudo iptables -A INPUT -p --dport 22 -j DROP
### Denial-of-Service Protection
if more than 5 tcp syn packets are sent to port 25,
reject packets by sending tcp rst packets
```sudo iptables -A INPUT -p tcp --dport 25 --syn -m connlimit --connlimit-above 5 -j REJECT --reject-with tcp-rst```
### Using Limit for Packets Filtering
rule to accept 7 new tcp syn packets no matter the time frame,
and then only accept 2 tcp syn packets after the first 7 tcp syn
packets have been accepted
```sudo iptables -A INPUT -p tcp --syn -m limit --limit 2/s --limit-burst 7 -j ACCEPT```
### Creating blacklist
```
#!/bin/bash

iptables -F

# if packets are sent within 60 seconds with a src ip
# that is found in the hackers blacklist created in the 
# second rule, drop the packet. If no packets from an ip in 
# the blacklist are sent within 60 seconds, any packets after
# the 60 are accepted
iptables -A INPUT -m recent --name hackers --update --seconds 60 -j DROP
# if any packets bound for ssh are detected between 8am and 10pm,
# create a blacklist called hackers and as the src ip to the list 
iptables -A INPUT -p tcp --dport 25 -m time --timestart 8:00 --timestop 22:00 \
-m recent --name hackers --set -j DROP
```
### Accepting packets up to a particular quota
#### limiting the amount of bytes from the destination ip on http to 1gb
```sudo iptables -A INPUT -p tcp --sport 80 -d 234.24.5.6 -m quota --quota 1000000000 -j ACCEPT```
#### if more than 1gb of data is requested, drop the packets
```sudo iptables -A INPUT -p tcp --sport 80 -d 234.24.5.6 -j DROP```

## For more on IP tables, check out this Udemy course where most of the example of this cheat sheet came from: https://www.udemy.com/course/linux-security-the-complete-iptables-firewall-guide/
