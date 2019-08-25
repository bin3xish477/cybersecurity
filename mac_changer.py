#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option('-i', '--interface', dest='interface', help='Interface whose MAC address you want to alter')
parser.add_option('-m', '--mac', dest='new_mac', help='Desired MAC address')
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print('[+] Changing Mac address for ' + interface + ' to ' + new_mac)

subprocess.call(['sudo', 'ifconfig', interface, 'down'])
subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['sudo', 'ifconfig', interface, 'up'])
