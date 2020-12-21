#!/usr/bin/env python3
"""
pip3 install prettytable
"""
import hashlib
from prettytable import PrettyTable
from sys import argv, exit

def generate_hashes_for_file(file_):
    # MD5, SHA1, SHA224, SHA256, SHA384, and SHA512
    text = open(file_, "rb").read()
    md5_hash = hashlib.md5(text).hexdigest()
    sha1_hash = hashlib.sha1(text).hexdigest()
    sha224_hash = hashlib.sha224(text).hexdigest()
    sha256_hash = hashlib.sha256(text).hexdigest()
    sha512_hash = hashlib.sha512(text).hexdigest()
    return (
        md5_hash, sha1_hash, sha224_hash, sha256_hash, sha512_hash
    )
if __name__ == "__main__":
    if len(argv) < 2:
        print(f"Usage: {__file__} <file_to_generate_hashes_for>")
        exit(1)
    file_ = argv[1]
    file_hashes = generate_hashes_for_file(file_)

    hash_algorithms = "MD5", "SHA1", "SHA224", "SHA256", "SHA512"
    print(f"Generating hashes for file: {file_}")
    t = PrettyTable(["Hash Function", "Digest"], padding_width=0)
    for algorithm, digest in zip(hash_algorithms, file_hashes):
        t.add_row([algorithm, digest])
    print(t)
