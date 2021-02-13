from mysql.connector import connect 
from os import environ

def invoke_stored_procedure(cursor, stored_proc_name):
	cursor.callproc(stored_proc_name)
	print("Superheros:")
	for result in cursor.stored_results():
		for entry in result.fetchall():
			print("\t", *entry)

if __name__ == "__main__":
	mydb = connect(
		host="localhost",
		user="root",
		password=environ["MYSQL_PASS"],
		database="marvel")

	cursor = mydb.cursor()
	invoke_stored_procedure(cursor, "get_superheros")