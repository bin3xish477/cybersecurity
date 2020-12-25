from winreg import (
                    ConnectRegistry,
                    OpenKey,
                    KEY_ALL_ACCESS,
                    EnumKey,
                    EnumValue,
                    QueryInfoKey
                    HKEY_LOCAL_MACHINE
                    )
if __name__ == "__main__":
    with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hive:
        with OpenKey(hive, r"Comm\\Tcpip\\Hosts", 0, KEY_ALL_ACCESS) as hosts_key:
            keys = EnumKey(hosts_key)
            values = EnumValue(hosts_key)





