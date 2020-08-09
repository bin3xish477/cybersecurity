#!/usr/bin/env python3
from scapy.all import *
from time import sleep

TARGET_IP  = ""
TARGET_MAC = ""
FAKE_IP    = "11.22.33.44"
FAKE_MAC   = "aa:bb:cc:dd:ee:ff"


if __name__ == "__main__:
    frame = Ether()
    arp = ARP()

    while True:
        sendp()
        print("[+] Fake ARP Request Sent")
        sleep(5)
