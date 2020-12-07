#!/usr/bin/env python3

# pip3 install gophish
from gophish import Gophish
from os import environ
from requests import packages
from readline import set_completer, parse_and_bind
from random import randint
from colored import fg, attr
from pyphish.campaigns.menu import show as campaigns_menu
from pyphish.groups.menu import show as groups_menu
from pyphish.templates.menu import show as templates_menu
from pyphish.pages.menu import show as pages_menu
from pyphish.smtp.menu import show as smtp_menu
from pyphish.utils.autocompleter import auto_complete


set_completer(auto_complete)
parse_and_bind("tab: complete")
packages.urllib3.disable_warnings()

prog_color = randint(1, 220)

if __name__ == "__main__":
    gophish_api_key = environ["GOPHISH_API_KEY"]
    phish_client = Gophish(gophish_api_key, verify=False)

    try:
        while (choice := input("Enter options: ").strip()) != "exit":
            if choice == "Campaigns":
                campaigns_menu()
            elif choice == "Groups":
                templates_menu()
            elif choice == "Templates":
                groups_menu()
            elif choice == "Pages":
                pages_menu()
            elif choice == "SMTP":
                smtp_menu()
            else:
                print("<[%s-%s]> Invalid option ..." % (fg(prog_color), attr(0)))
    except KeyboardInterrupt:
        print("<[%s-%s]> Exiting Pyphish interface ... Goodbye" % (fg(prog_color), attr(0)))

