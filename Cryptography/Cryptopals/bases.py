from string import ascii_lowercase, ascii_uppercase

char_set = ( *ascii_uppercase, *ascii_lowercase, *"0123456789+/" )
char_set_dict = { i: char for i, char in zip(range(len(char_set)), char_set) }

def _from_hex_to_ascii(s: str) -> str:
	_ascii = ""
	for i in range(0, len(s), 2):
		hex_char = s[i: i+2]
		_ascii += chr(int(hex_char, 16))
	return _ascii

def to_b64(b: bytes) -> bytes:
	pass

def from_b64(b: bytes) -> bytes:
	pass

def to_b32(b: bytes) -> bytes:
	pass

def from_b32(b: bytes) -> bytes:
	pass

def hex_to_b64(b: bytes) -> bytes:
	pass

def tests():
	t = "I'm killing your brain like a poisonous mushroom"
	h = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	assert _from_hex_to_ascii(h) == t, "hex to ascii error"

def main():
	tests()

if __name__ == '__main__':
	main()
