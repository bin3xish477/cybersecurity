#!/usr/bin/env python3

from requests import get
from netaddr import IPNetwork
from netaddr.core import AddrFormatError
from argparse import ArgumentParser
from os import remove
from os.path import isfile, exists

spamhaus_url = "https://www.spamhaus.org/drop/drop.txt"
f = "drop.txt"

def get_spam_list():
	if exists(f):
		remove(f)
	with get(spamhaus_url) as resp:
		with open(f, "w") as drop_file:
			drop_file.write(resp.text)

def ip_spam_check(ip: str) -> bool:
	if exists(f) and isfile(f):
		with open(f) as drop_file:
			# skip first four lines
			[next(drop_file) for _ in range(4)]
			for line in drop_file:
				try:
					ip_block = IPNetwork(line.split(";")[0].strip())
					if ip in ip_block:
						return True
				except AddrFormatError:
					print(f"[!] Invalid IPv4 address: {ip}")
					exit(1)
	else:
		get_spam_list()
		ip_spam_check(ip)
	return False

if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument("IP", help="The IP address to analyze")
	parser.add_argument("-u", "--update",
		action="store_true", help="Retrieve an updated list of known spam network blocks")

	args = parser.parse_args()

	if args.update:
		get_spam_list()

	ip = args.IP
	if ip_spam_check(ip):
		print(f"[!] {ip} is part of an IP block controlled by spammers")
	else:
		print(f"[X] {ip} is not part of an IP block controlled by spammers")
