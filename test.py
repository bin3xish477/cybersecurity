#!/usr/bin/env python3

from cryptography.fernet import Fernet

with open('/tmp/dir_to_encrypt/hello.txt', 'rb') as f:
	file_c = f.read().strip()
	print(file_c)

