#!/usr/bin/env python3

from emailer import Emailer

from os import environ
from os import stat

from os.path import exists
from os.path import isfile
from os.path import realpath

from time import sleep

from argparse import ArgumentParser

def watch_canary(f):
    initial_file_access_time = stat(f).st_atime
    sleep(5)

    while True:
        file_access_time = stat(f).st_atime
        
        if file_access_time != initial_file_access_time:
            
            gmail_address = environ["GMAIL_ADDR"]
            gmail_password  = environ["GMAIL_PASS"]

            with Emailer("smtp.gmail.com", 465) as email:
                
                # Remove print statements when running as cronjob or
                # scheduled task
                if email.authenticate(gmail_address, gmail_password):
                    print("{*} Authentication successful!")
                else:
                    print("{-} Authentication unsuccessful!")

                subject = "[WARNING] Canary Triggered"
                message = f"Someone accessed the canary file:\n\t {realpath(f)}"

                if email.send(gmail_address, subject, message):
                    print("{*} Successfully sent email!")
                else:
                    print("{*} Email could not be sent!")
            break
        sleep(5)

if __name__ == "__main__":
    parser = ArgumentParser(description="Basic file canary Python program")
    parser.add_argument("FILE", help="File to act as canary")

    args = parser.parse_args()
    
    if exists(args.FILE) and isfile(args.FILE):
        watch_canary(args.FILE)
    else:
        print(f"{{-}} {args.FILE} does not exist!")

