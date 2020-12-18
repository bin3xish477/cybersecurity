#!/usr/bin/env python3


from requests import get
from os.path import join, exists
from os import mkdir, environ
from sys import exit
from argparse import ArgumentParser
from json import load
from csv import DictWriter


__author__ = "Alexis Rodriguez"
__date__   = 20201203


parser = ArgumentParser()
parser.add_argument("-mf", "--mac-file",
    action="store_true",
	help="Use `mac_addr.json` file for specifying MAC addresses"
	)
parser.add_argument("-m", "--mac",
	help="Provide one MAC address to query"
	)
parser.add_argument(
    "-d", "--output-dir",
    help="Directory to output results into",
    default="."
    )
parser.add_argument("-e", "--env",
	action="store_true",
	help="Use environment variables for api authentication (API_NAME, API_TOKEN)"
	)


def invoke_wigle_api(
    api_auth: tuple, api_url: str, wifi_dict: dict
    ):

    for mac in wifi_dict:
        api_url = f"{api_url}?netid={mac}"
        api_resp = get(api_url, auth=api_auth).json()
        print(api_resp)
        continue
        
        try:
            if api_resp["resultCount"] == 0:
                wifi_dict[mac]["wigle"]["results"] = []
            else:
                wifi_dict[mac]["wigle"]["results"] = api_resp["results"]
        except KeyError:
            if api_resp["message"] == "too many queries today":
                print("(-)", api_resp["message"])
                continue
            else:
                print(
                    f"(-) An error occured while querying Wigle " \
                    "API for MAC address {mac}"
                    )
                continue

    return wifi_dict
    

def gen_wifi_dict(mac_addrs: list):

    wifi_dict = {}
    for mac in mac_addrs:
        wifi_dict[mac] = {"time_stamps": ["n/a"], "ssid": ["n/a"], "wigle": {}}

    return wifi_dict
    

def prep_output(wifi_dict: dict):
    pass

def output_to_csv(out_dir: str, wifi_results: dict):
    pass


def main():

    args = parser.parse_args()

    api_url = "https://api.wigle.net/api/v2/network/search"

    if args.mac_file or args.mac:
        if args.mac_file:
            with open("mac_addr.json") as macf:
                mac_addrs = [
                    mac_addr.strip() for mac_addr in load(macf)["mac_addrs"]
                    ]
        elif args.mac:
            mac_addrs = [args.mac]
    else:
        print("(-) must provide `-mf` or `-m` argument")
        exit(1)


    if args.env:
        api_name, api_token = environ["API_NAME"], environ["API_TOKEN"]
    else:
        with open("api.json") as apif:
            api_auth = load(apif)
            api_name, api_token = api_auth["api_name"], api_auth["api_token"]

    if args.output_dir and not exists(args.output_dir):
        mkdir(args.output_dir)
        
    empty_wifi_dict = gen_wifi_dict(mac_addrs)

    results_wifi_dict = invoke_wigle_api(
        api_auth=(api_name, api_token),
        api_url=api_url,
        wifi_dict=empty_wifi_dict,
        )
    print(results_wifi_dict)

    #prepared_output = prep_output(results_wifi_dict)
    #output_to_csv(args.output_dir, prepared_output)
    

if __name__ == '__main__':
	main()
