from argparse import ArgumentParser as AP

def arg_parse():
    p = AP(
        description="Performing encoding, hashing, encryption, "
        "and compression algorithms"
        )

    # url encoding args 
    p.add_argument("-urlenc","--url-encode",action="store_true",help="URL encode string")
    p.add_argument("-urldec","--url-decode",action="store_true",help="URL decode string")
    p.add_argument("-urlencpls","--url-encode-plus",action="store_true",
            help="URL encode string using + sign as space")
    p.add_argument("-urldecpls","--url-decode-plus",action="store_true",
        help="URL decode url string using + sign for spaces")
    # bases args
    p.add_argument("-b85","--base85",action="store_true",help="Convert string to base85")
    p.add_argument("-fb85","--from-base85",action="store_true",help="Convert string to base64")
    p.add_argument("-b64","--base64",action="store_true",help="Convert string to base64")
    p.add_argument("-fb64","--from-base64",action="store_true",help="Convert string to base64")
    p.add_argument("-b32","--base32",action="store_true", help="Convert string to base64")
    p.add_argument("-fb32","--from-base32",action="store_true",help="Convert string to base64")
    p.add_argument("-b16","--base16",action="store_true",help="Convert string to base64")
    p.add_argument("-fb16","--from-base16",action="store_true",help="Convert string to base64")

    # hex args
    p.add_argument("-hex", "--hexadecimal",action="store_true",help="Convert string hex")
    p.add_argument("-fhex", "--from-hexadecimal",action="store_true",help="Convert from hex")
    p.add_argument("-hexd", "--hexdump", action="store_true",
            help="Get hexdump of file")
    p.add_argument("-fhexdump", "--from-hexadecimal-dump", action="store_true",
            help="From hexdump to original file")

    # 
    return p.parse_args()
