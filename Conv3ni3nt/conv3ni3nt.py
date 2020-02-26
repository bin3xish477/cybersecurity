#!/usr/bin/env python3
'''
----------------------------------------------------------------
Author : Alexis Rodriguez
Start date : 2020-02-26
End date : 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Description : 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
----------------------------------------------------------------
'''
try:
	from colored import fg, attr
	import sys
	import os
	import time
	import threading
	import subprocess as subp
	from pyfiglet import Figlet
except ImportError:
	print('%s [-] Error importing a module %s' % (fg(196), attr(0)))

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 		Conv3ni3nt Class
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Conv3ni3nt:
	def __init__(self):
		pass

def prompt_tools():
	print('%sEnter the tools below you would like to use: %s' % (fg(226), attr(0)), end='')
	print('%se.g. nmap dirb nikto ...%s' % (fg(196), attr(0)))
	tools = input('conv3> ')
	lst_of_tools = tools.split()
	return lst_of_tools

def signature():
	sig = Figlet(font='future')
	print(sig.renderText('binexishatt'))
	print('By : ' + '%sAlexis Rodriguez\n\n%s' % (fg(129), attr(0)))

def initiate():
	# print my signature
	signature()
	prompt_tools()
	instance = Conv3ni3nt()
	time.sleep(10)
	os.system('clear')


# %%%%%%%%%%%%%%%%
# 		MAIN      
# %%%%%%%%%%%%%%%%
if __name__ == '__main__':
	initiate()