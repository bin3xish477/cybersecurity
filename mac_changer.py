#!/usr/bin/env python

import subprocess

interface = 'wlan0'
new_mac = '00:11:22:33:44:55'

print('[+] Changing Mac address for ' + interface + ' to ' + new_mac)
subprocess.call('ifconfig ' + interface + ' down', shell=True)
subprocess.call('ifconfig ' + interface + ' hw ether ' + new_mac, shell=True)
subprocess.call('ifconfig ' + interface + ' up', shell=True)
