# Simple calculator with GUI
from tkinter import *

root = Tk()
myLabel = Label(root, text="Hello world")
myLabel1 = Label(root, text="cum")
myLabel2 = Label(root, text="")

myLabel.grid(row = 0, column= 0)
myLabel1.grid(row = 2, column=2)
myLabel2.grid(row = 1, column = 1)

root.mainloop()