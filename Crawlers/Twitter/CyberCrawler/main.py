from twitter_crawler import TwitterCrawler
from argparse import ArgumentParser
from json import dump, load
from sys import exit

def setup():
    print("\n\n\t\tSet up")
    print("----------------------------------------")
    consumer_key=input("Enter consumer key: ")
    consumer_secret=input("Enter consumer secret: ")
    access_token_key=input("Enter access token key: ")
    access_token_secret=input("Enter access token secret: ")

    if consumer_key=="": consumer_key="None"
    if consumer_secret=="": consumer_secret="None"
    if access_token_key=="": access_token_key="None"
    if access_token_secret=="": access_token_secret="None"

    api_info={
        "consumer_key": consumer_key,
        "consumer_secret": consumer_secret,
        "access_token_key": access_token_key,
        "access_token_secret": access_token_secret
    }
    
    with open("config.json", "w") as f:
        f.seek(0)
        f.truncate(0)
        dump(api_info, f, indent=4)

    print("[++] Setup complete! The program is ready for usage...") 
    exit(1)

def main():
    config_json=open("config.json", "r")
    api_info=load(config_json)
    for v in api_info.values():
        if v=="None":
            print("[!!] A value in config.json file has not been set")
            print("[**] Please enter all necessary values in the following setup process")
            setup()

    tw_crawler=TwitterCrawler(
        api_info["consumer_key"], api_info["consumer_secret"],
        api_info["access_token_key"], api_info["access_token_secret"]
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[--][CTRL+C] Killing program...")
        exit(1)
