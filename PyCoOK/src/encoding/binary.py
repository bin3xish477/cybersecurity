class Binary:
    def __init__(self, stdin):
        self.stdin = stdin

    def to_bin():
        return ''.join('{:08b}'.format(ord(c)) for c in self.stdin)

    def from_bin():
        return ''.join(chr(int(self.stdin[i:i+8], 2)) for i in range(0, len(self.stdin), 8))
