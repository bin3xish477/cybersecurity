from urllib.parse import (
    quote, quote_plus, unquote, 
    unquote_plus, parse_qs
)


def url_encode(url: str): return quote(url)
def url_encode_plus(url: str): return quote_plus(url)
def url_decode(url: str): return unquote(url)
def url_decode_plus(url: str): return unquote_plus(url)
def parse_query_string(query_string: str): return parse_qs(query_string)


