import sqlite3

def create_connection(ZooManagement):
	try:
		conn = sqlite3.connect('ZooManagement.db')
		return conn
	except Error as e:
		print(e)

def select(conn):
	curr = conn.cursor()
	curr.execute("select * from dinosaurs")

	rows = curr.fetchall()
	with open('hello.txt', 'w') as f:
		for row in rows:
			print (row)
			f.write("%s\n" % str(row))

def main():

	database = "ZooManagement.db"

	conn = create_connection(database)
	with conn:
		print("All Tasks:")
		select(conn)
CREATE TABLE reservation ( 
	name INTEGER NOT NULL, 
	size TEXT NULL);


if __name__ == '__main__':
	main() 
