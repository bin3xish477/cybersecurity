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
except ImportError:
	print('%s [-] Error importing a module %s' % (fg(196), attr(0)))
	os.system('exit')

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 		Con3ni3nt Interface
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Interface:
	def __init__(self):
		pass
	def signature(self):
		sig = Figlet(font='future')
		print(sig.renderText('binexishatt'))
		print('By : ' + '%sAlexis Rodriguez\n\n%s' % (fg(129), attr(0)))

	def tools_prompt_interface(self):
		print('%sEnter the tools below you would like to use: %s' % (fg(226), attr(0)), end='')
		print('%se.g. nmap dirb nikto ...%s' % (fg(196), attr(0)))