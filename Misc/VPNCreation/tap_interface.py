#!/usr/bin/env python3
from fcntl import ioctl
from struct import pack
from os import read, write, open, O_RDWR
from scapy.all import *
from subprocess import run

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002
IFF_NO_PI = 0x1000

def main():
    tun = os.open("/dev/net/tun", O_RDWR)
    ifr = pack("16sH", b"tap%d", IFF_TAP | IFF_NO_PI)
    ifname_bytes = ioctl(tun, TUNSETIFF, ifr)
    ifname = ifname_bytes.decode("UTF-8")[:16].strip("\x00")
    print(f"VPN TAP INTERFACE: {ifname}")

    run(f"ip addr add 192.168.22.50/24 dev {ifname}", shell=True)
    run(f"ip link set dev {ifname} up", shell=True)

    while True:
        packet = read(tun, 2048)
        if True:
            ether = Ether(packet)
            ether.show()

            newether = Ether(src="aa:bb:cc:aa:bb:cc", dst=ether.src)
            newpkt = newether/ether.payload
            write(tun, bytes(newpkt))

if __name__ == "__main__":
    main()

