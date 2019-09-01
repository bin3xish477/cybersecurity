#!/usr/bin/env python

"""
***********************************************************
Title :       network_scanner.py
Author :      Alexis Rodriguez
Created on :  August 31th, 2019
Description : Scans network.
Purpose :     Uses the subprocess, optparse, and re modules
              to call system commands, customize build
              commands, and extract data using regular
              expressions, ultimately providing all the
              information needed to altar a network
              interface's MAC address.
Build with :  sudo python mac_changer.py -i [interface] 
              -m [MAC]
***********************************************************
"""

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_req_broad, timeout=1)

    for value in answered_list:
        print("IP : " + value[1].psrc)
        print("MAC : " + value[1].hwsrc)
        print("------------------------------")


scan("10.0.2.1/24")

