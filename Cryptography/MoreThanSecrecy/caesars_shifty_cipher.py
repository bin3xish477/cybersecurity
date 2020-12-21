from string import ascii_letters as letters
from sys import argv, exit

def encode(file_, shift):
    with open(file_, "r+") as f:
        plain_text = f.read()
        cipher = ""
        for letter in plain_text:
            if letter in letters:
               cipher += letters[
                    (letters.index(letter)+shift)%len(letters)
               ]
            else:
                cipher += letter
        f.truncate(0)
        f.seek(0)
        f.write(cipher)

def decode(file_, shift):
    with open(file_, "r+") as f:
        cipher_text = f.read()
        plain_text = ""
        for letter in cipher_text:
            if letter in letters:
                plain_text += letters[
                    (letters.index(letter)-shift)%len(letters)
                ]
            else:
                plain_text += letter
        f.truncate(0)
        f.seek(0)
        f.write(plain_text)
            
if __name__ == "__main__":
    if len(argv) != 4:
        print(f"usage: {__file__} <file> <1=encode|2=decode> <shift_distance>")
        exit(1)
        
    file_ = argv[1]  
    action = argv[2] 
    shift_dist = int(argv[3]) 

    if shift_dist < 1:
        raise ValueError("Shift distance must be greater or equal to 1")

    if action == "1":
        encode(file_, shift_dist)

    elif action == "2":
        decode(file_, shift_dist)

    else:
        print("Must provide action (encode or decode)")
        exit(1)



""" 
**************EXAMPLE FROM PRACTICAL CRYPTOGRAPHY IN PYTHON*************
In there example they create a two seperate dictionaries representing the
mappings in caesar cipher table. One represents the mapping of a letter to
it's substituted value and the other represents the mapping of a substituted
letter to it's original value.
"""
# def create_substitution_table(n):
#    encoding = {}
#    decoding = {}
#    alphebet_size = len(string.acsii_uppercase)
#    for i in range(alphabet_size):
#        letter       = string.ascii_uppercase[i]
#        subst_letter = string.ascii_uppercase[(i+n)%alphabet_size] 
#       encoding[letter] = subst_letter
#        decoding[subst] = letter
#    return encoding, decoding

#def encode(message, subst):
#    cipher = ""
#    for letter in message:
#        if letter in message:
#            cipher += subst[letter]
#        else:
#            cipher += letter
#    return cipher

# ** The function above can be simplified **
# def encode(message, subst):
#     return "".join(subst.get(x, x) for x in message)]

# def decode(message, subst):
#     encode(message, subst):


