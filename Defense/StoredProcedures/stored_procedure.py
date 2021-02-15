from mysql.connector import connect 
from os import environ

def get_email_addr(cursor, stored_proc_name, *stored_proc_args):
	result = cursor.callproc(stored_proc_name, [*stored_proc_args])
	email = result[2]
	print(email)

if __name__ == "__main__":
	from sys import argv
	username = argv[1]
	password = argv[2]

	mydb = connect(
		host="localhost",
		user="root",
		password=environ["MYSQL_PASS"],
		database="app")

	cursor = mydb.cursor()
	get_email_addr(cursor, "get_email_addr", username, password, None)