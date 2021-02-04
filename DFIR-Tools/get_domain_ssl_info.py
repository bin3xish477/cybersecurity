#!/usr/bin/env python3
from requests import get
from argparse import ArgumentParser
from colors import bkgrd
from colors import bold
from colors import green
from json import loads
from configparser import ConfigParser
from os import environ

__author__ = "BinexisHATT"
__date__   = "02/01/2021"

class DomainSSLCert:
	def __init__(self, domain, api_key):
		self.url = "https://api.threatintelligenceplatform.com/v1/sslCertificatesChain"
		self.domain = domain
		self.api_key = api_key

	def get_ssl_info(self):
		params = {
			"domainName": self.domain,
			"apiKey": self.api_key
		}
		return get(self.url, params=params).text

	def parse_ssl_info(self, ssl_chain):
		#ssl_chain = loads(ssl_chain)

		print(bkgrd("[SSL INFO]", "purple_1a"))
		for item in ssl_chain:
			for key, value in item.items():
				if isinstance(value, dict):
					print(key, "::")
					for k, v in value.items():
						print("\t", k, "::", v)
				elif isinstance(value, list):
					print(key, "::")
					for elem in value:
						print("\t", elem)
				else:
					print(key,"::", value)
			print(bold(green("+"*65)), "\n")

if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument("DOMAIN", help="The domain to retrieve SSL certificate information for")

	args = parser.parse_args()
	config = ConfigParser()
	config.read("config.ini")

	#domain = DomainSSLCert(args.DOMAIN, config["threat_intelligence_platform"]["api_key"])
	domain = DomainSSLCert(args.DOMAIN, environ["TTP_KEY"])
	#ssl_info = domain.get_ssl_info()
	domain.parse_ssl_info(sample_results)
