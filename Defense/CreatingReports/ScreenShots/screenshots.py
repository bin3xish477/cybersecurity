from tarfile import open as taropen
from zipfile import ZipFile as zfopen
from sys import exit
from argparse import ArgumentParser
from colored import fg, attr
from time import sleep
from glob import glob
from os import sep, mkdir
from os.path import join, exists
from random import randint


try:
    from pyscreenshot import grab
except ImportError:
    print(
        "[-] Please run `pip3 install -r requirements.txt` " \
        "to install script dependencies..."
        )
    exit(1)


__author__ = "Alexis Rodriguez"
__date__   = 20201204


parser = ArgumentParser(description="Taking screenshots as you work")
parser.add_argument("OUTDIR", help="Directory to output screenshots to")
parser.add_argument(
	"INTERVAL", help="Number of seconds to wait between screenshots"
	)
parser.add_argument(
	"-c", "--create_archive",
	choices=("zip", "tar"),
	help="Create Tar archive file of directory with screenshots"
	)
parser.add_argument(
	"-m", "--max-screenshots",
	help="Maximum number of screenshots to capture"
	)


def take_screenshot(outdir: str, interval: int, screenshot_count: int):

	img = grab()
	print(
		"\r[%sATTENTION%s] %s Screenshots captured ..."
		% (fg(randint(1, 220)), attr(0), screenshot_count), end=""
		)
	png = join(outdir, f"screenshot_{screenshot_count}.png")
	img.save(png)
	sleep(int(interval))


def create_archive(outdir: str, archive_type: str):

	screenshots_files = glob(f"{outdir}{sep}*.png")			
	if archive_type == "zip":
		with zfopen(f"{outdir}.zip", 'w') as zip_archive:
			for sf in screenshots_files:
				zip_archive.write(sf)
		print(f"[+] Created zip archive {outdir}.zip")

	elif archive_type == "tar":
		with taropen(f"{outdir}.tar", 'w') as tar_archive:
			for sf in screenshots_files:
				tar_archive.add(sf)	
		print(f"[+] Created tar archive {outdir}.zip")


if __name__ == "__main__":
	args = parser.parse_args()

	if not exists(args.OUTDIR):
		mkdir(args.OUTDIR)

	num_of_screenshots = 0

	try:
		print("[!!!] Press CTRL+C to stop program ...")
		if args.max_screenshots:
			while num_of_screenshots < args.max_screenshots:
				num_of_screenshots += 1
				take_screenshot(args.OUTDIR, args.INTERVAL, num_of_screenshots)
		else:
			while True:
				num_of_screenshots += 1
				take_screenshot(args.OUTDIR, args.INTERVAL, num_of_screenshots)
	except KeyboardInterrupt:
		print("\n[!] Stopping program ...")

	if args.create_archive:
		create_archive(args.OUTDIR, args.create_archive)
