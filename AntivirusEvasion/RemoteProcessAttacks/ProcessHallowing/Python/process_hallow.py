from sys import exit

from ctypes import windll
from ctypes import POINTER as Pointer


class SecurityAttributes(Structure):
    _fields_ = [
        ('nLength', DWORD),
        ('lpSecurityDescriptor', LPVOID),
        ('bInheritHandle', BOOL),
    ]


class ProcessHallow:
	def __init__(self):
		pass

	def __enter__(self):
		pass

	def __exit__(self):
		pass
