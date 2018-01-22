import sqlite3
import tkinter
from tkinter import *

 
 
def create_connection(ZooManagement):
	try:
		conn = sqlite3.connect('ZooManagement.db')
		return conn
	except Error as e:
		print(e)
  
def specific_search(conn,column):
	cur = conn.cursor()
	cur.execute("SELECT type, {cn} FROM dinosaurs".format(cn = column))
 
	rows = cur.fetchall()
	with open('searchoutput.txt', 'w') as f:
		for row in rows:
			print(row)
			f.write("%s\n" % str(row))
def makeGUI():
    top = tkinter.Tk()
    top.title("Outcome Of the Search")
    t = Text(top,height = 30, width = 100)
    t.pack()

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
option = OptionMenu(frame, search, "Age", "Medicine", "Bath")
option.pack()
#entry_box = Entry(t, textvariable = search).place(x=80, y= 50)
def search_criteria():
        string = str(search.get())
        database = "ZooManagement.db"
        # create a database connection
        conn = create_connection(database)
        if(string == "Medicine"):
                with conn:
                        specific_search(conn, "medicines")
                makeGUI()
        elif(string == "Age"):
                with conn:
                        specific_search(conn, "age")
                makeGUI()
        else:
                print("This search did not work")

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
