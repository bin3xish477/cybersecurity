#!/usr/bin/env python3


from requests import get
from os.path import join, exists
from os import mkdir, environ
from sys import exit
from xml.etree import ElementTree as ET
from argparse import ArgumentParser


__author__ = "Alexis Rodriguez"
__date__   = 20201203


parser = ArgumentParser()
parser.add_argument("INFILE", help="File with data to parse")
parser.add_argument("-d", "--output-dir", help="Directory to output results into")
parser.add_argument("-e", "--env",
	action="store_true",
	help="Use environment variables for api authentication (API_NAME, API_TOKEN)"
	)


def main():
	args = parser.parse_args()


if __name__ == '__main__':
	main()