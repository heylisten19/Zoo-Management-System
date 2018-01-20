import sqlite3
import tkinter
from tkinter import *
import subprocess
from datetime import datetime, timedelta
import time

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
    curr.execute("ALTER TABLE {tn} ADD COLUMN '{nc}' {ct};".format(tn=table_name, nc=new_column, ct=column_type))
    
def edit_cell(curr, table_name, column, new_info, row_name):
    curr.execute("UPDATE {tn} SET '{cn}' = {info} WHERE type = '{row}';".format(tn=table_name, cn=column, info=new_info, row=row_name))
    
def update_days_since_bath(curr):
    curr.execute("UPDATE dinosaurs SET 'Days Since Last Bath' = Cast(julianday('now') - julianday(Day_Of_Last_Bath) as Integer)")

def wash_dino(curr, dino):
    curr.execute("UPDATE dinosaurs SET 'Day_Of_Last_Bath' = CURRENT_TIMESTAMP WHERE type = '{d}'".format(d =dino))
    
def wash_all_dinos(curr):
    curr.execute("UPDATE dinosaurs SET 'Day_Of_Last_Bath' = CURRENT_TIMESTAMP")
    

def main():

	database = "ZooManagement.db"
	conn = create_connection(database)
	curr = conn.cursor()
	#add_column(curr, "dinosaurs", "Day_Of_Last_Bath", "INTEGER")
	#edit_cell(curr, "dinosaurs", "Days Since Last Bath", 4, "Hippo")
	#wash_all_dinos(curr)
	#wash_dino(curr, "Hippo")
	update_days_since_bath(curr)
	with conn:
		select(conn)
	conn.commit()
	makeGUI()
	


if __name__ == '__main__':
	main() 
