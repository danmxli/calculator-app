# import tkinter library
from tkinter import *

# global variables

# create root wiget first 
root = Tk()
root.geometry("400x400")

# initialize entry widget
entryName = Entry(root, width=40, borderwidth=6)

# define function
# update clickMe to populate the entry widget
def saveNum():
    global name
    name = int(entryName.get())

def multiplyTen():
    global name
    name *= 10
    entryName.delete(0, END)
    entryName.insert(0, name)

# initialize label 
labelHello = Label(root, text="Hello world")
labelName = Label(root, text="Enter a number")  

# initialize button
getName = Button(root, text="Save number", command=saveNum)
getMultiple = Button(root, text="Multiply by 10", command=multiplyTen)

# put into root using .grid row col
labelHello.grid(row=1, column=2)
labelName.grid(row=1, column=1)
getName.grid(row=2, column=2)
entryName.grid(row=1, column =4)
getMultiple.grid(row=3, column=1)

# run the wiget
root.mainloop()

