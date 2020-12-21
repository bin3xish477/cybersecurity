#!/usr/bin/env python3
from sys import argv, exit

def generate_wordlist(alphabet, max_length):
    # base case
    if max_length <= 0: return
    for c in alphabet: yield c
    for c in alphabet:
        print(max_length)
        # recursion :(
        for n in generate_wordlist(alphabet, max_length-1):
            print("yield")
            yield c + n

if __name__ == "__main__":
    if len(argv) != 3:
        print(f"Usage: {__file__} <character_set> <wordlist_max_length>")
        exit(1)
        
    wordlist_alphabet = argv[1]
    wordlist_max_length = int(argv[2])
    wordlist = generate_wordlist(wordlist_alphabet, wordlist_max_length)
    [print(word) for word in wordlist]    

    with open("word.lst", "w") as f:
        [f.write(word+"\n") for word in wordlist]

