from platform import system
from argparse import ArgumentParser
from os.path import abspath
from os import stat
from datetime import datetime as dt
from sys import exit
from colored import fg, attr
from random import randint
from hashlib import (
    md5, sha1, sha256, sha512
)

__author__ = "Alexis Rodriguez"
__date__   = 20201201


parser = ArgumentParser(description="Extract file metadata")
parser.add_argument("-f", "--file", help="File to extract metadata from")


def get_file_hashes(f):

    with open(f, "rb") as file_:
        file_bytes = file_.read()

        md5_hash = (
            "\t[%sMD5%s]: %s"
            % (fg(randint(1, 220)), attr(0), md5(file_bytes).hexdigest())
            )

        sha1_hash = (
            "\t[%sSHA1%s]: %s"
            % (fg(randint(1, 220)), attr(0), sha1(file_bytes).hexdigest())
            )

        sha256_hash = (
            "\t[%sSHA256%s]: %s"
            % (fg(randint(1, 220)), attr(0), sha256(file_bytes).hexdigest())
            )

        sha512_hash = (
            "\t[%sSHA512%s]: %s"
            % (fg(randint(1, 220)), attr(0), sha512(file_bytes).hexdigest())
            )

        return md5_hash, sha1_hash, sha256_hash, sha512_hash


if __name__ == "__main__":

    args = parser.parse_args()

    if not args.file:
        print("(-) Please provide the `-f` argument")
        exit(1)

    file_stats = stat(args.file)
    SYSTEM = system()

    print("\nFile: %s%s%s\n" % (fg(255), args.file, attr(0)))

    if SYSTEM in ("Linux", "Darwin"):
        ctime = (
            "\t[%sFile Metadata Changed on%s]: %s"
            % (fg(randint(1, 220)), attr(0), dt.fromtimestamp(file_stats.st_ctime))
            )

    elif SYSTEM == "Windows":
        ctime = (
            "\t[%sFile Created On%s]: %s"
            % (fg(randint(1, 220)), attr(0), dt.fromtimestamp(file_stats.st_ctime))
            )

    else:
        print("(-) Unsupported operating system")
        
    modified_on = (
        "\t[%sLast Modified On%s]: %s"
        % (fg(randint(1, 220)), attr(0), dt.fromtimestamp(file_stats.st_mtime))
        )

    access_on = (
        "\t[%sLast Accessed On%s]: %s"
        % (fg(randint(1, 220)), attr(0), dt.fromtimestamp(file_stats.st_mtime))
        )

    file_perm = (
        "\t[%sPermissions%s]: %s"
        % (fg(randint(1, 220)), attr(0), (oct(file_stats.st_mode)[-3:]))
        )

    owner_id = (
        "\t[%sOwner ID%s]: %s"
        % (fg(randint(1, 220)), attr(0), file_stats.st_uid)
        )

    group_id = (
        "\t[%sGroup ID%s]: %s"
        % (fg(randint(1, 220)), attr(0), file_stats.st_gid)
        )

    file_size = (
        "\t[%sFile Size%s]: %s"
        % (fg(randint(1, 220)), attr(0), file_stats.st_size)
        )

    num_of_hard_links = (
        "\t[%sHard Links%s]: %s"
        % (fg(randint(1, 220)), attr(0), file_stats.st_nlink)
        )

    inode = (
        "\t[%sInode #%s]: %s"
        % (fg(randint(1, 220)), attr(0), file_stats.st_ino)
        )

    print(ctime)
    print(modified_on)
    print(access_on)
    print(file_perm)
    print(owner_id)
    print(group_id)
    print(file_size)
    print(num_of_hard_links)
    print(inode)
    
    print(
        "\n\t[%sFile Hashes%s]:"
        % (fg(randint(1, 220)), attr(0))
        )

    # File hashes
    for h in get_file_hashes(args.file):
        print("\t"+h)

