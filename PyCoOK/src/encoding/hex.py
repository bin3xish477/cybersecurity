from hexdump import hexdump
from os.path import exists, isfile

def hx(s: str):
    return bytes(s, "utf").hex()

def hxd(s: str):
    if exists(s) and isfile(s):
        with open(s, "rb") as f:
            d = f.read()
            hexdump(d)
    else:
        hexdump(bytes(s, "utf8"))

