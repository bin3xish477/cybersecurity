#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option('-i', '--interface', dest='interface', help='Name of interface whose mode will be changed')
parser.add_option('-m', '--mode', dest='mode', help='Mode the interface will be changed into')

(options, arguments) = parser.parse_args()

interface = options.interface
mode = options.mode

print('[+] ' + interface + ' has been set to mode ' + mode)

subprocess.call(['sudo', 'ifconfig', interface, 'down'])
subprocess.call(['sudo', 'airmon-ng', 'check', 'kill'])
subprocess.call(['sudo', 'iwconfig', interface, 'mode', mode])
subprocess.call(['sudo', 'ifconfig', interface, 'up'])
