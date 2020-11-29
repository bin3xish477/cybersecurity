#!/usr/bin/env python3

from hashlib import (
    md5, sha1, sha224,
    sha256, sha384, sha512
)
from argparse import ArgumentParser
from colored import fg, attr
from enum import Enum
from time import sleep
from os.path import exists
from os import walk
from sys import exit


def handle_err(err_msg, exception: Exception=None): 
    """Handles all program errors/exceptions"""
    if exception is not None:
        print(err_msg)
        exit(1)
    else:
        print(err_msg, "\n", repr(exception))
        exit(1)

##
# Enum class for allowed hashing algorithms
##
class HashAlgo(Enum):
    MD5 = "md5"
    SHA1 = "sha1"
    SHA224 = "sha224"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"


def prog_args():
    parser = ArgumentParser(
        prog="detect_file_system_changes.py",
        description="File system change detector"
        )
    ##
    # Program arguments
    ##
    parser.add_argument(
        "-d", "--dir", 
        metavar="DIR",
        help="Monitor changes to a specified \
            directory and not entire file system"
        )
    parser.add_argument(
        "-a", "--hash-algo", 
        choices=HashAlgo,
        help="The type of hashing algorithm to generate"
        )
    parser.add_argument(
        "-l", "--live", 
        action="store_true",
        help="Program executes repeatedly to \
            watch live changes to target directory"
        )
    parser.add_argument(
        "-u", "--update", 
        metavar="INT",
        help="If `-l` is used, specify how \
            often to check for file system changes (seconds, default=5)"
        )

    return parser.parse_args()


##
# Hash class definition
##
class Hash():
    def __init__(
        self, dirname: str, hash_algo: HashAlgo
    ):
        self.dirname = dirname
        self.hash_algo = hash_algo

    def dir_exists(self):
        """Checks if file/dir exists"""
        return exists(self.dirname)

    def run(self):
        """Open and interates over all the files and directories in `self.dirname`"""
        if self.dir_exists():
            pass
            try:
                for root, dirs, files in walk(self.dirname):
                    pass
            except OSError as e:
                handle_err(e, "(-) An error occured accessing file...")

    def hash(self, f):
        """Hashes a file"""
        pass

    def recompute(self, interval: int=5):
        """Recompure all hashes for files in target directory"""
        sleep(self.interval)
        self.run()



def main():
    args = prog_args()
    #print(args)

    # Create Hash obj
    hasher = Hash(args.dir, args.hash_algo)
    # Begin hashing
    hasher.run()

    # if `-l` and `-u` args are provided
    if args.live and args.update:
        hasher.recompute(interval=args.update)
    # if only `-l` arg is provided
    elif args.live and not args.update:
        hasher.recompute()
    

if __name__ == "__main__":
    main()
    
