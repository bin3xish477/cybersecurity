#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes

def generate_cipher(key: bytes, iv: bytes) -> Cipher:
    """
    Notice the difference here between generating 
    the CBC cipher as opposed to the ECB cipher
    is the use of the initialization vector (iv)
    which is passed as an argument to modes.CBC()
    """
    cipher: Cipher = Cipher(
                    algorithms.AES(key),
                    modes.CBC(iv),
                    backend=default_backend()
                    )
    return cipher

if __name__ == "__main__":
    key: bytes = token_bytes(32)
    iv: bytes = token_bytes(16)
    c: Cipher = generate_cipher(key, iv)
    encryptor, decryptor = c.encryptor(), c.decryptor()

    # creating a padder/unpadder for a 128 block size
    padder = PKCS7(128).padder()
    unpadder = PKCS7(128).unpadder()

    plain_ts = [
        b"SHORT",
        B"MEDIUM MEDIUM MEDIUM",
        b"LONG LONG LONG LONG LONG LONG"
    ]

    cipher_ts = []

    for text in plain_ts:
        padded_text = padder.update(text) 
        cipher_ts.append(encryptor.update(padded_text))
    cipher_ts.append(encryptor.update(padder.finalize()))

    for cipher in cipher_ts:
        padded_text = decryptor.update(cipher)
        print("Recovered:", unpadder.update(padded_text))
    print("Recovered:", unpadder.finalize())
        

