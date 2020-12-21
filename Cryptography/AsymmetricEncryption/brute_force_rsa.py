from rsa import RSA
from time import perf_counter
from gmpy2 import powmod
from itertools import product
from string import ascii_letters

def bytes_to_int(b):
    return int.from_bytes(b, byteorder="big")

def rsa_encrypt(m, public_key):
    nums = public_key.public_numbers()
    return powmod(m, nums.e, nums.n) 
    
def brute_force(target, public_key, word_len):
    start = perf_counter()
    for word in product(ascii_letters, repeat=word_len):
        word = ''.join(word)
        word_as_int = bytes_to_int(bytes(word, "utf-8"))
        encrypted_word = rsa_encrypt(word_as_int, public_key)
        if encrypted_word == target:
            end = perf_counter()
            time_elapsed = end - start
            print(f"Found match: \"{word}\"")
            print(f"Time elapsed: {time_elapsed}")
            break

if __name__ == "__main__":
    public_key = RSA (
        public_exponent=65537, key_size=2048
    ).public_key

    word = b"pawn"
    word_as_int = bytes_to_int(word)    
    encrypted_word = rsa_encrypt(word_as_int, public_key)
    brute_force(encrypted_word, public_key, len(word))

"""
Found match: "pawn"
Time elapsed: 58.58826439999757
"""
