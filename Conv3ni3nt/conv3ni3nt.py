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
	from interface import *
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
	def __init__(self, interface_obj):

		self.interface = interface_obj

		self.interface.signature()

		self.tool_list = None

	def get_tools(self):

		self.interface.tools_prompt()

		tools = input('%sConv3%s> ' % (fg(self.interface.gray), attr(0)))

		if 'exit' in tools:

			sys.exit(0)
		else:

			received_tools = tools.split()

		self.tool_list = received_tools

		return received_tools


	def get_tool_options(self):
		# > clear the terminal screen
		os.system('clear')
		# > print out my signature
		self.interface.signature()
		# > our list containing the options for each tool
		options_list = []
		# > iterate over every tool and prompt user for the desired options
		for tool in self.tool_list:
			# > this addiition is simply formating for our colored module
			tool = '%s' + tool + '%s'
			# > store user input in variable
			tool_option = input('Enter ' + tool % (fg(self.interface.rancolor), attr(0))+ ' options : ')
			# > if exit is the inputed option, exit the program
			if 'exit' in tool_option:
				# > exit program
				sys.exit(0)
			else:
				# > append options to our list containing all tool options
				options_list.append(tool_option)

		return options_list

	def generate_file_name(self, tool_name, tool_options):
		'''
		'''
		if len(tool_options) == 1:
			return tool_name + '_' + tool_options[0]
		# > return crafted name
		return tool_name + '_' + '_'.join(tool_options.split())


	def start_tool(self, tool, tool_options):
		'''
		'''
		# > subprocess.run requires a list when stdout is not directed to shell
		# > so converting our command string to a list
		command = (tool + ' ' + ''.join(tool_options)).split()

		if tool_options == '-h' or tool_options == '--help':
			# > print out help menu
			subp.run(command)
			# > prompt user to verify if they would like to go back to the tool options screen 
			go_back = input('%sType "back" to go back to tool prompt: %s' % (fg(self.interface.red), attr(0)))
			# > if input is back then display options screen
			if go_back.strip() == 'back':
				# > display tool options prompt
				tool_options = self.get_tool_options()
				# > a little recursion going on here
				self.start_tool(tool, tool_options)
			else:
				# > if input is not back, exit program
				sys.exit(0)
		else:
			# > get file name to create
			file_name = self.generate_file_name(tool, tool_options)
			# > open file created for writing
			with open(file_name, 'w') as tool_file:
					# > use the tool with its options and direct output to file
					subp.run(command, stdout=tool_file, text=True)


# %%%%%%%%%%%%%%%%
# 		MAIN      
# %%%%%%%%%%%%%%%%
def initiate():
	os.system('clear')

	display = Interface()

	conv3_obj = Conv3ni3nt(display)

	tools_lst = conv3_obj.get_tools()

	tool_options = conv3_obj.get_tool_options()

	for tool, options in zip(tools_lst, tool_options):
		conv3_obj.start_tool(tool, options)


if __name__ == '__main__':
	initiate()