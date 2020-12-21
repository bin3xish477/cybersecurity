from rsa import RSA

if __name__ == "__main__":
    manager = RSA(public_exponent=65537, key_size=2048)
    print(f"n = {manager.public_key.public_numbers().n}")
    print(f"e = {manager.public_key.public_numbers().e}")
    print(f"d = {manager.private_key.private_numbers().d}")
