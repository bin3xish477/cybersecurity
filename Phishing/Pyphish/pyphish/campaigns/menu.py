from gophish.models import Campaign, Stat
from gophish.api.campaigns import API 
from tabulate import tabulate
from colored import fg, attr
from random import randint


class CampaignsMenu():
    def __init__(self, client=None):
        self.campaign_menu_color = randint(1, 220)
        self.client = client

    def prompt(self):
        while (
            i := input(
                "(%scampaigns%s) %s " %(fg(self.campaign_menu_color), attr(0), "%")
            ).strip().lower()):
            if i == "back":
               return 
            else:
                print(
                    "<[%s-%s]> Invalid option ..." 
                    %(fg(self.campaign_menu_color),attr(0))
                    )

