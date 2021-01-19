#!/usr/bin/env python3

from configparser import ConfigParser

from canary_watcher import CanaryWatcher

if __name__ == "__main__":
    with CanaryWatcher(ConfigParser().read("config.ini")) as cw:
        pass
