#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes
from sys import argv, exit
from typing import Callable

if __name__ == "__main__":
    if len(argv) < 2:
        print(f"usage: {__file__} quote.bmp | or any other bmp image")
        exit(1)
    
    image = argv[1]

    # AES-CBC Context
    key: bytes = token_bytes(32)
    iv: bytes = token_bytes(16)
    cbc_obj = Cipher (
                    algorithms.AES(key),
                    modes.CBC(iv),
                    backend=default_backend()
            )
    cbc_encryptor: Callable = cbc_obj.encryptor()
    cbc_decryptor: Callable = cbc_obj.decryptor()

    # AES-CTR Context
    key = token_bytes(32)
    nonce: bytes = token_bytes(16)
    ctr_obj = Cipher (
                    algorithms.AES(key),
                    modes.CTR(nonce),
                    backend=default_backend()
            )
    ctr_encryptor: Callable = ctr_obj.encryptor()
    ctr_decryptor: Callable = ctr_obj.decryptor()

    # TODO: make sure to first check if I can
    # encrypt and decrypt body of image successfully
    # and then corrupt ciphertext and trying 
    # decrypting it
    with open(image, "rb") as infile:
        with open("cbc_quote.bmp", "wb+") as outfile:
            file_data = infile.read()
            header, body = file_data[:54], file_data[54:]
            # add padding for block size limit
            body += b"/x00" * (16-(len(body)%16))
            encrypted_body = cbc_encryptor.update(body)
            body_size = len(encrypted_body)
            midpoint = int(body_size / 2)
            thousand_from_mid = encrypted_body[midpoint:midpoint+1000]
            # maliciously modifying ciphertext
            encrypted_body = encrypted_body.replace(thousand_from_mid,token_bytes(1000))
            decrypted_body = cbc_decryptor.update(encrypted_body)
            outfile.write(header+decrypted_body)

    with open(image, "rb") as infile:
        with open("ctr_quote.bmp", "wb+") as outfile:
            file_data = infile.read()
            header, body = file_data[:54], file_data[54:]
            encrypted_body = ctr_encryptor.update(body)
            body_size = len(encrypted_body)
            midpoint = int(body_size / 2)
            thousand_from_mid = encrypted_body[midpoint:midpoint+1000]
            # maliciously modifying ciphertext
            encrypted_body = encrypted_body.replace(thousand_from_mid,token_bytes(1000))
            decrypted_body = ctr_decryptor.update(encrypted_body)
            outfile.write(header+decrypted_body)
