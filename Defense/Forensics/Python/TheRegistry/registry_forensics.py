from winreg import (
                    ConnectRegistry,
                    OpenKey,
                    KEY_ALL_ACCESS,
                    EnumValue,
                    QueryInfoKey,
                    HKEY_LOCAL_MACHINE,
                    HKEY_CURRENT_USER
                    )
def enum_key(hive, subkey:str):
    with OpenKey(hive, subkey, 0, KEY_ALL_ACCESS) as key:
        num_of_values = QueryInfoKey(key)[1]
        for i in range(num_of_values):
            values = EnumValue(key, i)
            if values[0] == "LangID": continue
            print(*values[:-1], sep="\t")
if __name__ == "__main__":
    # Connecting to the HKEY_LOCAL_MACHINE hive
    with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hklm_hive:
        print("\nCurrent Version/Build Info")
        print("-"*50)
        enum_key(hklm_hive, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        print("\nSystem Environment Variables")
        print("-"*50)
        enum_key(hklm_hive, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
        print("\nStartup Applications")
        print("-"*50)
        enum_key(hklm_hive, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
    # Connecting to the HKEY_CURRENT_USER hive
    with ConnectRegistry(None, HKEY_CURRENT_USER) as hkcu_hive:
        print("\nPreviously rand applications")
        print("-"*50)
        enum_key(hkcu_hive, r"SOFTWARE\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache")
