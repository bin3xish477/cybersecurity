#!/usr/bin/env python3

"""
This program uses ip-api.com and it is a free API but no more 45 requests per minute are allowed
"""
from requests import get
from folium import Map, Marker, Icon
from argparse import ArgumentParser
from json import loads
from colors import bold
from colors import blue
from os.path import exists, isfile
from sys import argv, exit

__author__ = "BinexisHATT"
__date__   = "02/01/2021"

class Mapper:
	def __init__(self, targets: list):
		self.targets = targets
		self._generate_map()

	def _get_coordinates(self, target) -> list:
		url = F"http://ip-api.com/json/{target}?fields=lat,lon"
		resp = get(url)
		resp_json = loads(resp.text)
		latitude, longitude = resp_json["lat"], resp_json["lon"]
		return [latitude, longitude]

	def _generate_map(self):
		# creating map
		self.m = Map(location=[0,0], zoom_start=3)	

	def add_target_marker(self, target):
		# adding marker to map
		Marker(
			location=self._get_coordinates(target),
			popup=target,
			icon=Icon()	
		).add_to(self.m)

	def save(self):
		# save to html file
		self.m.save("./map.html")
		print(bold(blue("Map saved to file:")), "./map.html")

def usage():
	print("""
usage: Show IP/s or Domain name/s on earth map [-h] [-t TARGETS [TARGETS ...]]
                                               [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -t TARGETS [TARGETS ...], --targets TARGETS [TARGETS ...]
                        IP address/s or domain name/s to get coordinates for
                        and show on map
  -f FILE, --file FILE  File with IP addresses or domain names on seperate
                        lines to map

example:
  # get location of google.com
  >>> python3 map_ip_location.py -t google.com

  # get location of several IP addresses
  >>> python3 map_ip_location.py -t 1.1.1.1 8.8.8.8 9.9.9.9

  # use file with IP addresses or domain names to map
  >>> python3 map_ip_location.py -f ip_file.txt

  # use file with IP addresses or domain names to map and supply manual targets
  >>> python3 map_ip_location.py -t github.com netflix.com -f ip_file.txt
""")

if __name__ == "__main__":
	parser = ArgumentParser("Show IP/s or Domain name/s on earth map", add_help=False)
	parser.add_argument("-t", "--targets", nargs="+", help="IP address/s or domain name/s to get coordinates for and show on map")
	parser.add_argument('-f', "--file", help="File with IP addresses or domain names on seperate lines to map")
	parser.add_argument('-h', "--help", action="store_true", help="Shows this help message")

	args = parser.parse_args()

	if len(argv) < 2 or args.help:
		usage()
		exit(1)

	if args.file and not args.targets:
		if isfile(args.file) and exists(args.file):
			targets = []
			with open(args.file) as f:
				for target in f:
					target = target.strip()
					targets.append(target)
		print(targets)
		mapper = Mapper(targets=targets)
		for target in mapper.targets:
			mapper.add_target_marker(target)
		mapper.save()

	elif args.file and args.targets:
		if isfile(args.file) and exists(args.file):
			targets = []
			with open(args.file) as f:
				for target in f:
					target = target.strip()
					targets.append(target)
		targets.extend(args.targets)
		mapper = Mapper(targets=targets)
		for target in mapper.targets:
			mapper.add_target_marker(target)
		mapper.save()

	else:
		mapper = Mapper(targets=args.targets)
		for target in mapper.targets:
			mapper.add_target_marker(target)
		mapper.save()
