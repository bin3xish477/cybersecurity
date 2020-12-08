#!/usr/bin/env python3
from gophish import Gophish
from os import environ
from requests import packages
from readline import set_completer, parse_and_bind
from random import randint
from colored import fg, attr
from tabulate import tabulate
from pyphish.campaigns.menu import CampaignsMenu
from pyphish.groups.menu import GroupsMenu
from pyphish.templates.menu import TemplatesMenu
from pyphish.pages.menu import PagesMenu
from pyphish.profiles.menu import ProfilesMenu
from pyphish.utils.autocompleter import auto_complete
from json import load


__author__ = "binexisHATT"
__version__ = 1.0


if __name__ == "__main__":
    set_completer(auto_complete)
    parse_and_bind("tab: complete")
    packages.urllib3.disable_warnings()
    prog_color = randint(1, 220)


    config_file = load(open("config.json"))
    config_file["api_key"] = environ["GOPHISH_API_KEY"]
    gophish_client = Gophish(config_file["api_key"], host=config_file["host"], verify=False)

    print("""
\t┌────────────────────────────┐                                                                                         
\t│░█▀█░█░█░█▀█░█░█░▀█▀░█▀▀░█░█│                                                                                         
\t│░█▀▀░░█░░█▀▀░█▀█░░█░░▀▀█░█▀█│                                                                                         
\t│░▀░░░░▀░░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀│                                                                                         
\t└────────────────────────────┘
    \tAuthor: @{}
    \tVersion: {}
""".format(("%s"+__author__+"%s")%(fg(randint(1,220)),attr(0)), __version__))

    main_menu_options = [
        ("campaigns", "Enter campaigns menu"),
        ("groups", "Enter groups menu"),
        ("template", "Enter templates menu"),
        ("pages", "Enter landing pages menu"),
        ("profiles", "Enter profiles menu"),
        ("info", "Get server configuration details"),
        ("clear|cls", "Clear screen"),
        ("help", "Show this help menu"),
        ("exit", "Exit program")
    ]

    info = lambda: tabulate([
        ("Gophish API Key", gophish_client.client.api_key),
        ("Host", gophish_client.client.host),
        ], headers=["Key", "Value"])

    try:
        while (
            c := input("(%sMain%s) %s " %(fg(prog_color),attr(0),"%")
            ).strip().lower()) != "exit": 
            if c == "info":
                print("\n"+info(), "\n")
            elif c == "campaigns":
                _ = CampaignsMenu(client=gophish_client).prompt()
            elif c == "groups":
                _ = GroupsMenu(client=gophish_client).prompt()
            elif c == "templates":
                _ = TemplatesMenu(client=gophish_client).prompt()
            elif c == "pages":
                _ = PagesMenu(client=gophish_client).prompt()
            elif c == "profiles":
                _ = ProfilesMenu(client=gophish_client).prompt()
            elif c == "help":
                print("\n" + 
                    tabulate(main_menu_options, 
                    headers=["Commands", "Action"]),
                    "\n")
            elif c in ("clear", "cls"):
                for _ in range(80): print()
            else:
                print("<[%s-%s]> Invalid option ..." %(fg(prog_color),attr(0)))
    except KeyboardInterrupt:
        print("\n%s<[-]>%s Goodbye ..." %(fg(prog_color),attr(0)))

