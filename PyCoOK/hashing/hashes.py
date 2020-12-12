from hashlib import (
    md5, sha1, sha224,
    sha256, sha384, sha512,
    blake2b, blake2s, sha3_224,
    sha3_256, sha3_384, sha3_512,
    shake_128, shake_256
)

from chilkat import CkCrypt

crypt = chilkat.CkCrypt2()

s = "The quick brown fox jumps over the lazy dog"
crypt.put_HashAlgorithm("md2")
h = crypt.hashStringENC(s)
print("MD2: " + h)


