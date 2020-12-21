#!/usr/bin/env python3

########################################
# This file implements an intentionally
# vulnerable implementation of RSA. 
# Do not use this implementation for
# secure operations.
########################################

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from gmpy2 import powmod

def rsa_encrypt(m:int, publickey) -> int:
    nums = publickey.public_numbers()
    # powmod is short for power and modulus
    # encrypting a message simply involves taking
    # the message and raising it to the power of e
    # and then doing mod n on the resulting value
    return powmod(m, nums.e, nums.n)

def rsa_decrypt(c: int, privatekey) -> int:
    nums = privatekey.private_numbers()
    return powmod(c, nums.d, nums.public_numbers.n)

def int_to_bytes(i: int) -> bytes:
    """returns the bytes string converted from an integer"""
    i = int(i)
    return i.to_bytes(i.bit_length()+7//8, byteorder="big")

def bytes_to_int(msg: bytes) -> int:
    """RSA needs to operate on integers so this function
    will simply return the integer representation of the
    byte string passed an argument.
    """
    return int.from_bytes(msg, byteorder="big")
    
if __name__ == "__main__":
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    plaintext = b"Every moment is a fresh beginning"

    plaintext_as_int = bytes_to_int(plaintext)
    #print(plaintext_as_int)
    ciphertext = rsa_encrypt(plaintext_as_int, public_key)
    print("#"*70, "Ciphertext")
    print(int_to_bytes(ciphertext))
    print()
    plaintext = rsa_decrypt(ciphertext, private_key)
    print("#"*70, "Plaintext")
    print(int_to_bytes(plaintext).decode('ascii'))
