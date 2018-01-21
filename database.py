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

def select(conn, table):
    curr = conn.cursor()
    curr.execute("select * from {tn}".format(tn=table))
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
    #add_column(curr, "dinosaurs", "Day_Of_Last_Bath", "INTEGER")
    curr.execute("UPDATE dinosaurs SET 'Day_Of_Last_Bath' = CURRENT_TIMESTAMP WHERE type = '{d}'".format(d =dino))
    
def wash_all_dinos(curr):
    curr.execute("UPDATE dinosaurs SET 'Day_Of_Last_Bath' = CURRENT_TIMESTAMP")

def populate_food_types(curr):
    #add_column(curr, "dinosaurs", "Type_Of_Food", "TEXT")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Meat'", "T-Rex")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Vegetables'", "Hippo")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Vegetables'", "Triceratop")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Meat'", "Velociraptor")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Vegetables'", "Stegosaurus")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Vegetables'", "Brachiosaurus")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Vegetables'", "Iguanadon")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Meat'", "Megalosaurus")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Vegetables'", "Brontosaurus")
	edit_cell(curr, "dinosaurs", "Type_Of_Food", "'Meat'", "Crocodile")
	
def populate_food_per_day(curr):
    #add_column(curr, "dinosaurs", "Pounds_of_Food_Per_Day", "INTEGER")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 200, "T-Rex")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 88, "Hippo")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 175, "Triceratop")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 100, "Velociraptor")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 125, "Stegosaurus")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 200, "Brachiosaurus")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 150, "Iguanadon")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 150, "Megalosaurus")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 200, "Brontosaurus")
    edit_cell(curr, "dinosaurs", "Pounds_of_Food_Per_Day", 100, "Crocodile")
    
def supplies_in_stock(curr):
    #add_column(curr, "Supplies_In_Stock", "type", "TEXT")
    #add_column(curr, "Supplies_In_Stock", "amount", "INTEGER")
    edit_cell(curr, "Supplies_In_Stock", "amount", 2000, "Vegetables")
    edit_cell(curr, "Supplies_In_Stock", "amount", 3000, "Meat")
    
#def eat(curr):
    
    

def main():

	database = "ZooManagement.db"
	conn = create_connection(database)
	curr = conn.cursor()
	#wash_all_dinos(curr)
	#wash_dino(curr, "Hippo")
	#update_days_since_bath(curr)
	#populate_food_types(curr)
	#populate_food_per_day(curr)
	supplies_in_stock(curr)
	with conn:
		#select(conn, "dinosaurs")
		select(conn, "Supplies_In_Stock")
	conn.commit()
	makeGUI()
	


if __name__ == '__main__':
	main() 
