#!/usr/bin/env python3
from winreg import (

)

from ctypes import (

)

# Must add a key-value pair to this registry key:
#   [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run]

# TODO:
#   - create backdoor file on execution in common writable windows dir for user
#   - add element to windows startup registry
#   - flush registry modification with ctypes

if __name__ == "__main__":
  main()
