class Bases:
	def __init__(self):
		self.base64_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
		self.base32_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

	def _from_hex_to_ascii(self, string: str) -> str:
		_ascii = ""
		for i in range(0, len(string), 2):
			hex_char = string[i: i+2]
			_ascii += chr(int(hex_char, 16))
		return _ascii

	def _pad_right_and_get_index(self, bit_string, bit_length) -> int:
		if bit_length == 2:
			return int(f"{bit_string}0000", 2)
		elif bit_length == 4:
			return int(f"{bit_string}00", 2)
		return int(bit_string, 2)

	def to_b64(self, string: bytes) -> str:
		base64_dict = {
		i: char for i, char in zip(range(len(self.base64_charset)), self.base64_charset)
		}
		if not isinstance(string, bytes):
			raise TypeError("Argument to ``to_b64`` must be bytes")

		_encoded = ""
		for i in range(0, len(string), 3):
			_group = string[i:i+3]
			_bits = ''.join(bin(b)[2:].zfill(8) for b in _group)
			for j in range(0, len(_bits), 6):
				_bit_block = _bits[j:j+6]
				if len(_bit_block) == 2:
					_index = self._pad_right_and_get_index(_bit_block, len(_bit_block))
					_encoded += base64_dict[_index] + "=="
				elif len(_bit_block) == 4:
						_index = self._pad_right_and_get_index(_bit_block, len(_bit_block))
						_encoded += base64_dict[_index] + '='
				else:
					_index = int(_bit_block, 2)
					_encoded += base64_dict[_index]
		return _encoded

	def from_b64(self, string: str) -> str:
		if not isinstance(string, bytes):
			raise TypeError("Argument to ``from_b64`` must be bytes")

		_decoded = ""
		string = bytes(str(string)[2:-1].rstrip('='), "utf8")
		for i in range(0, len(string), 4):
			_group = string[i:i+4]
			_bits = ''.join(
				bin(self.base64_charset.index(chr(c)))[2:].zfill(8)[2:]
				for c in _group ) 
			for j in range(0, len(_bits), 8):
				_block = _bits[j:j+8]
				# if the last block is not equal to 8, break
				if len(_block) != 8:
					break
				else:
					_decoded += chr(int(_bits[j:j+8], 2))
		return _decoded

	def to_b32(self, string: bytes) -> str:
		pass

	def from_b32(self, string: bytes) -> str:
		pass

	def hex_to_b64(self, string: bytes) -> str:
		string = bytes(self._from_hex_to_ascii(string), "utf8")
		return self.to_b64(string)

def main():
	bases = Bases()
	b64_encode = bases.to_b64
	b64_decode = bases.from_b64
	s = b"QUJD"
	print(b64_decode(s))
	s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	print(bases.hex_to_b64(s))

if __name__ == "__main__":
	main()
