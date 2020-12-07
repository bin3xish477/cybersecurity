#!/usr/bin/env python3

# pip3 install gophish
from gophish import Gophish
from gophish.models import (
    Campaign, Groups, Template, 
    Attachments, Pages, SMTP, Stat
    )
from gophish.api import (
    campaigns, groups, templates,
    pages, smtp
    )
from os import environ
from requests import packages


# Disable ssl warnings
packages.urllib3.disable_warnings()


gophish_api_key = environ["GOPHISH_API_KEY"]


class ComponentManager():
    def __init__():
        self.name = name

    def create_campaign(campaign: Campaign):
        pass

    def create_group(group: Group):
        pass
        
    def create_template(template: Template):
        pass

    def create_page(landing_page: Page):
        pass

    def create_smtp_profile(smtp_profile: SMTP):
        pass

    def get_campaign_stats(name: str):
        pass

    def delete_campaign(name: str):
        pass

    def delete_group(name: str):
        pass
        
    def delete_template(name: str):
        pass

    def delete_page(name: str):
        pass

    def delete_smtp_profile(name: str):
        pass


if __name__ == "__main__":
    phish_client = Gophish(gophish_api_key, verify=False)
    for campaign in phish_client.campaigns.get():
        print(compaign)
    for template in phish_client.templates.get():
        print(compaign)
