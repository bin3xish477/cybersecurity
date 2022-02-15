#!/usr/bin/env python3
from requests import get
from argparse import ArgumentParser
from configparser import ConfigParser
from os import environ
from colors import white
from colors import bkgrd
from json import loads

__author__ = "BinexisHATT"
__date__   = "02/01/2021"

class IPRepChecker:
	def __init__(self, api_key, ip):
		self.url = f"https://ipqualityscore.com/api/json/ip/{api_key}/{ip}"

	def get_reputation(self):
		params = {
			"strictness": 0,
			"allow_public_access_points": "true",
			"lighter_penalties": "true"
		}
		return get(self.url, params=params).text

	def parse_reputation(self, rep):
		rep = loads(rep)
		premium_keys = ("success", "message", "request_id",
						"connection_type", "abuse_velocity")

		print(bkgrd(white("[Reputation]"), "blue"))
		for key, value in rep.items():
			if key in premium_keys:
				continue
			print("\t\u25aa " + key.capitalize().replace("_", " "), "::", value)
		print("\n\tCheck out this link for more info about results:" \
			  "\n\t\t- https://www.ipqualityscore.com/documentation/proxy-detection/overview\n")

if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument("IP", help="The IP address to check reputation for")

	args = parser.parse_args()
	config = ConfigParser()
	config.read("config.ini")

	if not config["ip_quality_score"]["api_key"]:
		ip = IPRepChecker(config["ip_quality_score"]["api_key"], args.IP)
	else:
		print("Please set IP Quality Score API key in `config.ini` file")
		exit(1)

	reputation = ip.get_reputation()
	ip.parse_reputation(reputation)
