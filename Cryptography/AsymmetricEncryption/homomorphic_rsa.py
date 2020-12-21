from rsa import RSA
from gmpy2 import powmod, invert

def rsa_encrypt(plaintext, publickey):
    nums = publickey.public_numbers()
    return powmod(plaintext, nums.e, nums.n)

def rsa_decrypt(ciphertext, privatekey):
    nums = privatekey.private_numbers()
    return powmod(ciphertext, nums.d, nums.public_numbers.n)

if __name__ == "__main__":
    manager = RSA(public_exponent=65537, key_size=2048)

    private_key = manager.private_key
    public_key = manager.public_key

    n = public_key.public_numbers().n
    a = 5
    b = 10

    encrypted_a = rsa_encrypt(a, public_key)
    encrypted_b = rsa_encrypt(b, public_key)
    
    # mutiplying the encrypted value of a with the
    # encrypted value of b, to obtain the product of
    # both encrypted values
    encrypted_product = (encrypted_a * encrypted_b) % n
    # getting the product of the two plaintext values
    product = rsa_decrypt(encrypted_product, private_key)

    print(f"{a} x {b} = {product}")
