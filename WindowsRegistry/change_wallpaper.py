#!/usr/bin/env python3

from sys import argv
from winreg import (
    HKEY_CURRENT_USER,
    ConnectRegistry,
    KEY_WRITE,
    EnumValue
)

def change_wallpaper(image: str):
   # specify None for first arg so winreg can find the default
   # computer name, otherwise specify computer name
   with ConnectRegistry(None, HKEY_CURRENT_USER) as hkey:
        with 
            # KEY_WRITE is basically like specifying "w" mode
            OpenKey(hkey, r"Control Panel\Desktop", 0, KEY_WRITE)
        as desktop_key:
           for i in enumerate(range(1, 10)):
               print(desktop_key.EnumValue(desktop_key, i))

if __name__ == "__main__":
    path_to_image: str = argv[1]
    change_wallpaper()
