#!/usr/bin/env python

import subprocess
import optparse


def get_args():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--interface', dest='interface', help='Interface whose MAC address you want to alter')
    parser.add_option('-m', '--mac', dest='new_mac', help='Desired MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface or not options.new_mac:
        parser.error('[-] You forgot to enter the interface or MAC address, --help for more info')
    return options


def change_mac(interface, new_mac='00:11:22:33:44:55'):
    print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)

    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])


options = get_args()
change_mac(options.interface, options.new_mac)
