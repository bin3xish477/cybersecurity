#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class Oracle:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def accept(self, ciphertext):
        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CBC(self.iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext)
        plaintext += decryptor.finalize()
        # return if the padding size = 15
        return plaintext[-1] == 15
        
def sslv3Pad(msg:bytes) -> bytes:
    """Implements an insecure padding techqinue
    used in some of the earlier versions of SSl
    """
    pad_needed = (16-(len(msg)%16)) - 1
    padding = pad_needed.to_bytes(pad_needed+1, "big")
    return msg+padding

def sslv3Unpad(padded_msg:bytes) -> bytes:
    # the last element contains the byte
    # representing the total number of padding
    # bytes - 1. Indexing byte string actually 
    # returns their integer value which is 
    # why we can add 1
    padding_len = padded_msg[-1] + 1
    return padded_msg[:-padding_len]

if __name__ == "__main__":
    pass
