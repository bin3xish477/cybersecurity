#!/usr/bin/env python3

from sys import argv
from ctypes import (
    windll,
    byref,
    c_long
) 
from winreg import (
    HKEY_CURRENT_USER,
    ConnectRegistry,
    OpenKey,
    KEY_ALL_ACCESS,
    EnumValue,
    SetValueEx,
    QueryInfoKey,
    REG_SZ
)

def change_wallpaper(image: str):
   with ConnectRegistry(None, HKEY_CURRENT_USER) as hkcu:
        with \
            OpenKey(hkcu, r"Control Panel\Desktop", 0, KEY_ALL_ACCESS) \
        as desktop_key:
            print(f"[+] Changing wallpaper to {image} ...")
            SetValueEx(desktop_key, "WallPaper", 0, REG_SZ, image)

            # the following lines of code is boiler plate code
            # for making telling Windows that registry settings have changed
            # and that it needs to refresh
            HWND_BROADCAST = 0xFFFF
            WM_SETTINGCHANGE = 0x1A
            SMTO_ABORTIFHUNG = 0x0002
            result = c_long()
            SendMessageTimeoutW = windll.user32.SendMessageTimeoutW
            SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u'Control Panel\\Desktop', SMTO_ABORTIFHUNG, 5000, byref(result),)

if __name__ == "__main__":
    path_to_image: str = argv[1]
    change_wallpaper(path_to_image)
