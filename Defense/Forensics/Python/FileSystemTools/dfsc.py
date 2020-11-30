#!/usr/bin/env python3

from hashlib import (
    md5, sha1, sha224,
    sha256, sha384, sha512
)
from argparse import ArgumentParser
from colored import fg, attr
from enum import Enum
from time import sleep
from os.path import exists, getsize, abspath
from os import walk
from sys import exit
from csv import writer


###################################################
# Change this to ignore permissions exception error
ignore_permission_exception = False

csv_fields_ = ["AbsoluteFilePath", "FileHash", "FileSize"]


def handle_err(err_msg, exception: Exception=None): 
    """Handles all program errors/exceptions"""
    if exception is not None:
        print(err_msg)
        exit(1)
    else:
        print(err_msg, "\n", repr(exception))
        exit(1)

###########################################
# Enum class for allowed hashing algorithms
class HashAlgo(Enum):
    MD5 = "md5"
    SHA1 = "sha1"
    SHA224 = "sha224"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"


def prog_args():
    parser = ArgumentParser(
        prog="dfsc.py",
        description="File system change detector"
        )
    ###################
    # Program arguments
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
            often to check for file system changes (seconds, default=10)"
        )

    return parser.parse_args()


#######################
# Hash class definition
class Hash():
    def __init__(
        self, dirname: str, hash_algo: HashAlgo
    ):
        self.dirname = dirname
        self.hash_algo = hash_algo

    def dir_exists(self):
        """Checks if file/dir exists"""
        return exists(self.dirname)

    def run(self, ignore_permission_exception: bool=False):
        """Open and interates over all the files in `self.dirname`"""

        file_path_and_hash = []

        if self.dir_exists():
            with open("sys_files.csv", "w") as w:
                w.truncate(0)
                w.seek(0)
                csvwriter = writer(w)
                csvwriter.writerow(csv_fields_)
                for root, dirs, files in walk(self.dirname):
                    for f in files:
                        file_meta = []
                        abs_file_path = root + "/" + f 
                        if f in ("dfsc.py", "sys_files.csv"):
                            continue
                        file_size = getsize(abs_file_path)
                        try:
                            print(abs_file_path, "File size:", file_size)
                            file_meta.append(abs_file_path)
                            ###########################
                            # TODO: 
                            #  - open file and hash file content 
                            #  - write csv row with csvwriter
                            #file_meta.append(file_hash)
                            file_meta.append(file_size)
                            csvwriter.writerow(file_meta)
                        except OSError as e:
                            if ignore_permission_exception:
                                continue
                            handle_err("(-) An error occured accessing file", e)


    def hash(self, f):
        """Hashes a file"""
        pass

    def recompute(self, interval: int=10):
        """Recompute all hashes for files in target directory"""
        sleep(interval)
        self.run(ignore_permission_exception=ignore_permission_exception)


def main():
    args = prog_args()
    #print(args)

    # Create Hash obj
    hasher = Hash(args.dir, args.hash_algo)
    # Begin hashing
    hasher.run(ignore_permission_exception=ignore_permission_exception)

    # if `-l` and `-u` args are provided
    if args.live and args.update:
        hasher.recompute(interval=args.update)
    # if only `-l` arg is provided
    elif args.live and not args.update:
        hasher.recompute()
    else:
        exit(1)
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("(+) Exiting program")
        exit(1)
    
