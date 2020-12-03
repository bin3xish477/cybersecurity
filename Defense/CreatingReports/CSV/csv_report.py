from csv import writer
from argparse import ArgumentParser
from os.path import join, exists
from os import mkdir


__author__ = "Alexis Rodriguez"
__date__   = 20201203


parser = ArgumentParser()
parser.add_argument("OUT_DIR", help="Directory to output report to")


def create_csv_report(
		data: list, csv_headers: list,
		out_dir: str, report_name: str="report.csv"
	):

	with open(join(out_dir, report_name), "w", newline='') as csvf:
		csvwriter = writer(csvf)
		csvwriter.writerow(csv_headers)
		csvwriter.writerows(data)
	

def main():

	args = parser.parse_args()

	if not exists(args.OUT_DIR):
		mkdir(args.OUT_DIR)

	example_acquisition_data = [
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

	acquisition_data_headers = ["EventID", "Date", "User Name", "Action"]

	create_csv_report(
		example_acquisition_data, 
		acquisition_data_headers,
		args.OUT_DIR, 
		report_name="example_report.csv"
		)



if __name__ == '__main__':
	main()