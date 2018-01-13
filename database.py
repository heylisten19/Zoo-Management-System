import sqlite3
import tkinter
from tkinter import *

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
    with open('outputforgui.txt', 'w') as f:
        for row in rows:
            print (row)
            f.write("%s\n" % str(row))
			
def makeGUI():
    top = tkinter.Tk()

    t = Text(top,height = 30, width = 100)
    t.pack()

    f = open("outputforgui.txt")
    data = f.read()
    f.close()
    t.insert(END, data)


    top.mainloop()		
    
def add_column(curr, table_name, new_column, column_type):
    curr.execute("ALTER TABLE {tn} ADD COLUMN '{nc}' {ct}".format(tn=table_name, nc=new_column, ct=column_type))
    

def main():

	database = "ZooManagement.db"
	conn = create_connection(database)
	curr = conn.cursor()
	#curr.execute('.headers on')
	#curr.execute(".mode column")
	with conn:
		select(conn)
	#add_column(curr, "dinosaurs", "Days Since Last Bath", "INTEGER")
	makeGUI()
	


if __name__ == '__main__':
	main() 
