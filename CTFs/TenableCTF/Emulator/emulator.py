#!/usr/bin/env python3

class Emulator:
    def __init__(self):
        self.TRX = "GED\x03hG\x15&Ka =;\x0c\x1a31o*5M"
        self.DRX = ""
        self.registers = ("TRX", "DRX")

    def _xor(self, dst, src):
        dst_len, src_len = len(dst), len(src)
        result = ""
        if dst_len > src_len:
            for i in range(dst_len):
                try:
                    result += chr(ord(dst[i]) ^ ord(src[i]))
                except IndexError:
                    result += dst[i:]
                    break
        else:
            for i in range(src_len):
                try:
                    result += chr(ord(dst[i]) ^ ord(src[i]))
                except IndexError:
                    result += src[i:]
                    break
        return result

    def xor(self, dst, src):
    	if dst == "TRX" and src == "DRX":
    		self.TRX = self._xor(self.TRX, self.DRX)
    	elif dst == "DRX" and src == "TRX":
        	self.DRX = self._xor(self.DRX, self.TRX)
        elif dst == "DRX" and src == "DRX":
        	self.DRX = self._xor(self.DRX, self.DRX)

    def mov(self, dst, src):
        if dst == "TRX" and src == "DRX":
            self.TRX = self.DRX
        elif dst == "DRX" and src == "TRX":
            self.DRX = self.TRX
        elif dst == "TRX" and src not in self.registers:
            self.TRX = src
        elif dst == "DRX" and src not in self.registers:
            self.DRX = src

    def reverse(self, dst):
        if dst == "TRX":
            self.TRX = self.TRX[::-1]
        else:
            self.DRX = self.DRX[::-1]

def main():
    emulator = Emulator()
    instructions = list(map(lambda l: l.strip(), open("Crypto.asm").readlines()))
    for instruction in instructions:
        instruction = list(map(lambda s: s.strip("\""), instruction.split()))
        if instruction[0] == "MOV":
           emulator.mov(instruction[1], instruction[2])
        elif instruction[0] == "XOR":
        	emulator.xor(instruction[1], instruction[2])
        elif instruction[0] == "REVERSE":
            emulator.reverse(instruction[1])

    #testing
    """
    print([chr(c) for c in emulator._xor(b"shadow", b"dogs")])
    emulator.TRX = b"shadow"
    emulator.DRX = b"dogs"
    emulator.mov("TRX", "DRX")
    print(emulator.TRX)
    emulator.TRX = b"hotdog"
    emulator.reverse("TRX")
    print(emulator.TRX)
    """

    flag = "".join(emulator.TRX)
    print(flag)

main()
