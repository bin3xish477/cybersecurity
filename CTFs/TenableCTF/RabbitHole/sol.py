from requests import get
from time import sleep
from re import search

proxies = {
        "http": "http://127.0.0.1:8080",
        "https":"https://127.0.0.1:443"
        }

letters_and_nums = ""

def send_req(base_url, page=None):
    global letters_and_nums

    if page:
        params = {"page": page}
    else:
        params = {}

    #resp = get(base_url, params=params, proxies=proxies).text
    resp = get(base_url, params=params).text
    print(resp)
    if "flag" not in resp:
        page = search(r"([A-Za-z0-9]{5,})", resp).group(1)
        h = search(r"\'([A-Fa-f0-9]{2})\'", resp).group(1)
        letters_and_nums += (":" + h)
        print(letters_and_nums)
        #b = bytes.fromhex(h)
        #try:
        #    print(b.decode("ASCII"))
        #except:
        #    pass
    return page


def main():
    url = "http://167.71.246.232:8080/rabbit_hole.php"
    page = send_req(url)
    while True:
        page = send_req(url, page)
        sleep(0.5)

main()
