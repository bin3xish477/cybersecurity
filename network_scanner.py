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
Build with :  sudo python network_scanner.py -t [target IP]
***********************************************************
"""

import scapy.all as scapy
import optparse


def command_line_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP/ IP range")
    opts, arguments = parser.parse_args()
    return opts


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_request
    answered_list = scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]

    def print_results():
        for value in answered_list:
            client_dict = dict()
            client_dict["IP"] = value[1].psrc
            client_dict["MAC"] = value[1].hwsrc
            print(client_dict)
            print("--------------------------------------------")
    print_results()


options = command_line_args()
scan(options.target)
