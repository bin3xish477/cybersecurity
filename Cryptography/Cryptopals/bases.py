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
			group = string[i:i+3]
			# create a string containing the bits of the three character bytes
			_bits = ''.join(bin(b)[2:].zfill(8) for b in group)
			# get chunks of 6 bits and convert them into ascii characters
			# adding padding as needed based on the block bit length
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

	def from_b64(self, string: bytes) -> str:
		pass

	def to_b32(self, string: bytes) -> str:
		pass

	def from_b32(self, string: bytes) -> str:
		pass

	def hex_to_b64(self, string: bytes) -> str:
		pass

def main():
	b64_encode = Bases().to_b64
	print(b64_encode(b"abcd"))

if __name__ == "__main__":
	main()