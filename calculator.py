# import tkinter library
from tkinter import *

# create root wiget first 
root = Tk()

#define commands
def clickMe():
    myLabel = Label(root, text = "button clicked")
    myLabel.grid()

# initialize label 
labelHello = Label(root, text="Hello World!")
labelTwo = Label(root, text="Label two")

# initialize button
buttonOne = Button(root, text="me", command=clickMe)

# put into root using .grid row col
labelHello.grid(row=1, column=2)
labelTwo.grid(row=1, column=1)
buttonOne.grid(row=2, column=2)

# run the wiget
root.mainloop()