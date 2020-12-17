from hashlib import (
    md5, sha1, sha224,
    sha256, sha384, sha512,
    blake2b, blake2s, sha3_224,
    sha3_256, sha3_384, sha3_512,
    shake_128, shake_256
)
from os.path import exists, isfile

class Hashes:
    def __init__(self, stdin: str, hash_functions: list):
        self.stdin = stdin
        self.hash_functions

    def get_hash(self):
        if exists(self.stdin) and isfile(self.stdin):
            print(f"File: {self.stdin}")
            with open(self.stdin, "rb") as f:
                self.stdin  = f.read()

        if type(self.stdin) == str:
            self.stdin = bytes(self.stdin.strip(), "utf8")

        for h in self.hash_functions:
            if h == "md5": yield ("MD5:", md5(self.stdin).hexdigest())
            if h == "sha1": yield ("SHA1:", sha1(self.stdin).hexdigest())
            if h == "sha224": yield ("SHA224:", sha224(self.stdin).hexdigest())
            if h == "sha256": yield ("SHA256:", sha256(self.stdin).hexdigest())
            if h == "sha384": yield ("SHA256:", sha384(self.stdin).hexdigest())
            if h == "sha512": yield ("SHA512:", sha512(self.stdin).hexdigest())
            if h == "sha3_224": yield ("SHA3_224:", sha3_224(self.stdin).hexdigest())
            if h == "sha3_256": yield ("SHA3_256:", sha3_256(self.stdin).hexdigest())
            if h == "sha3_384": yield ("SHA3_384:", sha3_384(self.stdin).hexdigest())
            if h == "sha3_512": yield ("SHA3_512", sha3_512(self.stdin).hexdigest())
            if h == "blake2b": yield ("BLAKE2B:", blake2b(self.stdin).hexdigest())
            if h == "blake2s": yield ("BLAKE2S:", blake2s(self.stdin).hexdigest())

