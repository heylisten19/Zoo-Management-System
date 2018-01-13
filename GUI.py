from tkinter import *
import tkinter


top = tkinter.Tk()

t = Text(top,height = 30, width = 30)
t.pack()

f = open("hello.txt")
data = f.read()
f.close()
t.insert(END, data)


top.mainloop()
