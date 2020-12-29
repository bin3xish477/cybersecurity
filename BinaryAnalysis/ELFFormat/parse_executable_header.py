#!/usr/bin/env python3
from colored import fg, attr
from argparse import ArgumentParser 
from os.path import exists, isfile
from sys import exit
from random import randint
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("FILE",help="ELF binary file to parse executable header for")
    args = parser.parse_args()
    f = args.FILE
    color = lambda s: "%s%s%s" % (fg(randint(1,220)), s,  attr(0))
    if (not exists(f) or not isfile(f)):
        print(f"[-] {color(f)} does not exists or is not a file...")
        exit(1)
