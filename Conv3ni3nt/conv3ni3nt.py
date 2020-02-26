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

		tools = input('%sconv3%s> ' % (fg(self.interface.gray), attr(0)))

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
		# > display prompt for inputing tool options
		self.interface.tool_options_prompt()
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
		# > convert string of options to list of options
		tool_options = tool_options.split()
		# > join all options with underscore for readability
		parsed_options = '_'.join(tool_options)
		# > return crafted name
		return tool_name + '_' + parsed_options

	def start_tool(self, tool_name, tool_options):
		# > get file name to create
		file_name = self.generate_file_name(tool_name, tool_options) + '.txt'
		print(file_name)
		# > open file created for writing
		with open(file_name, 'w') as tool_file:
			# > if tool_options is not asking for the help menu
			if tool_options != '-h':
				# > use the tool with its options and direct output to file
				subp.call(tool_name + ' ' + tool_options, stdout=tool_file)
			# > if option equals -h print out help menu to terminal
			else:
				subp.call(tool_name + ' ' + tool_options, shell=True)



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