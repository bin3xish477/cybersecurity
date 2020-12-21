from rsa import RSA
from gmpy2 import powmod
from itertools import product
from string import ascii_letters
from time import perf_counter

def bytes_to_int(b):
    return int.from_bytes(b, byteorder="big")

def rsa_encrypt(m, public_key):
    nums = public_key.public_numbers()
    return powmod(m, nums.e, nums.n)

def brute_force(target, public_key, word_size):
    start = perf_counter()
    for word in product(ascii_letters, repeat=word_size):
        word = ''.join(word)
        encrypted_word = rsa_encrypt (
            bytes_to_int(bytes(word, "utf-8")), public_key
        )
        if encrypted_word == target:
            end = perf_counter()
            elapsed = end - start
            print(f"Found match: \"{word}\" in {elapsed} seconds")
            break

if __name__ == "__main__":
    public_key = RSA (
        public_exponent=65537, key_size=2048
    ).public_key

    four_letter_word = b"Wish"
    five_letter_word = b"Allow"

    four_letter_word_as_int = bytes_to_int(four_letter_word)
    five_letter_word_as_int = bytes_to_int(five_letter_word)

    encrypted_four_letter_word = rsa_encrypt (
        four_letter_word_as_int, public_key
    )
    encrypted_five_letter_word = rsa_encrypt (
        five_letter_word_as_int, public_key
    )

    brute_force(encrypted_four_letter_word, public_key, len(four_letter_word))
    brute_force(encrypted_five_letter_word, public_key, len(five_letter_word))

"""
Output:

Found match: Wish in 188.66329249999944 seconds
Found match: Allow in 5334.405771 seconds
"""
