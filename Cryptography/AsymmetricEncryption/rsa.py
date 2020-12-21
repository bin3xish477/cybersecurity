from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from sys import exit
from os.path import exists

class RSA:
    def __init__(self, *, public_exponent: int, key_size: int):
        self._private_key = rsa.generate_private_key(
            public_exponent=public_exponent,
            key_size=key_size,
            backend=default_backend()
        )
        self._public_key = self._private_key.public_key()

    @property
    def private_key(self):
        return self._private_key
    
    @property
    def public_key(self):
        return self._public_key

    def get_private_key_bytes():
        self.private_key_bytes:bytes = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        return private_key_bytes
    
    def get_public_key_bytes(file_):
        public_key_bytes:bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def load_private_key(file_, *, password=None):
        if not exists(file_):
            print(f"[-] File {file_} does not exist")
            exit(1)
        with open(file_, "rb") as reader:
            self.private_key = serialization.load_pem_private_key(
                reader.read(),
                backend=default_backend(),
                password=password
            )

    def load_public_key(file_):
        if not exists(file_):
            print(f"[-] File {file_} does not exist")
            exit(1)
        with open(file_, "rb") as reader:
            self.public_key = serialization.load_pem_private_key(
                reader.read(),
                backend=default_backend(),
            )

    def encrypt(self, plaintext):
        ciphertext = self.public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashing.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def bytes_to_int(self, b):
        return int.to_bytes(b, byteorder="big")

    def int_to_bytes(self, i):
        i = int(i)
        return i.from_bytes((i.bit_length()+7)//8, byteorder="big")
