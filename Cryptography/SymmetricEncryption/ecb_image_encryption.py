from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from sys import argv, exit
from secrets import token_bytes

if __name__ == "__main__":
    if len(argv) < 3:
        print(f"Usage: python3 {__file__} quote.bmp [outfile_name].bmp")
        exit(1)

    key = token_bytes(32)
    cipher = Cipher(algorithms.AES(key),
                    modes.ECB(),
                    backend=default_backend())
    encryptor = cipher.encryptor()
    
    i_f, o_f = argv[1:3]
    with open(i_f, "rb") as reader:
        with open(o_f, "wb+") as writer:
            data = reader.read()
            header, body = data[:54], data[54:]
            body += b"\x00" * (16-(len(body)%16))
            encrypted_body = encryptor.update(body)
            writer.write(header+encrypted_body)

