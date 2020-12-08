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
from pyphish.smtp.menu import SMTPMenu
from pyphish.utils.autocompleter import auto_complete


__author__ = "binexisHATT"
__version__ = 1.0


if __name__ == "__main__":
    # Applying autocomplete functionality
    set_completer(auto_complete)
    parse_and_bind("tab: complete")
    # Disable SSL warnings
    packages.urllib3.disable_warnings()
    # Random color option for every new pyphish running instance
    prog_color = randint(1, 220)

    gophish_api_key = environ["GOPHISH_API_KEY"]
    gophish_client = Gophish(gophish_api_key, verify=False)

    print("""
\t┌────────────────────────────┐                                                                                         
\t│░█▀█░█░█░█▀█░█░█░▀█▀░█▀▀░█░█│                                                                                         
\t│░█▀▀░░█░░█▀▀░█▀█░░█░░▀▀█░█▀█│                                                                                         
\t│░▀░░░░▀░░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀│                                                                                         
\t└────────────────────────────┘
    \tAuthor: @{}
    \tVersion: {}
""".format(__author__, __version__))

    main_menu_options = [
        ["campaigns", "Enter campaigns menu"],
        ["groups", "Enter groups menu"],
        ["template", "Enter templates menu"],
        ["pages", "Enter landing pages menu"],
        ["smtp", "Enter STMP menu"],
        ["help", "Show this help menu"],
        ["exit", "Exit program"]
    ]

    try:
        while (
            c := input("(%smain%s) %s " %(fg(prog_color),attr(0),"%")
            ).strip().lower()) != "exit": 
            if c == "campaigns":
                _ = CampaignsMenu(client=gophish_client).prompt()
            elif c == "groups":
                _ = GroupsMenu(client=gophish_client).prompt()
            elif c == "templates":
                _ = TemplatesMenu(client=gophish_client).prompt()
            elif c == "pages":
                _ = PagesMenu(client=gophish_client).prompt()
            elif c == "smtp":
                _ = SMTPMenu(client=gophish_client).prompt()
            elif c == "help":
                print(tabulate(main_menu_options, headers=["Commands", "Command Action"]))
            elif c in ("cls", "clear"):
                for _ in range(100): print()
            else:
                print("<[%s-%s]> Invalid option ..." %(fg(prog_color),attr(0)))
    except KeyboardInterrupt:
        print("\n%s<[-]>%sGoodbye ..." %(fg(prog_color),attr(0)))

