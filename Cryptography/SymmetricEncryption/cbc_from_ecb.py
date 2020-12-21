#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes
from typing import Callable, List
from dataclasses import dataclass

@dataclass
class CBCFromECB(object):
    key: bytes = token_bytes(32)
    iv: bytes = token_bytes(16)
    block_size = 16
    c: Cipher = Cipher(
                    algorithms.AES(key),
                    modes.ECB(),
                    backend=default_backend()
                )
    encryptor: Callable = c.encryptor()
    decryptor: Callable = c.decryptor()
    padder: Callable = PKCS7(128).padder()
    unpadder: Callable = PKCS7(128).unpadder()
    iv_utilized: bool = False

    def byte_xor(self, str1: bytes, str2: bytes) -> bytes:
        return bytes(a ^ b for a, b in zip(str1, str2))

    @property
    def ciphertext(self):
        if hasattr(self, "ctexts"):
            return "\n".join(map(str, self.ctexts))
        else:
            raise AttributeError(
                "Must invoke `encrypt` before accessing ciphertext attribute"
            )

    def encrypt(self, plaintext: bytes):
        if not hasattr(self, "ctexts"):
            self.ctexts: List = []
        for i in range(0, len(plaintext), self.block_size):
            if self.iv_utilized:
                xor_ptext = self.byte_xor(plaintext[i:i+16], self.ctexts[-1])
                self.ctexts.append(
                    self.encryptor.update(
                        self.padder.update(xor_ptext)
                    )
                ) 
                # if we reached the end of the plaintext
                # invoke finalize methods
                if (i + 16) > len(plaintext):
                    self.ctexts.append(
                        self.encryptor.update(
                            self.padder.finalize()) + self.encryptor.finalize()
                    )
            else:
                xor_ptext = self.byte_xor(plaintext[i:i+16], self.iv)
                self.ctexts.append(
                    self.encryptor.update(
                        self.padder.update(xor_ptext)
                    )
                )
                self.iv_utilized = True
                
    @property
    def plaintext(self):
        if hasattr(self, "ptexts"):
            return "\n".join(map(str, self.ptexts))
        else:
            raise AttributeError(
                "Must invoke `decrypt` before accessing plaintext attribute"
            )

    def decrypt(self):
        if not hasattr(self, "ptexts"):
            self.ptexts: List = []
        index_cipher_dict = {i: c for i, c in enumerate(self.ctexts)}      
        for i, c in index_cipher_dict.items():
            if i == 0:
                decrypted_msg = self.decryptor.update(c)
                xored_msg = self.byte_xor(decrypted_msg, self.iv)
                unpadded_msg = self.unpadder.update(xored_msg)
                self.ptexts.append(unpadded_msg)
                continue
            decrypted_msg = self.decryptor.update(c)
            xored_msg = self.byte_xor(decrypted_msg, index_cipher_dict[i-1])
            unpadded_msg = self.unpadder.update(xored_msg)
            self.ptexts.append(unpadded_msg)

if __name__ == "__main__":
   cbc_obj = CBCFromECB() 
   cbc_obj.encrypt(b"This is a test. I hope this works")
   print(">"*25, "CipherText",">"*25)
   print(cbc_obj.ciphertext)
   cbc_obj.decrypt()
   print()
   print(">"*25, "PlainText",">"*25)
   print(cbc_obj.plaintext)
