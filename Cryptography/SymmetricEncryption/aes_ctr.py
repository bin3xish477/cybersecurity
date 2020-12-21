#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes
from dataclasses import dataclass
from typing import Callable

# AES CTR is a stream cipher so 
# it does not require padding
@dataclass
class AES_CTR(object):
    key: bytes = token_bytes(32)
    nonce: bytes = token_bytes(16)
    ctr_cipher = Cipher (
                        algorithms.AES(key),
                        modes.CTR(nonce),
                        backend=default_backend()
                 )
    encryptor: Callable = ctr_cipher.encryptor()
    decryptor: Callable = ctr_cipher.decryptor()
    
    def encrypt(self, plaintext: bytes) -> bytes:
        return self.encryptor.update(plaintext)
    
    def finalize_encryptor(self):
        return self.encryptor.finalize()

    def decrypt(self, ciphertext: bytes) -> bytes:
        return self.decryptor.update(ciphertext)

    def finalize_decryptor(self):
        return self.decryptor.finalize()

if __name__ == "__main__":
    cipher = AES_CTR()

    plaintexts = [
        b"SHORT",
        b"MEDIUM MEDIUM MEDIUM",
        b"LONG LONG LONG LONG LONG LONG"
    ]
    
    ciphertexts = []
    for p in plaintexts:
       ciphertexts.append(cipher.encrypt(p)) 
    ciphertexts.append(cipher.finalize_encryptor())

    print(">"*25, "Plaintext", "<"*25)
    for c in ciphertexts:
        print(cipher.decrypt(c))
    print(cipher.finalize_decryptor())
