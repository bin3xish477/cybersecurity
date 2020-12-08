from gophish.models import Page
from gophish.api.pages import API
from colored import fg, attr
from random import randint


class PagesMenu:
    def __init__(self, client=None):
        self.pages_menu_color = randint(1, 220)
        self.client = client

    def prompt(self):
        while (
            i := input(
                "(%spages%s) %s " %(fg(self.pages_menu_color), attr(0), "%")
            ).strip().lower()):
            if i == "back":
               return 
            else:
                print(
                    "<[%s-%s]> Invalid option ..."
                    %(fg(self.pages_menu_color),attr(0))
                    )

