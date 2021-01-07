from gophish.models import SMTP
from gophish.api.smtp import API
from colored import fg, attr
from random import randint
from tabulate import tabulate


class ProfilesMenu():
    def __init__(self, client=None):
        self.profiles_menu_color = randint(1, 220)
        self.client = client

        self.profiles_menu_options = [
            ("get", "Enter get profile menu"),
            ("create", "Enter create profile menu"),
            ("edit", "Enter edit profile menu"),
            ("delete", "Enter delete profile menu"),
            ("back", "Go back to the main menu"),
            ("help", "Show this help menu"),
        ]

    def prompt(self):
        while (
            c := input(
                "(%sProfiles%s) %s " %(fg(self.profiles_menu_color), attr(0), "%")
            ).strip().lower().split()):
            if c[0] == "back":
               return 
            elif c[0] == "get":
                self.get_profile_menu()
            elif c[0] == "create":
                self.create_profile_menu()
            elif c[0] == "edit":
                self.edit_profile_menu()
            elif c[0] == "delete":
                self.delete_profile_menu()
            elif c[0] == "help":
                print("\n" +
                    tabulate(self.profiles_menu_options,
                    headers=["Command", "Action"]),
                    "\n")
            elif c[0] in ("clear", "cls"):
                for _ in range(80): print()
            elif c[0] == "exit":
                raise KeyboardInterrupt()
            else:
                print(
                    "<[%s-%s]> Invalid option ..."%(fg(self.profiles_menu_color),attr(0))
                    )
        
    def get_profile_menu(self):
        get_profile_menu_options = [

        ]

        while (
            c := input(
                "(Get)(%sProfiles%s) %s " %(fg(self.profiles_menu_color), attr(0), "%")
            ).strip().lower().split()):
            if c[0] == "info":
                info()
            if c[0] == "back":
               return 
            elif c[0] == "help":
                print("\n" +
                    tabulate(get_profile_menu_options,
                    headers=["Command", "Action"]),
                    "\n")
            elif c[0] in ("clear", "cls"):
                for _ in range(80): print()
            elif c[0] == "exit":
                raise KeyboardInterrupt()
            else:
                print(
                    "<[%s-%s]> Invalid option ..."%(fg(self.profiles_menu_color),attr(0))
                    )

    def create_profile_menu(self):
        create_profile_menu_options = [
            ("info", "Get current profile information"),
            ("set", "Set a value"),
            ("create", "Create profile"),
            ("help", "Show this help menu"),
            ("back", "Go back to the Profile menu"),
        ]

        name = "N/A"
        host = "N/A"
        from_address = "N/A"
        interface_type = "SMTP (Default, Non other supported by Gophish)"
        ignore_cert_errors = True

        info = lambda: tabulate([
            ("name", name),
            ("host", host),
            ("email address", from_address),
            ("interface type", interface_type),
            ("ignore cert errors", ignore_cert_errors)
        ], headers=["Key", "Value"])
        
        while (
            c := input(
                "(Create)(%sProfiles%s) %s " %(fg(self.profiles_menu_color), attr(0), "%")
            ).strip().lower().split()):
            if c[0] == "info":
                print("\n"+info(), "\n")
            elif c[0] == "back":
               return 
            elif c[0] == "help":
                print("\n" +
                    tabulate(create_profile_menu_options,
                    headers=["Command", "Action"]),
                    "\n")
            elif c[0] in ("clear", "cls"):
                for _ in range(80): print()
            elif c[0] == "exit":
                raise KeyboardInterrupt()
            else:
                print(
                    "<[%s-%s]> Invalid option ..."%(fg(self.profiles_menu_color),attr(0))
                    )

    def edit_profile_menu(self, profile_id: int):
        edit_profile_menu_options = [

        ]

        while (
            c := input(
                "(Edit)(%sProfiles%s) %s " %(fg(self.profiles_menu_color), attr(0), "%")
            ).strip().lower().split()):
            if c[0] == "info":
                info()
            if c[0] == "back":
               return 
            elif c[0] == "help":
                print("\n" +
                    tabulate(edit_profile_menu_options,
                    headers=["Command", "Action"]),
                    "\n")
            elif c[0] in ("clear", "cls"):
                for _ in range(80): print()
            elif c[0] == "exit":
                raise KeyboardInterrupt()
            else:
                print(
                    "<[%s-%s]> Invalid option ..."%(fg(self.profiles_menu_color),attr(0))
                    )

    def delete_profile_menu(self, profile_id: int):
        delete_profile_menu_options = [

        ]

        while (
            c := input(
                "(Delete)(%sProfiles%s) %s " %(fg(self.profiles_menu_color), attr(0), "%")
            ).strip().lower().split()):
            if c[0] == "info":
                info()
            if c[0] == "back":
               return 
            elif c[0] == "help":
                print("\n" +
                    tabulate(delete_profile_menu_options,
                    headers=["Command", "Action"]),
                    "\n")
            elif c[0] in ("clear", "cls"):
                for _ in range(80): print()
            elif c[0] == "exit":
                raise KeyboardInterrupt()
            else:
                print(
                    "<[%s-%s]> Invalid option ..."%(fg(self.profiles_menu_color),attr(0))
                    )
