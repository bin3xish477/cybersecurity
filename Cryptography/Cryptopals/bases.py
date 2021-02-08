from string import ascii_lowercase, ascii_uppercase

char_set = ( *ascii_uppercase, *ascii_lowercase, *"0123456789+/" )
char_set_dict = { i: char for i, char in zip(range(len(char_set)), char_set) }

def _from_hex_to_ascii(s: str) -> str:
	_ascii = ""
	for i in range(0, len(s), 2):
		hex_char = s[i: i+2]
		_ascii += chr(int(hex_char, 16))
	return _ascii

def _pad_right_and_get_index(bit_string, bit_length) -> int:
	if bit_length == 2:
		return int(f"{bit_string}0000", 2)
	elif bit_length == 4:
		return int(f"{bit_string}00", 2)
	return int(bit_string, 2)

def to_b64(string: bytes) -> str:
	if not isinstance(string, bytes):
		raise TypeError("Arguemnt to ``to_b64`` must be bytes")

	_encoded = ""
	for i in range(0, len(string), 3):
		group = string[i:i+3]
		# create a string containing the bits of the three character bytes
		_bits = ''.join(bin(b)[2:].zfill(8) for b in group)
		# get chunks of 6 bits and convert them into ascii characters
		# adding padding as needed based on the block bit length
		for j in range(0, len(_bits), 6):
			_bit_block = _bits[j:j+6]
			if len(_bit_block) == 2:
				if '1' in _bit_block:
					_index = _pad_right_and_get_index(_bit_block, len(_bit_block))
					_encoded += char_set_dict[_index] + "=="
				else:
					_encoded += "=="
			elif len(_bit_block) == 4:
					if '1' in _bit_block:
						_index = _pad_right_and_get_index(_bit_block, len(_bit_block))
						_encoded += char_set_dict[_index] + '='
					else:
						_encoded += '='
			else:
				_index = int(_bit_block, 2)
				_encoded += char_set_dict[_index]
	return _encoded

def from_b64(string: bytes) -> str:
	pass

def to_b32(string: bytes) -> str:
	pass

def from_b32(string: bytes) -> str:
	pass

def hex_to_b64(string: bytes) -> str:
	pass

def main():
	print(to_b64(b"Alexis Rodriguez"))

if __name__ == "__main__":
	main()
