import sqlite3
import tkinter
from tkinter import *

 
 
def create_connection(ZooManagement):
	try:
		conn = sqlite3.connect('ZooManagement.db')
		return conn
	except Error as e:
		print(e)
  
def dinosaur_search(conn,column,label):
	cur = conn.cursor()
	cur.execute("SELECT type, {cn} FROM dinosaurs".format(cn = column))
 
	rows = cur.fetchall()
	with open('searchoutput.txt', 'w') as f:
		print("|	TYPE			|		" + label + "				|\n ",file=f )
		for item in rows:
			print("|	" + str(item[0]) + "			|		" + str(item[1]) + "				|",file =f)		
	
				
def supplies_search(conn):
	cur = conn.cursor()
	cur.execute("SELECT * FROM Supplies_In_Stock")
	rows = cur.fetchall()
	with open('searchoutput.txt', 'w') as f:
		print("|	TYPE OF FOOD		|		AMOUNT		|	COST PER UNIT			|\n ", file=f)
		for item in rows:
			print("|	" + str(item[0]) + "		|		" + str(item[1]) + "		|		" +str(item[2]) + "		|", file = f)

def makeGUI():
    top = tkinter.Tk()
    top.title("Search Results")
    t = Text(top,height = 30, width = 100)
    t.pack()
    #v = ("| Type | ", label, " |")
    #label1 = Label(t, text = v )
    #label1.pack()
    
    f = open("searchoutput.txt")
    data = f.read()
    f.close()
    t.insert(END, data)
    top.mainloop()


top = Tk()
top.title("Search Engine")
frame = Frame(top)
frame.grid(column = 0, row=0, sticky =(N,W,E,S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0,weight =1)
frame.pack(pady=100, padx = 100)
#t = Text(top,height = 30, width = 100)
#t.pack()
label = Label(frame, text = "What would you like to search for?")
label.pack()
search = StringVar()
search.set("")
option = OptionMenu(frame, search, "Age", "Medicine", "Last Bath", "Food Type","Food Per Day", "Supplies")
option.pack()
#entry_box = Entry(t, textvariable = search).place(x=80, y= 50)
def search_criteria():
        string = str(search.get())
        database = "ZooManagement.db"
        # create a database connection
        conn = create_connection(database)
        with conn:
                if(string == "Medicine"):
                        dinosaur_search(conn, "medicines", "MEDICINE")
                elif(string == "Age"):
                        dinosaur_search(conn, "age", "AGE")
                elif(string == "Food Type"):
                        dinosaur_search(conn, "Type_Of_Food", "TYPE OF FOOD")
                elif(string == "Last Bath"):
                        dinosaur_search(conn, "Days_Since_Last_Bath", "LAST BATH (in Days)")
                elif(string == "Food Per Day"):
                        dinosaur_search(conn, "Pounds_of_Food_Per_Day", "Food Per Day (in lbs)")
                elif(string == "Supplies"):
                        supplies_search(conn)
                else:
                        print("This search did not work")
        makeGUI()
	#if (string == "medicines"):
		
	#else:
#		print("Your name is not Wall-e. Go away, " + string)
	#s = str(search.get())
	#if (s == "blah")
	#button = Button(t, text = "Search", height =1, width = 4).place (x=250, y= 50)
button = Button(frame, text = "Search", height = 1, width = 4,command = search_criteria)# .place(x= 250, y = 50)
button.pack()
top.mainloop()


#def printstatements(s):
#	database = "ZooManagement.db"
#	conn = create_connection(database)
#	with conn:
#		if(s == "medicines"):
#			print(medicines(conn))
#		else:
#			print("This search did not work")
			

#def main():
#	database = "ZooManagement.db"
	#query = input()
 
	# create a database connection
	#conn = create_connection(database)
	#with conn:
		#if(search == "medicines"):
		#	print(medicines(conn))
		#else
		#	print("This search did not work")
#	makeGUI()
 
 
#if __name__ == '__main__':
#	main()
