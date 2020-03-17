#!/usr/bin/env python3

from scapy.all import *
from sys import argv
from colored import fg, attr

# limit verbose mode
conf.verb = 0

def send_ping(ip):
    """
    Send an ICMP request to a host machine
    
    :parameter:
        ip (str): the target's ipv4 address
    
    """
    # send and receive packets
    response= sr1(IP(dst=ip, ttl=10)/ICMP(), timeout=1)
    # if machine answered, print confirmation message
    if response != None:
        print(f'%s{ip} is up!%s' % (fg(1), attr(0)))


def main():
    subnet = argv[1]
    
    for num in range(1, 256):
        send_ping(subnet + '.' + str(num))


if __name__ == '__main__':
    main()
    
