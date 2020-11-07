This program was created to collect cybersecurity (you can use this program to search anything but the intentions of the project are directed towards cybersecurity) information from Tweets posted on Twitter. I personally do not use Twitter but have heard enough cybersecurity professionals say that their main source of cybersecurity news comes from Twitter so I decided to create this simple program to scrape intelligence from Twitter and store it into a Google Sheet's documents.

Note: To use this program and all of it's features you need to acquire two things:
    - API tokens from a Twitter Developer account (setting up a Twitter developer account but hey it's worth it because you can also use it for your own future projects!)
    - A Google service account for interacting with a Google Sheet's document (this is also quite complicated if you have not interacted with Google's Developer Console

HELP
----

usage: main.py [-h] [-q [SearchTerm] [[SearchTerm] ...]] [-a FILENAME] [-k KEY] [-c COUNT] [-s]

Twitter Trending Cyber News or Vulnerabilities Crawler

optional arguments:
  -h, --help            show this help message and exit
  -q [SearchTerm] [[SearchTerm] ...], --query [SearchTerm] [[SearchTerm] ...]
                        The keyword/s to search for
  -a FILENAME, --auth-file FILENAME
                        JSON file containing Google Sheets API identity info
  -k KEY, --url-key KEY
                        The random key found within the URL of the google sheets doc
  -c COUNT, --count COUNT
                        The number of tweets to search for
  -s, --console         Print results to console
  
Example
-------
python3 main.py -a "auth.json" -k "google_sheet_url_key" -q "CVE" "Hacker" "Advanced Persistent Threat" -c 100 -s
