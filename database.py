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
    
def populate_supplies_in_stock(curr):
    #add_column(curr, "Supplies_In_Stock", "type", "TEXT")
    #add_column(curr, "Supplies_In_Stock", "amount", "INTEGER")
    edit_cell(curr, "Supplies_In_Stock", "amount", 2000, "Vegetables")
    edit_cell(curr, "Supplies_In_Stock", "amount", 3000, "Meat")
    
def feed_dinos(curr):
    #get daily totals
    curr.execute("select Pounds_of_Food_Per_Day from dinosaurs where Type_Of_Food = 'Meat'")
    total_meat_eaten = 0
    total_veg_eaten = 0
    list_of_meat_pounds = curr.fetchall()
    for num in list_of_meat_pounds:
        total_meat_eaten = total_meat_eaten + num[0]
    curr.execute("select Pounds_of_Food_Per_Day from dinosaurs where Type_Of_Food = 'Vegetables'")
    list_of_veg_pounds = curr.fetchall()
    for num in list_of_veg_pounds:
        total_veg_eaten = total_veg_eaten + num[0]
    
    #subtract totals from stockpile
    curr.execute("select amount from Supplies_In_Stock where type = 'Meat'")
    stock_meat_pounds = curr.fetchall()[0][0]
    new_stock_meat_num = stock_meat_pounds - total_meat_eaten
    curr.execute("select amount from Supplies_In_Stock where type = 'Vegetables'")
    stock_veg_pounds = curr.fetchall()[0][0]
    new_stock_veg_num = stock_veg_pounds - total_veg_eaten
    edit_cell(curr, "Supplies_In_Stock", "amount", new_stock_veg_num, "Vegetables")
    edit_cell(curr, "Supplies_In_Stock", "amount", new_stock_meat_num, "Meat")
    if(new_stock_veg_num <= 0):
        edit_cell(curr, "Supplies_In_Stock", "amount", 0, "Vegetables")
        notification = "Out of vegetables. Order more."
    if(new_stock_meat_num <= 0):
        edit_cell(curr, "Supplies_In_Stock", "amount", 0, "Meat")
        notification = "Out of meat. Order more."
    print(notification)
    
def order_more_supplies(curr, how_many, item):
    curr.execute("select Cost_Per_Unit from Supplies_In_Stock where type = '{i}'".format(i=item))
    cost = curr.fetchall()[0][0] * how_many
    curr.execute("select amount from Supplies_In_Stock where type = 'Money'")
    money = curr.fetchone()[0]
    
    if money >= cost:
        money = money - cost
        edit_cell(curr, "Supplies_In_Stock", "amount", money, 'Money')
        
        curr.execute("select amount from Supplies_In_Stock where type = '{i}'".format(i=item))
        amount_in_stock = curr.fetchall()[0][0]
        total = amount_in_stock + how_many
        edit_cell(curr, "Supplies_In_Stock", "amount", total, item)
        
    else:
        print("Cannot purchase. You do not have enough money.")

def main():

	database = "ZooManagement.db"
	conn = create_connection(database)
	curr = conn.cursor()
	#wash_all_dinos(curr)
	#wash_dino(curr, "Hippo")
	#update_days_since_bath(curr)
	#populate_food_types(curr)
	#populate_food_per_day(curr)
	#populate_supplies_in_stock(curr)
	#feed_dinos(curr)
	order_more_supplies(curr, 10000000000, 'Vegetables')
	with conn:
		#select(conn, "dinosaurs")
		select(conn, "Supplies_In_Stock")
	conn.commit()
	makeGUI()
	


if __name__ == '__main__':
	main() 
