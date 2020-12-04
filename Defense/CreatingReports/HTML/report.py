#!/usr/bin/env python3

# light bootstrap download page:
# - https://www.creative-tim.com/product/light-bootstrap-dashboard

from argparse import ArgumentParser
from os.path import join
from os import getcwd
from shutil import copytree
from collections import Counter
from jinja2 import 


__author__ = "Alexis Rodriguez"
__date__   = 20201203


parser = ArgumentParser(
		prog=f"{__file__}",
		description="Create HTML report"
		)
#parser.add_argument("OUTPUT_DIR", help="Directory to dump HTML report files into")


def create_html_table(data: list):

	html_table = ""
	for entry in data:
		html_table += f"""
		<tr>
			<td>{entry[0]}</td>
			<td>{entry[1]}</td>
			<td>{entry[2]}</td>
			<td>{entry[3]}</td>
		</tr>
		"""

	return html_table


def create_template(table_data: str, output_dir: str):
	cwd = getcwd()
	table_out = join(output_dir, "table.html")
	bootstrap = join(cwd, "light-bootstrap-dashboard-master")
	shutil.copytree(bootstrap, output_dir)

	with open(table_out, "w") as tw:
		tw.write(TABLE.render(table_body=table_data))	


def main():
	args = parser.parse_args()

	acquisition_data = [
		["00001", "2020-11-02", "John Wick", "Signed In"],
		["00002", "2020-11-03", "John Wick", "Signed Out"],
		["00003", "2020-11-05", "John Wick", "Signed In"],
		["00004", "2020-11-07", "John Wick", "Signed Out"],
		["00005", "2020-11-15", "John Wick", "Signed Out"],
		["00006", "2020-11-17", "John Wick", "Signed In"],
		["00007", "2020-11-18", "John Wick", "Signed Out"],
		["00008", "2020-11-21", "John Wick", "Signed In"],
		["00009", "2020-11-25", "John Wick", "Signed Out"]
	]	

	html_table = create_html_table(acquisition_data)
	print(html_table)


if __name__ == '__main__':
	main()