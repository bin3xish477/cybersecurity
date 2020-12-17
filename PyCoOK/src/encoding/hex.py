from hexdump import hexdump
from os.path import exists, isfile

class Hex:
    def __init__(self, stdin):
        self.stdin = stdin

    def hx(self):
        return bytes(self.stdin, "utf8").hex()

    def from_hx(self):
        return bytes.fromhex(self.stdin).decode("utf-8")

    def hxd(self):
        if exists(self.stdin) and isfile(self.stdin):
            with open(self.stdin, "rb") as f:
                d = f.read()
                hexdump(d)
        else: hexdump(bytes(self.stdin, "utf8"))

