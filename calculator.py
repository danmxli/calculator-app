# import tkinter library
from tkinter import *

# create root wiget first 
root = Tk()

# initialize wiget
labelHello = Label(root, text="Hello World!")
labelTwo = Label(root, text="Label two")

# put into root using .grid row col
labelHello.grid(row=1, column=2)
labelTwo.grid(row=2, column=1)

# run the wiget
root.mainloop()