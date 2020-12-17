from argparse import SUPPRESS, ArgumentParser as AP

__version__ = 1.0

def hash_cmd_custom_help():
    return """\
usage: pycook hash ARG [-h] [-a md5,sha1,sha224...]

positional arguments:
  ARG                    string/file to encode
                         (NOTE: ARG must go before `-a` option if `-a` is used)

optional arguments:
    -h, --help           show this help message and exit
    -a, --hash-algo      hashing algorithm to use, supported algorithms:
                                                    - md5
                                                    - sha1
                                                    - sha224
                                                    - sha256 (default)
                                                    - sha384
                                                    - sha512
                                                    - sha3_224
                                                    - sha3_256
                                                    - sha3_384
                                                    - sha3_512
                                                    - blake2b
                                                    - blake2s"""

def arg_parse():
    p = AP(description="""
Perform common cybersecurity tasks like encoding, hashing,
text manipulation, crafting reverse shells, etc with a single tool""",
        )


    p.add_argument("-v", "--version",action="version",version=f"PyCoOK {__version__}",help="Get PyCoOK version")
    subparsers = p.add_subparsers(title="commands", dest="cmd", help="subcommand help")

    base_p = subparsers.add_parser("base",help="run `pycook base -h` for command help")
    bin_p = subparsers.add_parser("bin",help="run `pycook bin -h` for command help")
    hex_p = subparsers.add_parser("hex",help="run `pycook hex -h` for command help")
    url_p = subparsers.add_parser("url",help="run `pycook url -h` for command help")
    hash_p = subparsers.add_parser("hash",help="run `pycook hash -h` for command help")
    http_p = subparsers.add_parser("http",help="run `pycook http -h` for command help")
    revs_p = subparsers.add_parser("revs",help="run `pycook revs -h` for command help")
    ptn_p = subparsers.add_parser("ptn",help="run `pycook ptn -h` for command help")

    # bases args
    base_p.add_argument("-85","--base85",action="store_true",help="base85 encode string/file")
    base_p.add_argument("-f85","--from-base85",action="store_true",help="from base85 encoded string/file to ascii string")
    base_p.add_argument("-64","--base64",action="store_true",help="base64 encode string/file")
    base_p.add_argument("-f64","--from-base64",action="store_true",help="from base64 encoded string/file to ascii string")
    base_p.add_argument("-32","--base32",action="store_true",help="base32 encoding string/file")
    base_p.add_argument("-f32","--from-base32",action="store_true",help="from base32 encoded string/file to ascii string")
    base_p.add_argument("-16","--base16",action="store_true",help="base16 encode string/file")
    base_p.add_argument("-f16","--from-base16",action="store_true",help="from base16 encoded string/file to ascii string")
    base_p.add_argument("ARG",help="string/file to encode")
    
    # binary args
    bin_p.add_argument("-b", "--binary",action="store_true",help="binary encode string/file")
    bin_p.add_argument("-f", "--from-binary",action="store_true",help="from binary (0's and 1's) string/file to ascii string")
    bin_p.add_argument("ARG",help="string/file to encode")
    

    # hex args
    hex_p.add_argument("-x", "--hexadecimal",action="store_true",help="hexadecimal encode string/file")
    hex_p.add_argument("-f", "--from-hexadecimal",action="store_true",help="from hexadecimal encode string/file to ascii string")
    hex_p.add_argument("-d", "--hexdump", action="store_true",help="perform hexdump of string/file")
    hex_p.add_argument("ARG",help="string/file to encode")

    # url encoding args 
    url_p.add_argument("-e","--url-encode",action="store_true",help="URL encode string")
    url_p.add_argument("-d","--url-decode",action="store_true",help="URL decode string")
    url_p.add_argument("-ep","--url-encode-plus",action="store_true",help="URL encode string using `+` as spaces")
    url_p.add_argument("-dp","--url-decode-plus",action="store_true",help="URL decode string using `+` as spaces")
    url_p.add_argument("-pq","--parse-query",action="store_true",help="parse query string of a URL")
    url_p.add_argument("ARG",help="string/file to encode")

    # hashing
    hash_p.add_argument("ARG",help="string/file to hash")
    hash_p.add_argument("-a","--hash-algo",nargs="+", default=["sha256"],help="hashing algorithm to use")
    
    # compression

    # http
    http_p.add_argument("-s", "--simple-server",action="store_true",help="run simple HTTP server")
    http_p.add_argument("-p", "--port",default=8080,help="port for simpleHTTP server to listen on")

    # reverse shells
    revs_p.add_argument("-s", "--revshell",default="bsh_tcp_1",help="The reverse shell to generate, run `pycook revs -l` to list available reverse shells (default=bsh_tcp_1)")
    revs_p.add_argument("-p", "--port",default=1337,help="Port to use for reverse shell (default=1337)")
    revs_p.add_argument("-l", "--list-rev-shells",action="store_true",help="List all available reverse shells")
    revs_p.add_argument("IP",help="IP address to use for reverse shell (required=True)")

    # pattern
    ptn_p.add_argument("-c", "--create",action="store_true",help="create pattern")
    ptn_p.add_argument("-l", "--pattern-length",default=1000,help="length of pattern to create (default=1000)")
    ptn_p.add_argument("-g", "--get-offset",action="store_true",help="create pattern")
    ptn_p.add_argument("-m", "--mem-address",help="specify memory address value (with \\x) to find offset for")

    return p
