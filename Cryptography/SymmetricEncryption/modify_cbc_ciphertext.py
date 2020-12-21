#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes

def byte_xor(str1:bytes, str2:bytes) -> bytes:
    return bytes([a ^ b for a, b in zip(str1, str2)])

def create_new_ciphertext(malicious_header:bytes, ciphertext_body:bytes) -> bytes:
    return malicious_header + ciphertext_body

if __name__ == "__main__":
    bank_note = bytes(f"""
       < XML >
            < CreditCardPurchase >
                < Merchant > Acme Inc </ Merchant >
                < Buyer > Albert </ Buyer >
                < Date > 01/ 01/ 3001 </ Date >
                < Amount > $ 150.00  </ Amount >
                < CCNumber > 555-555-555-555 </CCNumber >
            </ CreditCardPurchase >
        </ XML >""", "utf-8")

    malicious_header = bytes(f"""
       < XML >
            < CreditCardPurchase >
                < Merchant > Evil LLC </ Merchant >""", "utf-8")
    
    header_end:int = bank_note.find(b"\n"+b" "*16+b"< Buyer")    
    key:bytes = token_bytes(32)
    nonce:bytes = token_bytes(16)
    aes_context = Cipher(
        algorithms.AES(key),
        modes.CTR(nonce),
        backend=default_backend()
    )
    encryptor = aes_context.encryptor()
    decryptor = aes_context.decryptor()

    encrypted_note:bytes = encryptor.update(bank_note)
    print("#"*30, "Original Message Ciphertext", "#"*30)
    print(encrypted_note)
    print("#"*30, "Original Message Plaintext", "#"*30)
    print(decryptor.update(encrypted_note).decode("utf-8"))
    
    extracted_keystream:bytes = byte_xor(
        bank_note[:header_end], encrypted_note[:header_end]
    )
    print("#"*30, "Extracted Keystream", "#"*30)
    print(extracted_keystream)

    encrypted_malicious_header:bytes = byte_xor(
        extracted_keystream, malicious_header
    )
    modified_encrypted_note:bytes = create_new_ciphertext(
        encrypted_malicious_header, encrypted_note[header_end:]
    )
    print("#"*30, "Modified Message Ciphertext", "#"*30)
    print(modified_encrypted_note)
    print("#"*30, "Modified Message Plaintext", "#"*30)
    # For some reason, I couldn't get the
    # modified message to decrypt although
    # I encrypted the modified message with
    # the correct keystream
    print(decryptor.update(modified_encrypted_note))
