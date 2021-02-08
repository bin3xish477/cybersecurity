from bases import Bases

if __name__ == "__main__":
	b64_encode = Bases().to_b64
	b64_decode = Bases().from_b64

	inp = b"ABCDEFGHIJ"
	out = "QUJDREVGR0hJSg=="
	assert b64_encode(inp) == out, "invalid base64 encoding"
