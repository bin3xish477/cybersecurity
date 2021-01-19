#!/usr/bin/env python3
from emailer import Emailer
from os import environ

if __name__ == "__main__":

    gmail_address = environ["GMAIL_ADDR"]
    gmail_password  = environ["GMAIL_PASS"]

    with Emailer("smtp.gmail.com", 465) as email:

        if email.authenticate(gmail_address, gmail_password):
            print("{*} Authentication successful!")
        else:
            print("{-} Authentication unsuccessful!")

        if email.send(gmail_address, "Testing", "Test message"):
            print("{*} Successfully sent email!")
        else:
            print("{*} Email could not be sent!")


