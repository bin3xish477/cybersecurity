#!/usr/bin/env python3
from stem import Signal
from stem.control import Controller
from argparse import ArgumentParser
from fake_useragent import UserAgent
from json import dump
from csv import writer
from requests import get
from os import environ
from time import sleep
from bs4 import BeautifulSoup
from colored import fg, attr
from re import findall, IGNORECASE


__author__ = "Alexis Rodriguez", "binexisHATT"
__date__   = 12_09_2020


def parse_response(resp: str):
    html_parser = BeautifulSoup(resp.text, "html.parser")
    #print(html_parser.prettify())
    all_tables = html_parser.findAll("table")
    general_attributes = all_tables[2]
    physical_appearance = all_tables[3]
    personality = all_tables[4]
    federal_taxpayer_id_nums = all_tables[5]
    
    for row in general_attributes.findAll("tr"):
        value = findall(
            r'<td [\w="]+>([\w\s\.@:()\'-0-9]+)<\/td>', str(row),
            IGNORECASE)
        print(value)

    for row in physical_appearance.findAll("tr"):
        value = findall(
            r'<td [\w="]+>([\w\s\.@:()\'-0-9]+)<\/td>', str(row),
            IGNORECASE)
        print(value)

    for row in personality.findAll("tr"):
        value = findall(
            r'<td [\w="]+>([\w\s\.@:()\'-0-9]+)<\/td>', str(row),
            IGNORECASE)
        print(value)

    for row in federal_taxpayer_id_nums.findAll("tr"):
        value = findall(
            r'<td [\w="]+>([\w\s\.@:()\'-0-9]+)<\/td>', str(row),
            IGNORECASE)
        print(value)


def make_request(url: str, gender: str):
    # Specifying Tor service as proxy
    # to use SOCKS over Tor

    tor_proxy = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }

    random_user_agent = UserAgent().random
    headers = {
        "User-Agent": random_user_agent
        }

    if gender == "female":
        url = url + "?gender=f"
    elif gender == "male":
        url = url + "?gender=m"
    else: 
        url = url + "?gender=r"

    resp = get(url, headers=headers, proxies=tor_proxy)
    #Testing url
    #resp = get("http://httpbin.org/ip", headers=headers, proxies=tor_proxy)

    return resp


def create_new_tor_ip():
    with Controller.from_port(port=9051) as c:
        c.authenticate(password=environ["TOR_PASS"])
        c.signal(Signal.NEWNYM)


def write_to_file(file_name: str, file_type: str):
    pass

    
if __name__ == "__main__":
    hidden_service_url = "http://elfq2qefxx6dv3vy.onion/fakeid.php"

    parser = ArgumentParser()
    parser.add_argument("-g", "--gender",
        choices=("female", "male", "random"),
        default="random",
        help="Select the gender to generate a Fake Id for")
    parser.add_argument("-f", "--outfile",
        choices=("txt", "json", "csv"),
        help="Specify file type to save fake identity to")  

    args = parser.parse_args()

#    for _ in range(10):
#        resp = make_request(hidden_service_url)
#        create_new_tor_ip()
#        print(resp.text)
#        sleep(5)

    resp = make_request(hidden_service_url, args.gender)
    #print(resp.text)
    parse_response(resp)

    
