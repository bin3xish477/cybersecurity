from winreg import (
  ConnectRegistry,
  OpenKey,
  KEY_ALL_ACCESS,
  EnumValue,
  QueryInfoKey,
  HKEY_LOCAL_MACHINE,
  HKEY_CURRENT_USER
)
if __name__ == "__main__":
    with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hive:
        with OpenKey(hive, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", 0, KEY_ALL_ACCESS) as hosts_key:
            num_of_values = QueryInfoKey(hosts_key)[1]
            for i in range(num_of_values):
                values = EnumValue(hosts_key, i)
                print(values)
