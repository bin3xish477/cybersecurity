from os import environ
from time import sleep
from twitter_crawler import TwitterCrawler
from json import dump, load
from sys import exit
from pandas import DataFrame, set_option
from prog_args import parse_args
from gspread import service_account
from shutil import get_terminal_size

s=get_terminal_size((80, 20))
set_option('display.max_colwidth', s.columns-75)

def color_out(string, color) -> str:
    colors={
        "r": "\033[31m",
        "g": "\033[32m",
        "b": "\033[34m",
        "p": "\033[35m",
        "bold": "\033[1m",
        "end": "\033[0m"
    }
    if color=="r": return colors['r']+colors['bold']+string+colors['end']
    if color=="g": return colors['g']+colors['bold']+string+colors['end']
    if color=="b": return colors['b']+colors['bold']+string+colors['end']
    if color=="p": return colors['p']+string+colors['end']

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
    
    with open("api.json", "w") as f:
        f.seek(0)
        f.truncate(0)
        dump(api_info, f, indent=4)

    print("[++] Setup complete! The program is ready for usage...") 
    exit(1)

def main():
    # api_config_json=open("api.json", "r")
    # api_info=load(api_config_json)
    # for v in api_info.values():
    #     if v=="None":
    #         print("[!!] A value in config.json file has not been set")
    #         print("[**] Please enter all necessary values in the following setup process")
    #         setup()

    args=parse_args()

    api_info={}

    api_info["consumer_key"]		= environ.get("CONSUMER_KEY")
    api_info["consumer_secret"]		= environ.get("CONSUMER_SECRET")
    api_info["access_token_key"]	= environ.get("ACCESS_TOKEN_KEY")
    api_info["access_token_secret"]	= environ.get("ACCESS_TOKEN_SECRET")

    tw_crawler=TwitterCrawler(
        api_info["consumer_key"], api_info["consumer_secret"],
        api_info["access_token_key"], api_info["access_token_secret"]
    )
 
    #tw_crawler.get_timeline()
    c=args.count
    if c:
        if args.query:
            q=(" OR ".join(args.query))
            print("\n"+color_out("[++]", "r"), f"Search query: '{q}', Count: {c}\n")
            tweets=tw_crawler.search(count=c, to_query=q)
        else:
            print(
                "\n"+color_out("[++]", "r"),
                f"Search query: 'Malware OR Ransomware OR Advanced Persistent Threat OR CVE OR Cyber Threat OR Hacker', Count: {c}\n"
            )
            tweets=tw_crawler.search(count=c)
    else:
        if args.query:
            q=(" OR ".join(args.query))
            print("\n"+color_out("[++]", "r"), f"Search query: '{q}', Count: 200\n")
            tweets=tw_crawler.search(to_query=q)
        else:
            print(
                "\n"+color_out("[++]", "r"),
                f"Search query: 'Malware OR Ransomware OR Advanced Persistent Threat OR CVE OR Cyber Threat OR Hacker', Count: {c}\n"
            )
            tweets=tw_crawler.search()

    tweet_dates=[t.created_on for t in tweets]
    tweet_locations=[t.location for t in tweets]
    tweet_usernames=[t.username for t in tweets]
    tweet_texts=[t.text for t in tweets]
    
    if args.console:
        set_option("display.max_rows", len(tweets))
        d=DataFrame(
            {
                "Date": tweet_dates,
                "Location": tweet_locations,
                "Username": tweet_usernames,
                "Tweet": tweet_texts
            }
        )
        print(d)

    if args.auth_file:
        print(color_out("[**]", "g"), "Uploading results to a Google Sheet's Doc...")
        account=service_account(args.auth_file)
        sheet=account.open_by_key(args.url_key).sheet1

        row=len(sheet.col_values(1))+1
        for date, loc, user, tweet in zip(
            tweet_dates, tweet_locations, tweet_usernames, tweet_texts
        ):
           sheet.update_cell(row, 1, str(date))
           sheet.update_cell(row, 2, loc)
           sheet.update_cell(row, 3, user)
           sheet.update_cell(row, 4, tweet)
           row+=1
           sleep(0.5)
        print(color_out("[**]", "p"), "Finished uploading search results to Google Sheet's Doc...)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n",color_out("[CTRL+C]", "r"), " Killing Program...")
        exit(1)
