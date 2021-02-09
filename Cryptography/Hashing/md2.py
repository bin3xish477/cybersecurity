from binascii import hexlify

def md2(msg: bytes) -> str:
	"""
	MD2 implementation using RFC 1319: https://tools.ietf.org/html/rfc1319
	"""

	# block size = 16 bytes|128 bits
	b_s = 16
	# these are 256 randomly selected digits
	# from the mathematical constant, PI
	S = (	41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
		19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
		76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
		138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
		245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
		148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
		39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
		181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
		150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
		112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
		96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
		85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
		234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
		129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
		8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
		203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
		166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
		31, 26, 219, 153, 141, 51, 159, 17, 131, 20 )

	# add padding
	M = bytearray(msg)
	pad_size = b_s - (len(M) % b_s)
	padding = bytearray( pad_size for _ in range(pad_size) )
	M += padding

	# appending checksum
	C = bytearray( 0 for _ in range(b_s) )

	L = 0
	N = len(M)

	for i in range(N // b_s):
		for j in range(b_s):
			c = M[i * b_s + j]
			L = C[j] = S[c ^ L]
	# append checksum to message
	M += C

	# initialize message digest buffer
	buff_size = 48
	X = bytearray(0 for _ in range(buff_size))

	N_p = len(M)
	# processing message in 16-byte blocks
	for i in range(N_p // b_s):
		for j in range(b_s):
			X[b_s + j] = M[i * b_s + j]
			X[2 * b_s + j] = X[b_s + j] ^ X[j]

		t = 0
		for j in range(18):
			for k in range(buff_size):
				X[k] = t = X[k] ^ S[t]
			t = (t + j) % len(S)

	return X[:16].hex()

if __name__ == "__main__":
	invalid_hash = "invalid MD2 hash"
	assert md2(b'') == "8350e5a3e24c153df2275c9f80692773", invalid_hash
	assert md2(b"abc") == "da853b0d3f88d99b30283a69e6ded6bb", invalid_hash
	assert md2(b"message digest") == "ab4f496bfb2a530b219ff33031fe06b0", invalid_hash

	with open("./test.txt", "rb") as f:
		file_bytes = f.read()
		assert md2(file_bytes) == "8c74d1b6920bd7f67fdaa9697b938961", invalid_hash