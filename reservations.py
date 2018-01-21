import sqlite3

def create_connection(ZooManagement):
	try:
		conn = sqlite3.connect('ZooManagement.db')
		return conn
	except Error as e:
		print(e)

def select_for_reservations(conn):
	curr = conn.cursor()
	curr.execute("select size from reservations")
	rows = curr.fetchall()
	cap = 150 # this is the total amount of spaces for the reservations
	total = 0
	for row in rows:
		#print(row[0])
		total = row[0] + total
	print(total)
	if (total > cap):
		print("There are no spaces left")
	else:
		print("There are ", cap - total, " spaces left")
		
		
		
def main():

	database = "ZooManagement.db"

	conn = create_connection(database)
	with conn:
		print("All Tasks:")
		select_for_reservations(conn)



if __name__ == '__main__':
	main() 
