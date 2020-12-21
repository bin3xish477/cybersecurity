#!/usr/bin/env python3

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from os import urandom
from sys import argv, exit

def generating_scrypt_key(key):
    salt = urandom(16)
    """
    length: how long the key will be after the process is finished
    n : CPU/memory cost parameter
    r: block size parameter
    p: threads to run in parallel 

    n should be a number divisible by 2. For operations that
    require less wait time (such as a login request), 2**14 is
    suggested. For operations that are more sensitive, 2**20 is suggested.
    """
    key_derivation_func = Scrypt(salt=salt, length=32,
                            n=2**14, r=8, p=1,
                            backend=default_backend())
    key = key_derivation_func.derive(b"deriveFromPasswor")
    return key

if __name__ == "__main__":
    if len(argv) < 2:
        print(f"Usage: {__file__} <password_to_generate_key_for>")
        exit(1)
    password = argv[1]
    key = generating_scrypt_key(password).hex()
    print(key)
