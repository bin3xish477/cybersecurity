#!/usr/bin/env python




import scapy.all as scapy

packet_ = scapy.ARP(op=2, pdst="10.0.2.6", hwdst="08:00:27:e6:e5:59", psrc="10.0.2.1")
print(packet_.show())
print(packet_.summary())
