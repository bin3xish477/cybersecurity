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
	from pyfiglet import Figlet
	from random import randrange
	from tqdm import tqdm
except ImportError:
	print('%s [-] Error importing a module %s' % (fg(196), attr(0)))
	os.system('exit')

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 		Con3ni3nt Interface
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Interface:
	def __init__(self):
		self.title = 'Conv3ni3nt'
		self.font='future'
		self.red = 196
		self.purple = 129
		self.lightyellow = 228
		self.gray = 250
		self.rancolor = randrange(256)

	def signature(self):
		'''
		'''
		sig = Figlet(font=self.font)

		print(sig.renderText(self.title))

		print('\tBy : ' + '%sAlexis Rodriguez%s' % (fg(self.purple), attr(0)))

		print('%s\t aka BinexisHATT\n%s' % (fg(self.purple), attr(0)))

	def tools_prompt(self):
		'''
		'''
		print('%sEnter the tools you use: %s' % (fg(self.red), attr(0)))

		print('%sE.g. nmap dirb nikto ...%s' % (fg(self.lightyellow), attr(0)))
