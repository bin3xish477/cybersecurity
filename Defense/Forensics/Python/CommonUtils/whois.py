from argparse import ArgumentParser
from json import load
from os import environ
from sys import exit


__author__ = "Alexis Rodriguez"
__date__   = 20201201


api_url = "https://www.whoisxmlapi.com/whoisserver/WhoisService"


parser = ArgumentParser(description="Get whois info on specified domain")
parser.add_argument("DOMAIN", help="Domain name to query to query whois")
parser.add_argument("-k", "--apikey", help="Whoisxmlapi API key")


def main():
    args = parser.parse_args()
    print(args.DOMAIN)

    if not args.apikey:
        try:
            apikey = environ["WHOIS_APIKEY"]
        except KeyError:
            print("\n(-) Environment variable WHOIS_APIKEY has not been set")
            print("[*] Please set the WHOIS_APIKEY env variable or use the" \
                "`-k` argument")
            exit(1)
    

if __name__ == "__main__":
    main()
