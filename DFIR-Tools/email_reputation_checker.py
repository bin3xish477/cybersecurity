#!/usr/bin/env python3
from requests import get
from argparse import ArgumentParser
from configparser import ConfigParser
from os import environ
from colors import red
from colors import white
from colors import bkgrd
from json import loads
from sys import exit

__author__ = "BinexisHATT"
__date__   = "02/01/2021"

class EmailRepChecker:
	def __init__(self, api_key, email):
		self.url = f"https://ipqualityscore.com/api/json/email/{api_key}/{email}"

	def get_reputation(self):
		params = {
			"abuse_strictness": 1,
			"strictness": 1
		}
		return get(self.url, params=params).text

	def parse_reputation(self, rep):
		rep = loads(rep)
		premium_keys = ("message", "success", "request_id")
		age = ("domain_age", "first_seen")

		print(bkgrd(white("[Reputation]"), "orange_red_1"))
		for key, value in rep.items():
			if key in premium_keys:
				continue
			elif key in age:
				print("\t\u2022 " + key.capitalize().replace("_", " "), "::")
				for k, v in rep[key].items():
					print(f"\t\t{k.capitalize()} -> {v}")
			else:
				print("\t\u2022 " + key.capitalize().replace("_", " "), "::", value)
		print("\n\tCheck out this link for more info about results:" \
			  "\n\t\t- https://www.ipqualityscore.com/documentation/email-validation/overview\n")

if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument("EMAIL_ADDRESS", help="The email address to check reputation for")

	args = parser.parse_args()

	config = ConfigParser()
	config.read("config.ini")

	if not config["ip_quality_score"]["api_key"]:
		email = EmailRepChecker(config["ip_quality_score"]["api_key"], args.EMAIL_ADDRESS)
	else:
		print("Please set IP Quality Score API key in `config.ini` file")
		exit(1)

	reputation = email.get_reputation()
	email.parse_reputation(reputation)
