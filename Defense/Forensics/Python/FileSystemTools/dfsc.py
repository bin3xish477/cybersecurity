#!/usr/bin/env python3

from hashlib import (
    md5, sha1, sha224,
    sha256, sha384, sha512
)
from argparse import ArgumentParser
from colored import fg, attr
from enum import Enum
from time import sleep, perf_counter
from os.path import (
    exists, dirname, abspath,
    join 
)
from os import walk, remove
from glob import glob
from sys import exit
from csv import writer, reader
from random import choice


__author__ = "Alexis Rodriguez"
__date__   = 20201201


###################################################
# Change this to ignore permissions exception error
ignore_permission_exception = False

csv_fields_ = ["AbsoluteFilePath", "FileHash"]

############################
# allowed hashing algorithms
hash_algos = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

def handle_err(err_msg, exception: Exception=None): 
    """Handles all program errors/exceptions"""
    
    if exception is not None:
        print(err_msg)
        exit(1)
    else:
        print(err_msg, "\n", repr(exception))
        exit(1)


def prog_args():

    parser = ArgumentParser(
        prog="dfsc.py",
        description="Detect File System Change"
        )
    ###################
    # Program arguments
    parser.add_argument(
        "-d", "--dir", 
        metavar="DIR",
        default=".",
        help="Monitor changes to a specified \
            directory and not entire file system, default='/'"
        )
    parser.add_argument(
        "-a", "--hash-algo", 
        choices=hash_algos,
        default="md5",
        help="The type of hashing algorithm to use, default='md5'"
        )
    parser.add_argument(
        "-w", "--wait", 
        metavar="INT",
        default=10,
        help="The seconds to wait before performing the second round of hashing" \
            ", default=10"
        )

    return parser.parse_args()


#######################
# Hash class definition
class Hash():

    def __init__(
        self, directory: str, hash_algo: str, wait: int
    ):

        if directory == ".":
            self.directory = dirname(abspath(__file__))
        else:
            self.directory = directory 

        self.hash_algo = hash_algo
        self.wait = wait
        self.round = 1
        self.f1 = "".join([choice("abcdefghijklmnopqrstuvwxyz") for _ in range(6)]) + ".csv"
        self.f2 = "".join([choice("abcdefghijklmnopqrstuvwxyz") for _ in range(6)]) + ".csv"

        for f in glob("*.csv"):
            remove(f)

    def dir_exists(self):
        """Checks if file/dir exists"""
        
        return exists(self.directory)

    def run(self, ignore_permission_exception: bool=False):
        """Open and interates over all the files in `self.dirname`"""

        if self.round == 1:
            file_name = self.f1
        else:
            file_name = self.f2

        if self.dir_exists():
            with open(file_name, "w") as w:
                w.truncate(0)
                w.seek(0)
                csvwriter = writer(w)
                csvwriter.writerow(csv_fields_)
                for root, _, files in walk(self.directory):
                    for f in files:
                        file_meta = []
                        abs_file_path = join(root, f)
                        file_hash = self.hash_file(abs_file_path)
                        try:
                            file_meta.append(abs_file_path)
                            file_meta.append(file_hash)
                            csvwriter.writerow(file_meta)
                        except OSError as e:
                            if ignore_permission_exception:
                                continue
                            handle_err("(-) An error occured accessing file", e)
                self.round += 1


    def hash_file(self, f):
        """Hashes a file"""

        with open(f, "rb") as fb:
            file_bytes = fb.read()
            # TODO: hash file content based on HashAlgo value
            if self.hash_algo == "md5":
                return md5(file_bytes).hexdigest()

            elif self.hash_algo == "sha1":
                return sha1(file_bytes).hexdigest()

            elif self.hash_algo == "sha224":
                return sha224(file_bytes).hexdigest()

            elif self.hash_algo == "sha256":
                return sha256(file_bytes).hexdigest()

            elif self.hash_algo == "sha384":
                return sha384(file_bytes).hexdigest()

            elif self.hash_algo == "sha512":
                return sha512(file_bytes).hexdigest()

    def diff(self):

        with open(self.f1) as r1, open(self.f2) as r2:
            file_1 = reader(r1, delimiter=',')
            file_2 = reader(r2, delimiter=',')

            next(file_1)
            next(file_2)

            for f1_data, f2_data in zip(file_1, file_2):
                print("-----")
                print(f1_data)
                print(f2_data)

    def recompute(self):
        sleep(self.wait)
        self.run(ignore_permission_exception=ignore_permission_exception)


def main():
    args = prog_args()
    #print(args)

    # Create Hash obj
    hasher = Hash(args.dir, args.hash_algo, int(args.wait))
    # Begin first round of hashing
    start = perf_counter()
    hasher.run(ignore_permission_exception=ignore_permission_exception)
    # Perform second round of hashing
    hasher.recompute()
    end = perf_counter()
    # Compare csv files for file changes
    hasher.diff()

    print(f"Completed in {end - start} seconds")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("(+) Exiting program")
        exit(1)
    
