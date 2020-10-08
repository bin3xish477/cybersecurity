#!/usr/bin/env python3
from winreg import (
	HKEY_CURRENT_USER,
	KEY_ALL_ACCESS,
	ConnectRegistry,
	OpenKey,
	EnumValue,
	EnumKey,
	QueryInfoKey
)

from ctypes import (
	windll,
	c_long,
	byref
)

def get_key_values(key):
	num_key_values = QueryInfoKey(key)[1]
	for i in range(num_key_values):
		print("[{}, {}, {}]".format(*EnumValue(key, i)))

def get_subkeys(key):
		j = 0
		while True:
			try:
				yield EnumKey(key, j)
				j += 1
			except WindowsError: break

def enumerate_registry_hive(top_registry_key, subkey=None):
	with ConnectRegistry(None, top_registry_key) as key:
		for subkey in get_subkeys(key):
			opened_key = OpenKey(top_registry_key, subkey, 0, KEY_ALL_ACCESS)
			get_key_values(opened_key)
	
	if subkey not None:

	subkey = f"{}"
	#enumerate_registry_hive(top_registry_key, subkey=subkey)

if __name__ == "__main__":
	enumerate_registry_hive(HKEY_CURRENT_USER)