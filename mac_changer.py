





#!/usr/bin/env python

import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--interface', dest='interface', help='Interface whose MAC address you want to alter')
    parser.add_option('-m', '--mac', dest='new_mac', help='Desired MAC address. Note: first number should be even.')
    (options, arguments) = parser.parse_args()
    if not options.interface or not options.new_mac:
        parser.error('[-] You forgot to enter the interface or MAC address, --help for more info')
    return options


def change_mac(interface, new_mac='00:11:22:33:44:55'):
    print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)

    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['sudo', 'ifconfig',  interface])
    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_result:
        return mac_address_result.group(0)
    else:
        print("[-] Couldn\'t read MAC address.")

options = get_args()

current_mac = get_current_mac(options.interface)
print("Current MAC : " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully altered to : " + str(current_mac))
else:
    print("[-] MAC address did not change")

    
    
