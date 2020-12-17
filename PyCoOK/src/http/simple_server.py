from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


class SServer:
    def __init__(self, stdin):
        self.port = stdin

    def run(self):
        handler = SimpleHTTPRequestHandler
        with TCPServer(("", self.port), handler) as httpd:
            print(f"[+] Server running on port {self.port}")
            httpd.serve_forever()
