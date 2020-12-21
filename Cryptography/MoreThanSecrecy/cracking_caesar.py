from string import ascii_lowercase as alphabet 
from sys import argv, exit

def crack_caesar(cipher):
    plain_text = ""
    for n in range(1, 27):
        plain_text = ""
        for char in cipher:
            if char in alphabet:
                plain_text += alphabet[alphabet.index(char)-n%len(alphabet)]
            else:
                plain_text += char
        yield plain_text 

if __name__ == "__main__":
    if len(argv) < 2:
        print(f"usage: {__file__} <encoded_caesar_string>")
        exit(1)

    cipher = argv[1].lower()
    decoded_strings = crack_caesar(cipher)
    for string in decoded_strings:
        print(string)
