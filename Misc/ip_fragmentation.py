#!/usr/bin/env python3
from scapy.all import *

ID = 1000
dst_ip = "192.168.33.138"

def ip_fragmentation():
	# constructing udp packet
	udp = UDP(sport=7777, dport=4444, chksum=0)
	"""
	8 = UDP header fixed byte size
	32 = size of first packet
	40 = size of second packet
	20 = size of third packet
	"""
	udp.len = 8 + 32 + 40 + 20

	"""
	if flags = 1:
		there are still more fragments
	elif flags = 0:
		the current fragment is the last fragment

	frag = fragment offset from the the zeroth byte
	"""

	# constructing and sending first fragment
	ip = IP(dst=dst_ip, id=ID, frag=0, flags=1)
	payload = "A"*31 + "\n"
	pkt = ip/udp/payload
	print("[*] Sending first fragment...")
	send(pkt, verbose=0)

	# ip.proto = 17 means protocol is UDP
	# constructing and sending second fragment
	ip = IP(dst=dst_ip, id=ID, frag=5, flags=1)
	ip.proto = 17
	payload = "B"*39 + "\n"
	pkt = ip/payload
	print("[*] Sending second fragment...")
	send(pkt, verbose=0)

	# constructing and sending third and last fragment
	ip = IP(dst=dst_ip, id=ID, frag=10, flags=0)
	ip.proto = 17
	payload = "C"*19 + "\n"
	pkt = ip/payload
	print("[*] Sending third fragment...")
	send(pkt, verbose=0)

if __name__ == "__main__":
	ip_fragmentation()
