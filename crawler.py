import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
         pass
    except requests.exceptions.InvalidURL:
        pass
    
target_url = input("Enter a URL: ")

with open("files-and-dirs-wordlist.txt", "r") as wordlist_file:
    for word in wordlist_file:
        word = word.strip("\n")
        url = target_url + "/" + word
        response = request(url)
        if response:
            print("[+] discovered subdomain --> " + url)
