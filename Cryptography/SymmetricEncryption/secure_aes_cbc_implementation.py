#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from dataclasses import dataclass
from secrets import token_bytes
from typing import Callable

@dataclass
class EncryptionManager(object):
    key: bytes = token_bytes(32)
    iv: bytes = token_bytes(16)
    c: Cipher = Cipher(
                    algorithms.AES(key),
                    modes.CBC(iv),
                    backend=default_backend()
            )
    encryptor: Callable = c.encryptor()
    decryptor: Callable = c.decryptor()
    padder: Callable = PKCS7(128).padder()
    unpadder: Callable = PKCS7(128).unpadder()
    
    def update_encryptor(self, plaintext: bytes) -> bytes:
        return self.encryptor.update(self.padder.update(plaintext))
    
    def finalize_encryptor(self):
        return self.encryptor.update(self.padder.finalize()) \
        + self.encryptor.finalize()
    
    def update_decryptor(self, ciphertext: bytes) -> bytes:
        return self.unpadder.update(self.decryptor.update(ciphertext))
                    
    def finalize_decryptor(self) -> bytes:
        return self.unpadder.update(self.decryptor.finalize()) \
        + self.unpadder.finalize()

if __name__ == "__main__":
    manager = EncryptionManager()

    text = [
        b"SHORT SHORTSHORT",
        b"MEDIUM MEDIUM MEDIUM",
        b"LONG LONG LONG LONG LONG LONG"
    ]

    ciphertexts = []
    for t in text:
        ciphertexts.append(manager.update_encryptor(t))
    ciphertexts.append(manager.finalize_encryptor())

    for c in ciphertexts:
        print(manager.update_decryptor(c))
    print(manager.finalize_decryptor())

