#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from typing import List, NoReturn 
from glob import glob
from os import path

def generate_cipher(key: bytes) -> Cipher:
    cipher = Cipher(algorithms.AES(key),
                    modes.ECB(),
                    backend=default_backend())
    return cipher

def encrypt(plain_t: bytes, c: Cipher) -> hex:
    encryptor = c.encryptor()
    cipher_t: bytes = encryptor.update(plain_t)
    return cipher_t.hex()

def get_key(content: str) -> bytes:
    key_i = content.find("KEY")
    key_e = content[key_i:].find("\n")
    key = content[key_i:key_i+key_e].replace("KEY = ", "") 
    return bytes.fromhex(key)
    
def get_plain_text(content: str) -> str:
    return content.replace("PLAINTEXT = ", "") 
    
def get_cipher_text(content: str) -> str:
    return content.replace("CIPHERTEXT = ", "") 

def test(plain_texts: List, cipher_texts: List, c: Cipher) -> NoReturn:
    print("\n\tKAT CipherText", "\t\t\t"," "*2, "Computer CipherText")
    for p_t, c_t in zip(plain_texts, cipher_texts):
        p_t_bytes = bytes.fromhex(p_t)
        computed_c_t = encrypt(p_t_bytes, c)
        if computed_c_t == c_t:
            print(computed_c_t, "==", c_t, "[PASS] \u2713")
        else:
            print(computed_c_t, "!=", c_t, "[FAIL] \u00d7")
    print("\n")

if __name__ == "__main__":
    key = ""
    cwd = path.dirname(path.abspath(__file__)) + "/KATs/ECBGFS*box*"
    for rsp_f in glob(cwd): 
        plain_texts, cipher_texts = [], [] 
        file_ = rsp_f.split("/")[-1]
        print(f"Running AES ECB Test on file: {file_}")
        with open(rsp_f, "r") as f:
            [next(f) for _ in range(9)]
            content: str = f.read()
            key: bytes = get_key(content)
            cipher: Cipher = generate_cipher(key)
            for line in content.split("\n"):
                if "PLAINTEXT" in line:
                    plain_texts.append(get_plain_text(line))
                elif "CIPHERTEXT" in line:
                    cipher_texts.append(get_cipher_text(line))
                elif "DECRYPT" in line:
                    break
            test(plain_texts, cipher_texts, cipher)
                
