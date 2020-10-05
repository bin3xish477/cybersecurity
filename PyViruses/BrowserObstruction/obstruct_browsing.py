#!/usr/bin/env python3

""" A very scans a system for any running browsers and terminates them """

from psutil import process_iter
from os import kill
from signal import SIGTERM
from time import sleep
target_browser_executables = ('chrome.exe', 'firefox.exe', 'explorer.exe')
testing_target = ['notepad.exe']
while True:
  running_processes = {p.pid: p.info['name'] for p in process_iter(["pid", "name"])}
  for pid, p_name in running_processes.items():
    if p_name in testing_target:
      kill(pid, SIGTERM)
      sleep(10
