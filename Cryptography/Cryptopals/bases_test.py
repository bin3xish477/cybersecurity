from bases import Bases

if __name__ == "__main__":
	base = Bases()
	b64_encode = base.to_b64
	b64_decode = base.from_b64

	inp = b"ABCDEFGHIJ"
	out = "QUJDREVGR0hJSg=="
	assert b64_encode(inp) == out, "invalid base64 encoding"

	inp = b"QUJDREVGR0hJSg=="
	out = "ABCDEFGHIJ"
	assert b64_decode(inp) == out, "invalid base64 decoding"
