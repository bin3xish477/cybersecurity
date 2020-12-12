from base64 import (
    b85encode, b85decode,
    b64encode, b64decode,
    b32encode, b32decode,
    b16encode, b16decode
)

def eighty_five(s: str):
    return b85encode(bytes(s, "utf8")).decode()

def eighty_five_decode(s: str):
    return b85decode(bytes(s, "utf8")).decode()

def sixty_four(s: str):
    return b64encode(bytes(s, "utf8")).decode()

def sixty_four_decode(s: str):
    return b64decode(bytes(s, "utf8")).decode()

def thirty_two(s: str):
    return b32encode(bytes(s, "utf-8")).decode()

def thirty_two_decode(s: str):
    return b32decode(bytes(s, "utf8")).decode()

def sixteen(s: str):
    return b16encode(bytes(s, "utf8")).decode()

def sixteen_decode(s: str):
    return b16decode(bytes(s, "utf8")).decode()
