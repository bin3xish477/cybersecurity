#!/usr/bin/env python3
from email import message_from_bytes
from os import scandir
from os import sep
from os.path import isfile
from os.path import isdir
from os.path import exists
from glob import glob
from argparse import ArgumentParser
from sys import exit
from sys import argv
from colors import red
from colors import green
from colors import blue
from colors import white
from colors import purple
from colors import orange
from colors import yellow
from colors import grey
from colors import normal
from colors import bold
from colors import bkgrd

__author__ = "BinexisHATT"
__date__   = "02/01/2021"

class ParseEmail:
	def __init__(self, _file=None, directory=None):
		self._file     = _file
		self.directory = directory 

	def run(self, func, args=None):
		if self._file:
			with open(self._file, "rb") as f:
				self.eml = message_from_bytes(f.read())
				print(bkgrd(white(" File "), "grey_42"), ":", self._file, "\n")
				if func == self.match_headers:
					func(args)
				else:
					func()
		else:
			for entry in scandir(path=self.directory):
				file_name = entry.name
				if entry.is_file():
					with open(f"{self.directory}{sep}{entry.name}", "rb") as f:
						self.eml = message_from_bytes(f.read())
						print(bkgrd(white(" File "), "grey_42"), ":", file_name, "\n")
						if func == self.match_headers:
							func(args)
						else:
							func()
						print()

	def basic_parse(self):
		print(bold(blue("[To]")), (":").rjust(11), self.eml["To"])
		print(bold(green("[From]")), (":").rjust(9), self.eml["From"])
		print(bold(yellow("[Sender]")), (":").rjust(7), self.eml["Sender"])
		print(bold(orange("[Delivered To]")), ":", self.eml["Delivered-To"])
		print(bold(red("[Subject]")), (":").rjust(6), self.eml["Subject"])
		print(bold(purple("[Date]")), (":").rjust(9), self.eml["Date"])
		print(bold(grey("[Content-Type]")), (":").rjust(1), self.eml["Content-Type"])

	def get_received_headers(self):
		received = self.eml.get_all("Received")
		if received:
			for receive in received:
				print(bold(white(f"<Received>")), ":", receive)
		else:
			print("No", bkgrd(white("`Received`"), 'red'), "header for this email")

	def get_all_headers(self):
		print(bold(green("[Headers]")))
		for header in self.eml.keys():
			print("\t", "\u2022", header)

	def match_headers(self, headers):
		headers = list(map(lambda s: s.lower(), headers))
		for header in self.eml.keys():
			if header.lower() in headers:
				for m in self.eml.get_all(header):
					print(bold(white(f"<{header}>")), ":", m)

def usage():
	print("""usage: Parse emails [-h] [-f FILE] [-d DIRECTORY] [-m MATCH [MATCH ...]] [-a] [-r]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Email file to parse
  -d DIRECTORY, --directory DIRECTORY
                        Directory containing email files to parse
  -m MATCH [MATCH ...], --match MATCH [MATCH ...]
                        Get all values for a specified header
  -a, --all-headers     Show all email headers
  -r, --show-receives   Show all values for `Received` header

examples:
   # Perform basic parsing on email

   >>> python3 parse_email.py -f sample.eml 

   # Show all emails headers

   >>> python3 parse_email.py -f sample.eml -a

   # Show all values for `Received` headers

   >>> python3 parse_email.py -f sample.eml -r

   # Show all values for a specified header

   >>> python3 parse_email.py -f sample.eml -m "to" "from" "subject"

   # Parse all emails files in a given directory
   # Note: all arguments above can be used on directories as well

   >>> python3 parse_email.py -d email_dir""")

if __name__ == "__main__":
	parser = ArgumentParser("Parse emails", add_help=False)
	parser.add_argument("-f", "--file", help="Email file to parse")
	parser.add_argument("-d", "--directory", help="Directory containing email files to parse")
	parser.add_argument("-m", "--match", nargs="+", help="Get all values for a specified header")
	parser.add_argument("-a", "--all-headers", action="store_true", help="Show all email headers")
	parser.add_argument("-r", "--show-receives", action="store_true", help="Show all values for `Received` header")
	parser.add_argument("-h", "--help", action="store_true", help="Show this help message")

	args = parser.parse_args()

	if len(argv) < 2 or args.help:
		usage()
		exit(1)

	if not args.file and not args.directory:
		print(bkgrd(white("Must provide `-f` or `-d` arguments"), "red"))
		exit(1)
	elif args.file:
		if not exists(args.file) or not isfile(args.file):
			print(bkgrd(white(f"{args.file} does not exists or is not a file..."), "red"))
			exit(1)
		else:
			email_parser = ParseEmail(_file=args.file)
	else:
		if not exists(args.directory) or not isdir(args.directory):
			print(bkgrd(white(f"{args.file} does not exists or is not a directory..."), "red"))
			exit(1)
		else:
			email_parser = ParseEmail(directory=args.directory)

	if args.match:
		email_parser.run(email_parser.match_headers, args=args.match)
	elif args.all_headers:
		email_parser.run(email_parser.get_all_headers)
	elif args.show_receives:
		email_parser.run(email_parser.get_received_headers)
	else:
		email_parser.run(email_parser.basic_parse)
