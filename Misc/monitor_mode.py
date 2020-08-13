#!/usr/bin/env python

"""
************************************************************
Title :       monitor_mode.py
Author :      Alexis Rodriguez
Created on :  August 25th, 2019
Description : sets a preferred interface into monitor mode
Purpose :     Uses the subprocess and optparse module to call
              system commands and parsing command-line options.
Build with :  python monitor_mode.py -i [interface] -m[mode]
************************************************************
"""

import subprocess
import optparse


def get_args():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--interface', dest='interface', help='Name of interface whose mode will be changed')
    parser.add_option('-m', '--mode', dest='mode', help='Mode the interface will be changed into')
    (options, arguments) = parser.parse_args()

    if not options.interface or not options.mdoe:
        parser.error('[-] You forgot to provide an interface or mode, --help for more info')
    return options


def to_monitor_mode(interface, mode):
    print('[+] ' + interface + ' has been set to mode ' + mode)

    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'airmon-ng', 'check', 'kill'])
    subprocess.call(['sudo', 'iwconfig', interface, 'mode', mode])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
    subprocess.call(['sudo', 'service', 'network-manager', 'start'])


options = get_args()
to_monitor_mode(options.interface, options.mode)
