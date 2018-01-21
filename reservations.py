import sqlite3

def create_connection(ZooManagement):
	try:
		conn = sqlite3.connect('ZooManagement.db')
		return conn
	except Error as e:
		print(e)

def select(conn):
	curr = conn.cursor()
	curr.execute("select size from reservations")
	rows = curr.fetchall()
	size = rows
	for row in rows:
		total_size = sum(int(size[int(row)]))
		print (total_size)
		
		
def main():

	database = "ZooManagement.db"

	conn = create_connection(database)
	with conn:
		print("All Tasks:")
		select(conn)
'''CREATE TABLE reservations ( 
	name INTEGER NOT NULL, 
	size TEXT NULL);'''


if __name__ == '__main__':
	main() 
