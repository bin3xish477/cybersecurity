from sys import exit

class PatternCreate:
    def __init__(self, pattern_len: int):
        self.pattern_len = pattern_len

    def create(self):
        if self.pattern_len > 20280:
            print("[-] pattern length cannot be larger than 20280 bytes")
            exit(0)

        UPPERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        LOWERS = "abcdefghijklmnopqrstuvwxyz"
        DIGITS = "0123456789"
        pattern = ""

        for digit in DIGITS:
            for lower in LOWERS:
                for upper in UPPERS:
                    if len(pattern) > self.pattern_len:
                        return pattern
                    pattern += (digit+lower+upper)

