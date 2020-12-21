#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from sys import argv, exit
from typing import Callable

if __name__ == "__main__":
    if len(argv) <2:
        print(f"Usage: {__file__} <file_with_info:merchant,buyer,amount>")
        exit(1)

    # The same preshared key and iv will be used
    # to encrypt multiple messages
    preshared_key = bytes.fromhex("11112222333344445555AAAABBBBFFFF")
    preshared_iv = bytes.fromhex("0"*32)

    info = open(argv[1], 'r').readlines()
    ciphertexts = []    
    for row in info:
        merchant, buyer, amount = row.strip().split(',')
        message = bytes(f"""
        < XML >
            < CreditCardPurchase >
                < Merchant > {merchant} </ Merchant >
                < Buyer > {buyer} </ Buyer >
                < Date > 01/ 01/ 2001 </ Date >
                < Amount > $ {amount.strip()}  </ Amount >
                < CCNumber > 555-555-555-555 </CCNumber >
            </ CreditCardPurchase >
        </ XML >""", "utf-8") 

        c = Cipher(
                    algorithms.AES(preshared_key),
                    modes.CTR(preshared_iv),
                    backend=default_backend()
            )
        encryptor: Callable = c.encryptor()
        ciphertexts.append(encryptor.update(message))
    
    # if one looks carefully at the ciphertext
    # produced by encrypting each message with
    # an object reusing the same key and iv,
    # one can see the repetitive bytes that reappear
    # throughout the text, simplifying the work needed
    # for adversaries to detect patterns and decipher 
    # the encrypted messages
    [print(c, "\n", "-"*50, "End of Ciphertext") for c in ciphertexts]
