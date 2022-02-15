#!/usr/bin/env python3
from pefile import PE
from argparse import ArgumentParser
from tabulate import tabulate
from colors import bold
from colors import blue
from colors import red
from colors import white
from colors import green 
from colors import orange 
from sys import argv, exit

__author__ = "BinexisHATT"
__date__   = "02/01/2021"

class PEParser:
	def __init__(self, pe):
		self.pedump = PE(pe, fast_load=True).dump_dict()

	def get_dos_header(self):
		headers = [
			bold(blue("Fields")),
			bold(red("FileOffset")),
			bold(green("Offset")),
			bold(orange("Value"))
		]
		table = []

		print("\n\t\t", bold(white("DOS HEADER")), "\n")
		for field, value in self.pedump["DOS_HEADER"].items():
			if isinstance(value, dict):
				t = [field]
				for subvalue in value.values():
					if isinstance(subvalue, int):
						subvalue = hex(subvalue)
						t.append(subvalue)
					elif "\\x00" in subvalue:
						l = len(subvalue)
						t.append("\\x00 * " + str(l))
				table.append(t)
		print(tabulate(table, headers=headers))

	def get_nt_header(self):
		pass

	def get_file_header(self):
		headers = [
			bold(blue("Fields")),
			bold(red("FileOffset")),
			bold(green("Offset")),
			bold(orange("Value"))
		]
		table = []

		print("\n\t\t\t\t", bold(white("FILE HEADER")), "\n")
		for field, value in self.pedump["FILE_HEADER"].items():
			if isinstance(value, dict):
				t = [field]
				for subvalue in value.values():
					if isinstance(subvalue, int):
						subvalue = hex(subvalue)
					t.append(subvalue)
				table.append(t)
		print(tabulate(table, headers=headers))

	def get_optional_header(self):
		headers = [
			bold(blue("Fields")),
			bold(red("FileOffset")),
			bold(green("Offset")),
			bold(orange("Value"))
		]
		table = []

		print("\n\t\t\t\t", bold(white("OPTIONAL HEADER")), "\n")

	def get_section_header(self):
		pass

if __name__ == "__main__":
	parser = ArgumentParser("Parse PE file headers")
	parser.add_argument("-g", "--header", nargs="+",
		choices=("dos", "nt", "file", "optional", "section"),
		help="The PE file header to parse")
	parser.add_argument("FILE", help="Path to PE file to parse headers for")

	args = parser.parse_args()

	if not args.header:
		print(bold(red("Please provide `-g` argument")))
		exit(1)

	peparser = PEParser(args.FILE)
	pe_headers = args.header
	if "dos" in pe_headers:
		peparser.get_dos_header()
	if "nt" in pe_headers:
		peparser.get_nt_header()
	if "file" in pe_headers:
		peparser.get_file_header()
	if "optional" in pe_headers:
		peparser.get_optional_header()
	if "section" in pe_headers:
		peparser.get_section_header()
