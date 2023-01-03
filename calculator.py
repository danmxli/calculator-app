# import tkinter library
from tkinter import *

# root window
root = Tk()
root['background']='#e9efed'

# entry widget for user
userEntry = Entry(root, width=30, borderwidth=7, font=('Arial 20'))

# populate entry with number widget
def clickNumber(num):
    global operationSign
    temp = userEntry.get()
    userEntry.delete(0, END)
    userEntry.insert(0, str(temp) + str(num))


# clear operation function
def clearOperation():
    global userInput
    global operationSign
    userInput = 0
    operationSign == " "
    userEntry.delete(0, END)

# do operation function definition, only two parameters // test
def equalOperation():
    global userInput
    global operationSign
    
    rightArugment = userEntry.get()
    
    userEntry.delete(0, END)
    if operationSign == "+":
        userEntry.insert(0, int(userInput) + int(rightArugment))
    if operationSign == "-":
        userEntry.insert(0, int(userInput) - int(rightArugment))
    if operationSign == "*":
        userEntry.insert(0, int(userInput) * int(rightArugment))
    

# store user entry function
def storeEntry():
    global userInput 
    userInput = userEntry.get()
    userEntry.delete(0, END)

# arithmetic sign definition
def addSign():
    global operationSign
    operationSign = "+"
    storeEntry()

def subtractSign():
    global operationSign
    operationSign = "-"
    storeEntry()

def multiplySign():
    global operationSign
    operationSign = "*"
    storeEntry()

def divideSign():
    global operationSign

def expSign():
    global operationSign

def sqrtSign():
    global operationSign

# create photoimage for each button
add_icon = PhotoImage(file=r"C:\Users\danmu\my_projects\calculator-app\calculator_icons\plus.png")
minus_icon = PhotoImage(file=r"C:\Users\danmu\my_projects\calculator-app\calculator_icons\minus.png")
multiply_icon = PhotoImage(file=r"C:\Users\danmu\my_projects\calculator-app\calculator_icons\multiply.png")
divide_icon = PhotoImage(file=r"C:\Users\danmu\my_projects\calculator-app\calculator_icons\divide.png")
exp_icon = PhotoImage(file=r"C:\Users\danmu\my_projects\calculator-app\calculator_icons\exp.png")
sqrt_icon = PhotoImage(file=r"C:\Users\danmu\my_projects\calculator-app\calculator_icons\sqrt.png")
equals_icon = PhotoImage(file=r"C:\Users\danmu\my_projects\calculator-app\calculator_icons\equals.png")

# numeric buttons
button_1 = Button(root, text="1", height=5, width=7, command=lambda: clickNumber(1))
button_2 = Button(root, text="2", height=5, width=7, command=lambda: clickNumber(2))
button_3 = Button(root, text="3", height=5, width=7, command=lambda: clickNumber(3))
button_4 = Button(root, text="4", height=5, width=7, command=lambda: clickNumber(4))
button_5 = Button(root, text="5", height=5, width=7, command=lambda: clickNumber(5))
button_6 = Button(root, text="6", height=5, width=7, command=lambda: clickNumber(6))
button_7 = Button(root, text="7", height=5, width=7, command=lambda: clickNumber(7))
button_8 = Button(root, text="8", height=5, width=7, command=lambda: clickNumber(8))
button_9 = Button(root, text="9", height=5, width=7, command=lambda: clickNumber(9))
button_0 = Button(root, text="0", height=5, width=7, command=lambda: clickNumber(0))
button_decimal = Button(root, text=".", height=5, width=7)
button_sign = Button(root, text="+/-", height=5, width=7)

# operation buttons 
button_add = Button(root, height=60, width=60, image=add_icon, command=lambda: addSign())
button_subtract = Button(root, height=60, width=60, image=minus_icon, command= lambda: subtractSign())
button_multiply = Button(root, height=60, width=60, image=multiply_icon, command= lambda: multiplySign())
button_divide = Button(root, text="/", height=4, width=7)
button_exp = Button(root, text="^", height=4, width=7)
button_sqrt = Button(root, text="r", height=4, width=7)

button_equals = Button(root, height=50, width=350, image= equals_icon, command= lambda: equalOperation())
button_clear = Button(root, text="CLEAR", command=lambda: clearOperation())

# put onto root window
userEntry.grid(row=0, column=0)
button_equals.grid(row=1,column=0)
button_clear.grid(row=0, column=1)

button_7.grid(row=1, column=4)
button_8.grid(row=1, column=5)
button_9.grid(row=1, column=6)

button_4.grid(row=2, column=4)
button_5.grid(row=2, column=5)
button_6.grid(row=2, column=6)

button_1.grid(row=3, column=4)
button_2.grid(row=3, column=5)
button_3.grid(row=3, column=6)

button_0.grid(row=4, column=5)

button_decimal.grid(row=4, column=4)
button_sign.grid(row=4, column=6)

button_add.grid(row=2, column=0)
button_subtract.grid(row=3, column=0)
button_multiply.grid(row=4, column=0)
# button_divide.grid(row=5, column=0)
# button_exp.grid(row=6, column=0)
# button_sqrt.grid(row=7, column=0)


# run app
root.mainloop()