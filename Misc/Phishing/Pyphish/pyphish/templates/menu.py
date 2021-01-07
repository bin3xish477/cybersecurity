from gophish.models import Template, Attachment
from gophish.api.templates import API
from colored import fg, attr
from random import randint


class TemplatesMenu:
    def __init__(self, client=None):
        self.templates_menu_color = randint(1, 220)
        self.client = client

    def prompt(self):
        while (
            i := input(
                "(%sTemplates%s) %s " %(fg(self.templates_menu_color), attr(0), "%")
            ).strip().lower()):
            if i == "back":
               return 
            else:
                print(
                    "<[%s-%s]> Invalid option ..." 
                    %(fg(self.templates_menu_color),attr(0))
                    )
