# import tkinter library
from tkinter import *

# root window
root = Tk()

# entry widget for user
userEntry = Entry(root, width=45, borderwidth=7)

# error handling invalid user input function

# do operation function definition, only two parameters
def equalOperation():
    global userInput
    global operationSign

# arithmetic sign definition
def addSign():
    global userInput
    global operationSign

def subtractSign():
    global userInput
    global operationSign

def multiplySign():
    global userInput
    global operationSign

def divideSign():
    global userInput
    global operationSign

def expSign():
    global userInput
    global operationSign

def sqrtSign():
    global userInput
    global operationSign

# number buttons
button_1 = Button(root, text="1", height=5, width=7)
button_2 = Button(root, text="2", height=5, width=7)
button_3 = Button(root, text="3", height=5, width=7)
button_4 = Button(root, text="4", height=5, width=7)
button_5 = Button(root, text="5", height=5, width=7)
button_6 = Button(root, text="6", height=5, width=7)
button_7 = Button(root, text="7", height=5, width=7)
button_8 = Button(root, text="8", height=5, width=7)
button_9 = Button(root, text="9", height=5, width=7)
button_0 = Button(root, text="0", height=5, width=7)

# operation buttons
button_add = Button(root, text="+", height=4, width=7)
button_subtract = Button(root, text="-", height=4, width=7)
button_multiply = Button(root, text="*", height=4, width=7)
button_divide = Button(root, text="/", height=4, width=7)
button_exp = Button(root, text="^", height=4, width=7)
button_sqrt = Button(root, text="r", height=4, width=7)
button_equals = Button(root, text="=", height=2, width=35)

# put onto root window
userEntry.grid(row=0, column=0)
button_equals.grid(row=1,column=0)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)

button_0.grid(row=4, column=2)

button_add.grid(row=2, column=0)
button_subtract.grid(row=3, column=0)
button_multiply.grid(row=4, column=0)
# button_divide.grid(row=5, column=0)
# button_exp.grid(row=6, column=0)
# button_sqrt.grid(row=7, column=0)


# run app
root.mainloop()