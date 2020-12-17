from urllib.parse import (
    quote, quote_plus, unquote, 
    unquote_plus, parse_qs, urlparse
)

class URL:
    def __init__(self, stdin):
        self.stdin = stdin

    def url_encode(self):
        return quote(self.stdin)

    def url_encode_plus(self):
        return quote_plus(self.stdin)

    def url_decode(self):
        return unquote(self.stdin)

    def url_decode_plus(self):
        return unquote_plus(self.stdin)

    def parse_query_string(self):
        if "http" in self.stdin or "www" in self.stdin:
            return parse_qs(urlparse(self.stdin).query)
        return parse_qs(self.stdin)

