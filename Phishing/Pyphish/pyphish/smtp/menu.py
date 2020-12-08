from gophish.models import SMTP
from gophish.api.smtp import API
from colored import fg, attr
from random import randint


class SMTPMenu():
    def __init__(self, client=None):
        self.smtp_menu_color = randint(1, 220)
        self.client = client

    def prompt(self):
        while (
            i := input(
                "(%ssmtp%s) %s " %(fg(self.smtp_menu_color), attr(0), "%")
            ).strip().lower()):
            if i == "back":
               return 
            else:
                print(
                    "<[%s-%s]> Invalid option ..."%(fg(prog_color),attr(0))
                    )
