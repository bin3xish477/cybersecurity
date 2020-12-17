from src.pattern.create import PatternCreate
from sys import exit

class PatternOffset:
    def __init__(self, s: str):
        self.string_to_find = bytes.fromhex(s).decode('utf-8')[::-1]

    def offset(self):
        p = PatternCreate(20000).create()
        if (offset := p.find(self.string_to_find)) == -1:
            print(f"[-] Could not find offset for {self.string_to_find}")
            exit(0)
        else: return offset
