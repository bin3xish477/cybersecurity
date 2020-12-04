from tarfile import open as taropen
from zipfile import ZipFile as zfopen
from sys import exit
from argparse import ArgumentParser


try:
    from pyscreenshot import grab
    import wx
except ImportError:
    print(
        "[-] Please run `pip3 install -r requirements.txt` " \
        "to install script dependencies..."
        )
    exit(1)


__author__ = "Alexis Rodriguez"
__date__   = 20201204


parser = ArgumentParser(description="Taking screenshots as you work")

if __name__ == "__main__":
    args = parser.parge_args()
    
