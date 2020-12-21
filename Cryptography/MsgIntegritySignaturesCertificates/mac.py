from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes
from hashlib import sha256

class Encryptor:

    def __init__(self, key, nonce):
        aes_ctr = Cipher(
            algorithms.AES(key), modes.CTR(nonce), backend=default_backend()
        )
        self.encryptor = aes_ctr.encryptor()
        self.hasher = sha256()

    def update_encryptor(self, plaintext):
        ciphertext = self.encryptor.update(plaintext)
        self.hasher.update(ciphertext)
        return ciphertext

    def finalize(self):
        return self.encryptor.finalize() + self.hasher.digest()

if __name__ == "__main__":
    key = token_bytes(32)
    nonce = token_bytes(16)
    E = Encryptor(key, nonce)
    ciphertext = E.update_encryptor(b"This is a message")
    ciphertext += E.finalize()
    print(ciphertext)


