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
	import interface
	import sys
	import os
	import time
	import threading
	import subprocess as subp
except ImportError:
	print('%s [-] Error importing a module %s' % (fg(196), attr(0)))
	os.system('exit')

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 		Conv3ni3nt Class
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Conv3ni3nt:
	def __init__(self):
		self.interface = interface_obj

def get_tools():
	self.interface.tools_prompt_interface()
	tools = input('conv3> ')
	lst_of_tools = tools.split()
	return lst_of_tools

def initiate():
	# print my signature
	inter = Interface()
	conv3_obj = Conv3ni3nt(inter)
	time.sleep(10)
	os.system('clear')


# %%%%%%%%%%%%%%%%
# 		MAIN      
# %%%%%%%%%%%%%%%%
if __name__ == '__main__':
	initiate()