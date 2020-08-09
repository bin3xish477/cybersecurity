#!/usr/bin/env python3
from scapy.all import *
from time import sleep

TARGET_IP  = ""
TARGET_MAC = ""
FAKE_IP    = ""
FAKE_MAC   = ""


if __name__ == "__main__:
    frame = Ether()
    arp = ARP()

    while True:
        sendp()
        print("[+] Fake ARP Request Sent")
        sleep(5)
