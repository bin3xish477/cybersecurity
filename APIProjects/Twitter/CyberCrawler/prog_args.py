from argparse import ArgumentParser

def parse_args():
    parser=ArgumentParser(
        description="Twitter Trending Cyber News or Vulnerabilities Crawler"
    )
    parser.add_argument(
        "-q", "--query",
        type=str, nargs="+",
        metavar="[SearchTerm]",
        help="The keyword/s to search for"
    )
    parser.add_argument(
        "-a", "--auth-file", metavar="FILENAME",
        help="JSON file containing Google Sheets API identity info"
    )
    parser.add_argument(
        "-k", "--url-key", metavar="KEY",
        help="The random key found within the URL of the google sheets doc"
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        help="The number of tweets to search for"
    )
    parser.add_argument(
        "-s", "--console",
        action="store_true",
        help="Print results to console"
    )

    return parser.parse_args()
