from gophish.models import Group
from gophish.api.groups import API
from colored import fg, attr
from random import randint


class GroupsMenu():
    def __init__(self, client=None):
        self.groups_menu_color = randint(1, 220)
        self.client = client

    def prompt(self):
        while (
            i := input(
                "(%sGroups%s) %s " %(fg(self.groups_menu_color), attr(0), "%")
            ).strip().lower()):
            if i == "back":
               return 
            else:
                print(
                    "<[%s-%s]> Invalid option ..."
                    %(fg(self.groups_menu_color),attr(0))
                    )

    def get_groups():
        pass
