#!/usr/bin/env python3
from stem import Signal
from stem.control import Controller
from argparse import ArgumentParser as AP
from fake_useragent import UserAgent
from requests import get
from os import environ
from bs4 import BeautifulSoup as bs
from colored import fg, attr
from re import compile, findall, IGNORECASE
from prettytable import PrettyTable as PT
from random import randint


__author__ = "Alexis Rodriguez", "binexisHATT"
__date__   = 12_09_2020


row_data_cell_re = compile(r'<td [\w="]+>([\w\s\.@:()\'-0-9]+)<\/td>')


def extract_row_data_cells(row: str):
        return row_data_cell_re.findall(row, IGNORECASE)
        

def parse_response(resp: str):
    html_parser = bs(resp.text, "html.parser")
    #print(html_parser.prettify())

    all_tables = html_parser.findAll("table")
    general_details = all_tables[2]
    physical_appearance = all_tables[3]
    personality = all_tables[4]
    federal_taxpayer_id_nums = all_tables[5]
    
    general_details_tbl = PT()
    general_details_tbl.field_names = [
        "%sGeneral Details%s" % (fg(randint(1, 220)), attr(0)), 
        "%sValues%s" % (fg(randint(1, 220)), attr(0))
        ]
    for row in general_details.findAll("tr"):
        v = extract_row_data_cells(str(row))
        if len(v) != 2: continue
        else: general_details_tbl.add_row(v)
    print(general_details_tbl)

    physical_appearance_tbl = PT()
    physical_appearance_tbl.field_names = [
        "%sPhysical Appearance%s" % (fg(randint(1, 220)), attr(0)), 
        "%sValues%s" % (fg(randint(1, 220)), attr(0))
        ]
    for row in physical_appearance.findAll("tr"):
        v = extract_row_data_cells(str(row))
        if len(v) != 2: continue
        else: physical_appearance_tbl.add_row(v)
    print(physical_appearance_tbl)

    personality_tbl = PT()
    personality_tbl.field_names = [
        "%sPersonality Traits%s" % (fg(randint(1, 220)), attr(0)), 
        "%sValues%s" % (fg(randint(1, 220)), attr(0))
        ]
    for row in personality.findAll("tr"):
        v = extract_row_data_cells(str(row))
        if len(v) != 2: continue
        else: personality_tbl.add_row(v)
    print(personality_tbl)

    federal_taxpayer_tbl = PT()
    federal_taxpayer_tbl.field_names = [
        "%sUS Federal Taxpayer Id Number (Tin)%s" % (fg(randint(1, 220)), attr(0)), 
        "%sTax ID%s" % (fg(randint(1, 220)), attr(0))
        ]
    for row in federal_taxpayer_id_nums.findAll("tr"):
        v = extract_row_data_cells(str(row))
        if len(v) != 2: continue
        else: federal_taxpayer_tbl.add_row(v)
    print(federal_taxpayer_tbl)


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
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=environ["TOR_PASS"])
        controller.signal(Signal.NEWNYM)

    
if __name__ == "__main__":
    hidden_service_url = "http://elfq2qefxx6dv3vy.onion/fakeid.php"

    parser = AP(description="Generate identity to browse the Dark Web")
    parser.add_argument(
        "-g", "--gender",
        choices=("female", "male", "random"),
        default="random",
        help="Select the gender to generate a Fake Id for"
        )

    args = parser.parse_args()

#    for _ in range(10):
#        resp = make_request(hidden_service_url)
#        create_new_tor_ip()
#        print(resp.text)
#        sleep(5)

    resp = make_request(hidden_service_url, args.gender)
    #print(resp.text)
    parse_response(resp)

    
