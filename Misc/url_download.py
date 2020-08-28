from requests import get
from sys import argv, exit

def download(source):
    response = get(source)
    print(f"[+] Getting {source} data")
    if response.status_code == 200:
        source_file_name = source.split("/")[-1]
        with open(source_file_name, "wb") as opened_file:
            opened_file.write(response.content)
    print(f"[+] Successfully downloaded {source}")

if __name__ == "__main__":
    if len(argv) < 1:
        print(f"Usage: {argv[0]} <URL>")
        exit(1)
    source = argv[1].rstrip("/")
    download(source)
