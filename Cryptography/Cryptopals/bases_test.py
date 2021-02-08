from bases import to_b64
from bases import from_b64

if __name__ == "__main__":
	inp = b"ABCDEFGHIJ"
	out = "QUJDREVGR0hJSg=="
	assert to_b64(inp) == out, "invalid base64 encoding"
