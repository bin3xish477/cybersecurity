#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes
from typing import Callable

class CTRFromECB:
    def __init__(self, key, nonce, block_size):
        self.key: bytes = key
        self.nonce: bytes = nonce
        self.block_size: int = block_size
        cipher = Cipher(
                        algorithms.AES(self.key),
                        modes.ECB(),
                        backend=default_backend()
                )
        self.encryptor: Callable = cipher.encryptor()
        self.decryptor: Callable = cipher.decryptor()

    def byte_xor(self, string1: bytes, string2: bytes) -> bytes:
        return bytes([a ^ b for a, b in zip(byte_string1, byte_string2)])

    def keystream(self, n: int, decrypt: bool=False) -> bytes
        if decrypt:
            return self.decryptor.update(self.nonce + bytes(n)) 
        return self.encryptor.update(self.nonce + bytes(n))
        
    @property
    def ciphertext(self) -> str:
        return "\n".join(map(str, self.ciphertext_list))

    def encrypt(self, plaintext: bytes):
        if not hasattr(self, "ciphertext_list"):
            self.ciphertext_list = []
        for i in range(0, len(plaintext), 16):
           keystr = self.keystream(i)
           ciphertxt = self.byte_xor(plaintext[i:i+block_size], keystr)
           self.ciphertext_list.append(ciphertxt)
    
    @property
    def plaintext(self) -> str:
        return "\n".join(map(str, self.plaintext_list))

    def decrypt(self):
        if not hasattr(self, "plaintext_list"):
            self.plaintext_list = []
        counter = 0
        for c in self.ciphertext_list:
            keystr = self.keystream(counter)
            plaintext = self.byte_xor(c, keystr)
            self.plaintext_list.append(plaintext)

if __name__ == "__main__":
    key, nonce = token_bytes(32), token_bytes(16)
    block_size = 16
    ctr_obj = CTRFromECB(key, nonce, block_size)
    
    plaintexts = [
        b"SHORT",
        b"MEDIUM MEDIUM MEDIUM",
        b"LONG LONG LONG LONG LONG LONG"
    ]

    for p in plaintexts:
        ctr_obj.encrypt(p)

    print(">"*25, "Ciphertext", "<"*25)
    print(ctr_obj.ciphertext, "\n")

    ctr_obj.decrypt()
    print(">"*25, "Plaintext", "<"*25)
    print(ctr_obj.plaintext)
