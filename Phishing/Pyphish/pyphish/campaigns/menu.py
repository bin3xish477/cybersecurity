from gophish.models import Campaign, Stat
from tabulate import tabulate
from colored import fg, attr
from random import randint


class CampaignsMenu():
    def __init__(self, client=None):
        self.campaign_menu_color = randint(1, 220)
        self.client = client

        self.campaign_menu_options = [
            ("get-campaigns", "Get a list of all campaigns launched in Gophish"),
            ("create-campaign", "Create a new campaign"),
            ("edit-campaign", "Edit an existing campaign"),
            ("delete-campaign", "Delete an existing campaign"),
            ("clear|cls", "Clear screen"),
            ("back", "Go back to the main menu"),
            ("help", "Show this help menu"),
            ("exit", "Exit program")
        ]

    def prompt(self):
        while (
            c := input(
                "(%sCampaigns%s) %s " %(fg(self.campaign_menu_color), attr(0), "%")
            ).strip().lower()):
            if c == "back":
               return 
            elif c == "get-campaigns":
                self.get_campaigns()
            elif c == "create-campaigns":
                self.create_campaigns()
            elif c == "edit-campaigns":
                self.edit_campaigns()
            elif c == "delete-campaigns":
                self.delete_campaign()
            elif c in ("clear", "cls"):
                for _ in range(80): print()
            elif c == "help":
                print("\n" +
                    tabulate(self.campaign_menu_options,
                    headers=["Command", "Action"]),
                    "\n")
            elif c == "exit":
                raise KeyboardInterrupt()
            else:
                print(
                    "<[%s-%s]> Invalid option ..." 
                    %(fg(self.campaign_menu_color),attr(0))
                    )

    def get_campaigns(self):
        campaigns_list = []
        for campaign in self.client.campaigns.get():
            campaigns_list.append((campaign.id, campaign.name))
        print("\n" +
            tabulate(campaigns_list,
            headers=["Id", "Name"]),
            "\n")

    def create_campaign(campaign: Campaign):
        pass

    def edit_campaign(campaign_id: int):
        pass
        
    def delete_campaign(campaign_id: int):
        pass
        
