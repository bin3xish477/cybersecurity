#!/usr/bin/env python3
from argparse import ArgumentParser 
from os.path import exists, isfile
from sys import exit
from random import randint

def parse_ident_array(e_ident):
    magic = ''.join([hex(b)[2:] for b in e_ident[:4]])
    print("Magic Bytes:", magic)

    if (arch := e_ident[4]) == 0x1:
        print("Architecture:", "32-bit")
    elif arch == 0x2:
        print("Architecture:", "64-bit")

    if (endianness := e_ident[5]) == 0x1:
        print("Endianness:", "little-endian")
    elif endiannes == 0x2:
        print("Endianness:", "big-endian")

    if (elf_version := e_ident[6]) == 1:
        print("Version: 1")
        
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("FILE",help="ELF binary file to parse executable header for")
    args = parser.parse_args()
    f = args.FILE
    if (not exists(f) or not isfile(f)):
        print(f"[-] {f} does not exists or is not a file...")
        exit()
    print(f"\nFile: {f}\n")
    with open(f, "rb") as elf:
        header = elf.read()[:64]
        if header[:4].hex() != '7f454c46':
            print(f"[-] {f} is not an ELF binary...")
            exit(1)

        e_ident = header[:16]
        parse_ident_array(e_ident)

        if (e_type := header[16]) == 0x1:
            print("Type: Relocatable File")
        elif e_type == 0x2:
            print("Type: Executable File")
        else:
            print("Type: Shared Object File")

        e_machine = header[17:19]
        e_machine = int('0x' + hex(e_machine[0])[2:]+hex(e_machine[1])[2:], 16)
        if e_machine == 3:
            print("Machine: Intel 80386")
        elif e_machine == 40:
            print("Machine: Intel 80386")
        elif e_machine == 62:
            print("Machine: AMD x86-64 architecture")

