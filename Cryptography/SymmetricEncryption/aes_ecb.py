#!/usr/bin/env python3
"""
This program is using AES in ECB mode. 
ECB, or the Electronic Code Book mode,
is utterly insecure so do not use it for
production purposes.
"""
from secrets import token_bytes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from sys import argv, exit

def create_aes_cipher() -> Cipher:
    key: bytes = token_bytes(16)
    cipher = Cipher(algorithms.AES(key),
                    modes.ECB(),
                    backend=default_backend())
    return cipher

# AES ECB is a block cipher, so attempting
# to encrypt or decrypt a byte string less than
# 16 bytes will return an empty byte string
def encrypt(plain_t: bytes, c: Cipher) -> bytes:
    encryptor = c.encryptor()
    return encryptor.update(plain_t)

def decrypt(cipher_t: bytes, c: Cipher) -> bytes:
    decryptor = c.decryptor()
    return decryptor.update(cipher_t)

if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Usage: {__file__} <string_to_encrypt_and_decrypt>")
        exit(1)

    msg = argv[1]
    # adding "P" as padding is data chunks 
    # arent not 16 bytes in length
    msg += "P" * (-len(msg) % 16)
    msg = bytes(msg, "utf-8")
    c: Cipher = create_aes_cipher()

    cipher_t = encrypt(msg, c)
    print(f"Encrypted message: {cipher_t}")    
    plain_t = decrypt(cipher_t, c)
    print(f"Decrypted message: {plain_t}")
        
