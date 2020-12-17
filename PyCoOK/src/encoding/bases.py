from base64 import (
    b85encode, b85decode,
    b64encode, b64decode,
    b32encode, b32decode,
    b16encode, b16decode
)

class Bases:
    def __init__(self, stdin: str):
        self.stdin = stdin

    def eighty_five(self):
        return b85encode(bytes(self.stdin, "utf8")).decode()

    def eighty_five_decode(self):
        return b85decode(bytes(self.stdin, "utf8")).decode()

    def sixty_four(self):
        return b64encode(bytes(self.stdin, "utf8")).decode()

    def sixty_four_decode(self):
        return b64decode(bytes(self.stdin, "utf8")).decode()

    def thirty_two(self):
        return b32encode(bytes(self.stdin, "utf-8")).decode()

    def thirty_two_decode(self):
        return b32decode(bytes(self.stdin, "utf8")).decode()

    def sixteen(self):
        return b16encode(bytes(self.stdin, "utf8")).decode()

    def sixteen_decode(self):
        return b16decode(bytes(self.stdin, "utf8")).decode()
