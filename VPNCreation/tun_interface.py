#!/usr/bin/env python3
from fcntl import ioctl
from struct import pack
from scapy.all import *
from os import read, write, open, O_RDWR
from subprocess import run

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002
IFF_NO_PI = 0x1000

def main():
    tun = open("/dev/net/tun", O_RDWR)
    ifr = pack("16sH", b"tun%d", IFF_TUN | IFF_NO_PI)
    ifname_bytes = ioctl(tun, TUNSETIFF, ifr)
    ifname = ifname_bytes.decode("UTF-8")[:16].strip("\x00")
    run(f"ip addr add 192.168.53.100/24 dev {ifname}", shell=True)
    run(f"ip link set dev {ifname} up", shell=True)
    print(f"VPN TUN INTERFACE: {ifname}") 


    while True:
        packet = read(tun, 2048)
        if True:
            ip = IP(packet)
            ip.show()

            newip = IP(src="1.2.3.4", dst=ip.src)
            newpkt = newip/ip.payload
            write(tun, bytes(newpkt))

if __name__ == "__main__":
    main()
